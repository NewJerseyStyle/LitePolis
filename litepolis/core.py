import os
import shutil
import inspect
import importlib
import subprocess
import configparser

import ray
from ray import serve
from fastapi import FastAPI
import click

from .utils import DEFAULT_CONFIG_PATH
from .utils import keep, register_config_service

app = FastAPI()

# Removed check_import function as it conflicts with version pinning

@click.group()
@click.pass_context
def cli(ctx):
    """The LitePolis CLI to help you integrate and deploy, or develop new module."""
    pass

@cli.group()
@click.option("--packages-file", type=str, default="~/.litepolis/packages.txt",
                    help="The file listing all litepolis packages needed.")
@click.option("--cluster", type=str, default="auto",
                    help="Start LitePolis API service on given Ray cluster.")
@click.pass_context
def deploy(ctx, packages_file, cluster):
    """Start the LitePolis service."""
    ctx.ensure_object(dict)
    packages_file = os.path.expanduser(packages_file)
    ctx.obj['packages_file'] = packages_file
    ctx.obj['cluster'] = cluster
    if not os.path.exists(packages_file):
        os.makedirs(os.path.dirname(packages_file), exist_ok=True)
        with open(packages_file, 'w') as f:
            # f.write('litepolis-router-example\n')
            # f.write('litepolis-middleware-example\n')
            # f.write('litepolis-ui-example\n')
            # if package API not backward compatible, rename to new package e.g. litepolis-router-example-v2
            # Example with version:
            f.write('litepolis-database-example==0.0.1\n')
            # f.write('litepolis-router-example==0.2.1\n')
            pass

@deploy.command()
@click.pass_context
def list_deps(ctx):
    """Lists required packages and compares with installed versions."""
    packages_file = ctx.obj['packages_file']
    required_packages = {}
    try:
        with open(packages_file, 'r') as f:
            for line in f:
                line = line.strip()
                if len(line) and not line.startswith('#'):
                    if '==' in line:
                        name, version = line.split('==', 1)
                        required_packages[name] = version
                    else:
                        # Handle lines without version specifier if needed, or raise error
                        print(f"Warning: Line '{line}' in {packages_file} is missing version specifier '=='. Skipping.")
    except FileNotFoundError:
        print(f"Error: Packages file '{packages_file}' not found.")
        return

    try:
        result = subprocess.run(['pip', 'list', '--format=freeze'],
                                capture_output=True, text=True, check=True)
        installed_packages = {}
        for line in result.stdout.splitlines():
            if '==' in line:
                name, version = line.split('==', 1)
                # Normalize names (replace _ with - for comparison if needed, though pip freeze usually uses -)
                installed_packages[name.replace('_', '-')] = version
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error running 'pip list': {e}")
        return

    print(f"Dependencies from {packages_file}:")
    print(f"{'Package':<40} {'Required':<15} {'Installed':<15}")
    print("-" * 70)
    for name, req_version in required_packages.items():
        # Normalize required name for lookup
        lookup_name = name.replace('_', '-')
        inst_version = installed_packages.get(lookup_name, "Not Installed")
        print(f"{name:<40} {req_version:<15} {inst_version:<15}")

@deploy.command()
@click.argument('package_spec') # Changed argument name
@click.pass_context
def add_deps(ctx, package_spec):
    """Adds or updates a package dependency. 
    Format: package_name or package_name==version. If no version is specified, the latest version will be used."""
    packages_file = ctx.obj['packages_file']

    if '==' in package_spec:
        new_name, new_version = package_spec.split('==', 1)
    else:
        new_name = package_spec
        new_version = None # Indicate latest version
    # Normalize name for comparison
    new_name_normalized = new_name.replace('_', '-')

    updated_lines = []
    package_found = False
    try:
        with open(packages_file, 'r') as f:
            for line in f:
                stripped_line = line.strip()
                if len(stripped_line) and not stripped_line.startswith('#') and '==' in stripped_line:
                    current_name, current_version = stripped_line.split('==', 1)
                    # Normalize current name for comparison
                    if current_name.replace('_', '-') == new_name_normalized:
                        if new_version:
                            updated_lines.append(f"{new_name}=={new_version}\n") # Use original new_name format
                            print(f"Updating {current_name} from {current_version} to {new_version}")
                        else:
                            updated_lines.append(f"{new_name}\n") # No version specified, just package name
                            print(f"Updating {current_name} (version will be updated to latest if specified)")
                        package_found = True
                    else:
                        updated_lines.append(line)
                else:
                    updated_lines.append(line) # Keep comments, empty lines, or lines without '=='
    except FileNotFoundError:
        print(f"Packages file '{packages_file}' not found. Creating.")
        # If file doesn't exist, we'll create it below

    if not package_found:
        if new_version:
            updated_lines.append(f"{new_name}=={new_version}\n") # Use original new_name format
            print(f"Adding {new_name}=={new_version}")
        else:
            try:
                import importlib.metadata
                version = importlib.metadata.version(new_name)
                updated_lines.append(f"{new_name}=={version}\n")
                print(f"Adding {new_name}=={version} (latest version installed)")
            except importlib.metadata.PackageNotFoundError:
                updated_lines.append(f"{new_name}\n") # No version specified, just package name
                print(f"Adding {new_name} (latest version - version detection failed)")


    # Write the updated list back to the file
    try:
        os.makedirs(os.path.dirname(packages_file), exist_ok=True)
        with open(packages_file, 'w') as f:
            f.writelines(updated_lines)
    except IOError as e:
        print(f"Error writing to packages file '{packages_file}': {e}")
        return

    # Install the package
    install_spec = package_spec if new_version else new_name # Use package_spec if version is given, else just name
    print(f"Installing {install_spec}...")
    try:
        # Use the exact package_spec provided by the user for pip install
        subprocess.run(['pip', 'install', install_spec], check=True, capture_output=True, text=True)
        print(f"Successfully installed {install_spec}.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {install_spec}:")
        print(e.stderr)
        # Consider if we should revert the change in packages.txt here
        print(f"Installation failed. Please check the package name and version.")
    except FileNotFoundError:
         print(f"Error: 'pip' command not found. Make sure pip is installed and in your PATH.")

@deploy.command()
@click.argument('package_name') # Changed argument name
@click.pass_context
def remove_deps(ctx, package_name):
    """Removes a package dependency from the packages file."""
    packages_file = ctx.obj['packages_file']
    # Normalize name for comparison
    package_name_normalized = package_name.replace('_', '-')

    updated_lines = []
    removed = False
    try:
        with open(packages_file, 'r') as f:
            for line in f:
                stripped_line = line.strip()
                if len(stripped_line) and not stripped_line.startswith('#') and '==' in stripped_line:
                    current_name, _ = stripped_line.split('==', 1)
                    # Normalize current name for comparison
                    if current_name.replace('_', '-') == package_name_normalized:
                        removed = True
                        print(f"Removing {stripped_line} from {packages_file}")
                    else:
                        updated_lines.append(line)
                else:
                    updated_lines.append(line) # Keep comments, empty lines, or lines without '=='

        if not removed:
            raise ValueError(f"Package '{package_name}' not found in dependencies file '{packages_file}'.")

        # Write the filtered list back to the file
        with open(packages_file, 'w') as f:
            f.writelines(updated_lines)
        print(f"Successfully removed {package_name} reference from {packages_file}.")
        print("Note: The package itself was not uninstalled from the environment.")

    except FileNotFoundError:
        print(f"Error: Packages file '{packages_file}' not found.")
    except ValueError as e:
         print(f"Error: {e}")
    except IOError as e:
        print(f"Error writing to packages file '{packages_file}': {e}")


@deploy.command()
@click.pass_context
def sync_deps(ctx):
    """Installs all packages listed in the packages file to the specified versions."""
    packages_file = ctx.obj['packages_file']
    print(f"Syncing environment with {packages_file}...")
    packages_to_install = []
    try:
        with open(packages_file, 'r') as f:
            for line in f:
                line = line.strip()
                if len(line) and not line.startswith('#') and '==' in line:
                    packages_to_install.append(line)
    except FileNotFoundError:
        print(f"Error: Packages file '{packages_file}' not found.")
        return

    if not packages_to_install:
        print("No valid package specifications found in the file.")
        return

    all_successful = True
    for package_spec in packages_to_install:
        print(f"Ensuring {package_spec} is installed...")
        try:
            # Use the exact package_spec from the file for pip install
            subprocess.run(['pip', 'install', package_spec], check=True, capture_output=True, text=True)
            # print(f"Successfully installed/verified {package_spec}.") # Optional: reduce verbosity
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package_spec}:")
            print(e.stderr)
            all_successful = False
        except FileNotFoundError:
             print(f"Error: 'pip' command not found. Make sure pip is installed and in your PATH.")
             all_successful = False
             break # Abort if pip is not found

    if all_successful:
        print("Environment synced successfully.")
    else:
        print("Environment sync completed with errors.")


@deploy.command()
@click.pass_context
def init_config(ctx):
    config = configparser.ConfigParser()
    packages_file = ctx.obj['packages_file']
    
    package_names = [] # Store only names for import
    try:
        with open(packages_file) as f:
            for line in f:
                line = line.strip()
                if len(line) and not line.startswith('#'):
                    # Extract package name before '=='
                    package_name = line.split('==', 1)[0]
                    # Normalize name for importlib (replace - with _)
                    import_name = package_name.replace('-', '_')
                    if import_name.startswith('litepolis_'):
                         # Attempt import to check availability (optional, sync_deps should handle installation)
                        try:
                            importlib.import_module(import_name)
                            package_names.append(import_name)
                        except ImportError:
                             print(f"Warning: Package {import_name} (from {line}) not installed. Run 'deploy sync-deps'. Skipping config generation for this package.")

    except FileNotFoundError:
        print(f"Warning: Packages file '{packages_file}' not found during config init.")

    for import_name in package_names:
        m = importlib.import_module(import_name)
        config.add_section(line)
        for k, v in m.DEFAULT_CONFIG.items():
            config.set(line, k, v)

    write_flag = True
    prompt = f"Config file '{DEFAULT_CONFIG_PATH}' already exists. Overwrite?"
    if os.path.exists(DEFAULT_CONFIG_PATH):
        if not click.confirm(prompt):
            write_flag = False
    if write_flag:
        with open(DEFAULT_CONFIG_PATH, 'w') as f:
            config.write(f)

    print(f"Now edit file '{DEFAULT_CONFIG_PATH}' to configure the server.")

def get_apps(ctx, monolithic=False):
    config = configparser.ConfigParser()
    config.read(DEFAULT_CONFIG_PATH)
    keep(config)
    packages_file = ctx.obj['packages_file']

    package_specs = [] # Store full spec like name==version
    try:
        with open(packages_file) as f:
            for line in f:
                line = line.strip()
                if len(line) and not line.startswith('#') and '==' in line:
                     package_specs.append(line)
                elif len(line) and not line.startswith('#'):
                     print(f"Warning: Line '{line}' in {packages_file} is missing version specifier '=='. Skipping.")
    except FileNotFoundError:
         print(f"Warning: Packages file '{packages_file}' not found when getting apps.")


    routers = []
    databases = []
    middlewares = []
    user_interfaces = []
    for spec in package_specs:
        package_name = spec.split('==', 1)[0]
        # Normalize name for importlib and type checking
        import_name = package_name.replace('-', '_')
        if import_name.startswith('litepolis_'):
            parts = import_name.split('_', 2) # Split into 'litepolis', type, rest
            if len(parts) >= 2:
                package_type = parts[1]
                if package_type == 'router':
                    routers.append(import_name)
                elif package_type == 'middleware':
                    middlewares.append(import_name)
                elif package_type == 'database':
                    databases.append(import_name)
                elif package_type == 'ui':
                    user_interfaces.append(import_name)

    # Ensure packages are installed before trying to import them
    # It's better to rely on sync_deps being run beforehand,
    # but a check here can prevent crashes if sync wasn't run.
    print("Checking required packages for application server...")
    all_installed = True
    for spec in package_specs:
         package_name = spec.split('==', 1)[0]
         import_name = package_name.replace('-', '_')
         try:
             importlib.import_module(import_name)
         except ImportError:
             print(f"Error: Required package {import_name} (from spec {spec}) is not installed.")
             print(f"Please run 'litepolis deploy sync-deps' first.")
             all_installed = False
    if not all_installed:
        raise RuntimeError("Missing required packages. Cannot start server.")


    for import_name in databases:
        # m = importlib.import_module(import_name)
        # ray.remote(
        #     m.DatabaseActor
        # ).options(
        #     name=import_name,
        #     get_if_exists=True,
        #     lifetime="detached"
        # ).remote()
        pass

    for import_name in user_interfaces:
        m = importlib.import_module(import_name)
        try:
            app.include_router(m.prefix, m.files, name=m.name)
        except Exception as e:
            print(f"Error importing UI {import_name}: {e}")

    for import_name in routers:
        m = importlib.import_module(import_name)
        try:
            app.include_router(
                m.router,
                prefix=f'/api/{m.prefix}',
                dependencies=m.dependencies
            )
        except Exception as e:
            print(f"Error importing router {import_name}: {e}")

    for import_name in middlewares:
        m = importlib.import_module(import_name)
        try:
            m.add_middleware(app)
        except Exception as e:
            print(f"Error importing middleware {import_name}: {e}")

    return [app]


@deploy.command("local")
@click.pass_context
def auto_init_local(ctx):
    subprocess.run(["ray", "start", "--head"])
    ctx.forward(serve_command)

def auto_init_gcp():
    pass
def auto_init_azure():
    pass
def auto_init_aws():
    pass


@deploy.command("serve")
@click.pass_context
def serve_command(ctx):
    ray.init(address=ctx.obj['cluster'])
    register_config_service()

    app = get_apps(ctx)[0]

    @serve.deployment
    @serve.ingress(app)
    class FastAPIWrapper:
        pass

    serve.run(FastAPIWrapper.bind(), route_prefix="/")


@cli.group()
def create():
    """Initialize a new package from GitHub template repo."""
    pass

def validate_project_name(name: str) -> None:
    """Ensures project name starts with 'litepolis-router-'"""
    name = name.lower()
    name = name.replace('_', '-')
    project_type = inspect.stack()[1][3]
    if not name.startswith(f"litepolis-{project_type}-"):
        raise ValueError(f"Project name must start with 'litepolis-router-'. Got: {name}")
        
def git_reinit(project_path, repo_url):
    content = ''
    setup_py_path = os.path.join(project_path, "setup.py")
    if os.path.exists(setup_py_path):
        with open(setup_py_path, 'r') as f:
            content = f.read()

    repo_name = os.path.basename(repo_url)[:-4]
    project_name = os.path.basename(project_path)
    content = content.replace(repo_name, project_name)

    repo_name = repo_name.lower()
    project_name = project_name.lower()
    content = content.replace(repo_name, project_name)

    repo_name = repo_name.replace('-', '_')
    project_name = project_name.replace('-', '_')
    content = content.replace(repo_name, project_name)

    if os.path.exists(setup_py_path):
        with open(setup_py_path, 'w') as f:
            f.write(content)

    os.rename(
        os.path.join(project_path, repo_name),
        os.path.join(project_path, project_name)
    )

    git_dir = os.path.join(project_path, ".git")
    if os.path.exists(git_dir):
        shutil.rmtree(git_dir)

    import git
    new_repo = git.Repo.init(project_path)

    project_name = os.path.basename(project_path)
    click.secho(f"\nProject {project_name} created!", fg="green", bold=True)
    click.echo(f"Next steps:\n"
               f"cd {project_name}\n"
               f"git remote add origin YOUR_REPO_URL\n"
               f"git push -u origin main")

@create.command()
@click.argument('project_name')
def router(project_name):
    """Initialize a new router package from GitHub templace repo."""
    try:
        validate_project_name(project_name)
    except ValueError as e:
        click.secho(f"Error: {e}", fg="red")
        return

    import git

    # Clone the repository
    click.secho(f"Cloning template into {project_name}...", fg="cyan")
    repo_url = "https://github.com/NewJerseyStyle/LitePolis-router-template.git"
    repo = git.Repo.clone_from(repo_url, project_name)

    git_reinit(project_name, repo_url)


@create.command()
@click.argument('project_name')
def database(project_name):
    """Initialize a new database package from GitHub templace repo."""
    try:
        validate_project_name(project_name)
    except ValueError as e:
        click.secho(f"Error: {e}", fg="red")
        return

    import git

    # Clone the repository
    repo_url = "https://github.com/NewJerseyStyle/LitePolis-database-template.git"
    repo = git.Repo.clone_from(repo_url, project_name)
    git_reinit(project_name, repo_url)


@create.command()
@click.argument('project_name')
def middleware(project_name):
    """Initialize a new middleware package from GitHub templace repo."""
    try:
        validate_project_name(project_name)
    except ValueError as e:
        click.secho(f"Error: {e}", fg="red")
        return

    import git

    # Clone the repository
    repo_url = "https://github.com/NewJerseyStyle/LitePolis-middleware-template.git"
    repo = git.Repo.clone_from(repo_url, project_name)
    git_reinit(project_name, repo_url)

@create.command()
@click.argument('project_name')
def ui(project_name):
    """Initialize a new UI component package from GitHub templace repo."""
    try:
        validate_project_name(project_name)
    except ValueError as e:
        click.secho(f"Error: {e}", fg="red")
        return

    import git

    # Clone the repository
    repo_url = "https://github.com/NewJerseyStyle/LitePolis-ui-template.git"
    repo = git.Repo.clone_from(repo_url, project_name)
    git_reinit(project_name, repo_url)


def main():
    cli(obj={})


def get_test_app():
    from pydantic import BaseModel

    class ctx(BaseModel):
        obj: dict

    packages_file = os.path.expanduser('~/.litepolis/packages.txt')
    return get_apps(
        ctx(obj={'packages_file': packages_file}),
        monolithic=True
    )[0]


if __name__ == '__main__':
    main()