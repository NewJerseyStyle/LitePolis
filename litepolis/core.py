import os
import importlib
import subprocess
import configparser

import ray
from ray import serve
from fastapi import FastAPI
import click

from .routers import public

DEFAULT_CONFIG_PATH = '~/.litepolis/config.conf'

app = FastAPI()

def check_import(package):
    try:
        importlib.import_module(package)
    except ImportError:
        print(f"Package {package} not found. Triggering pip install...")
        retcode = os.system(f"pip install {package}")
        if retcode != 0:
            raise RuntimeError(f"Package {package} not available,"
                                " please check if it is available on PyPI"
                                " or you may need to build from source.")


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
            f.write('litepolis-router-database\n')
            # f.write('litepolis-router-example\n')
            # f.write('litepolis-middleware-example\n')
            # f.write('litepolis-ui-example\n')
            # if package API not backward compatible, rename to new package e.g. litepolis-router-example-v2
            pass

@deploy.command()
@click.pass_context
def list_deps(ctx):
    with open(ctx.obj['packages_file']) as f:
        result = subprocess.run(['pip', 'list'],
                                capture_output=True,
                                text=True, check=True)
        pip_packages = []
        for line in result.stdout.split('\n'):
            line = line.strip()
            if '-' in line:
                line = line.replace('-', '_')
            if 'litepolis_' in line.lower():
                pip_packages.append(line)
        for line in f.readlines():
            line = line.strip()
            if len(line) and not line.startswith('#'):
                if '-' in line:
                    line = line.replace('-', '_')
                package = line.strip()
                check_import(package)
                for pip_package in pip_packages:
                    if pip_package.startswith(package + " "):
                        print(pip_package)
                        break

@deploy.command()
@click.argument('package')
@click.pass_context
def add_deps(ctx, package):
    packages = []
    with open(ctx.obj['packages_file'], 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if len(line) and not line.startswith('#'):
                if '-' in line:
                    line = line.replace('-', '_')
                if 'litepolis_' in line.lower():
                    packages.append(line)
    check_import(package)
    if package not in packages:
        with open(ctx.obj['packages_file'], 'a') as f:
            f.write(f"{package}\n")

@deploy.command()
@click.argument('package')
@click.pass_context
def remove_deps(ctx, package):
    with open(ctx.obj['packages_file'], 'r') as f:
        lines = f.readlines()
    packages = []
    for line in lines:
        line = line.strip()
        if len(line) and not line.startswith('#'):
            if '-' in line:
                line = line.replace('-', '_')
            if 'litepolis_' in line.lower():
                packages.append(line)
    if package not in packages:
        raise ValueError(f"Package '{package}' not found in dependencies file.")
    else:
        packages.remove(package)
        with open(ctx.obj['packages_file'], 'w') as f:
            f.write('\n'.join(packages))


@deploy.command()
@click.pass_context
def init_config(ctx):
    config = configparser.ConfigParser()
    
    packages = []
    with open(ctx.obj['packages_file']) as f:
        for line in f.readlines():
            line = line.strip()
            if len(line) and not line.startswith('#'):
                check_import(line)
                if '-' in line:
                    line = line.replace('-', '_')
                if '_' in line:
                    package = line.split('_')
                    if package[0] == 'litepolis':
                        packages.append(line)
    
    for line in packages:
        m = importlib.import_module(line)
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

    packages = []
    with open(ctx.obj['packages_file']) as f:
        for line in f.readlines():
            line = line.strip()
            if len(line) and not line.startswith('#'):
                check_import(line)
                if '-' in line:
                    line = line.replace('-', '_')
                if '_' in line:
                    packages.append(line)

    routers = []
    middlewares = []
    user_interfaces = []
    for line in packages:
        package = line.split('_')
        if package[0] == 'litepolis':
            if package[1] == 'router':
                routers.append(line)
            elif package[1] == 'middleware':
                middlewares.append(line)
            elif package[1] == 'ui':
                user_interfaces.append(line)

    for line in user_interfaces:
        pass

    for line in routers + user_interfaces:
        m = importlib.import_module(line)
        router = m.init(config)
        try:
            app.include_router(
                router,
                prefix=f'/api/{m.prefix}',
                dependencies=m.dependencies
            )
        except Exception as e:
            print(f"Error importing router {line}: {e}")

    for line in middlewares:
        m = importlib.import_module(line)
        try:
            m.add_middleware(app, config)
        except Exception as e:
            print(f"Error importing middleware {line}: {e}")

    app.include_router(
        public.router,
        prefix="/api"
    )

    return [app]


def auto_init_local():
    pass
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

@create.command()
@click.argument('local_path')
def router(local_path):
    """Initialize a new router package from GitHub templace repo."""
    import git

    # Clone the repository
    repo_url = "https://github.com/NewJerseyStyle/LitePolis-router-template.git"
    repo = git.Repo.clone_from(repo_url, os.path.abspath(local_path))

@create.command()
@click.argument('local_path')
def middleware(local_path):
    """Initialize a new middleware package from GitHub templace repo."""
    import git

    # Clone the repository
    repo_url = "https://github.com/NewJerseyStyle/LitePolis-router-template.git"
    repo = git.Repo.clone_from(repo_url, os.path.abspath(local_path))

@create.command()
@click.argument('local_path')
def ui(local_path):
    """Initialize a new UI component package from GitHub templace repo."""
    import git

    # Clone the repository
    repo_url = "https://github.com/NewJerseyStyle/LitePolis-router-template.git"
    repo = git.Repo.clone_from(repo_url, os.path.abspath(local_path))


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