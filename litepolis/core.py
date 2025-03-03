import os
import logging
import argparse
import importlib
import subprocess

import ray
from ray import serve
from fastapi import FastAPI

from .routers import public


logging.basicConfig(filename='litepolis.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser()
parser.add_argument("--use-deps-file", type=str, default="~/.litepolis/litepolis-pypi-deps.txt",
                    help="The file listing all litepolis packages needed.")
parser.add_argument("--list-deps", action='store_true', help="List all litepolis packages in deps.")
parser.add_argument("--add-deps", type=list, default=[], help="Add a litepolis packages to deps.")
parser.add_argument("--remove-deps", type=list, default=[], help="Remove a litepolis packages from deps.")
# --init-router
# --init-middleware
# --init-ui
parser.add_argument("--serve", type=str, default="", help="Start LitePolis API service on given Ray cluster.")
args = parser.parse_args()

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


def add_deps(package):
    check_import(package)
    with open(args.use_deps_file, 'r') as f:
        lines = f.readlines()
    packages = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            if '-' in line:
                line = line.replace('-', '_')
            if 'litepolis_' in line.lower():
                packages.append(line)
    if package not in packages:
        with open(args.use_deps_file, 'a') as f:
            f.write(f"{package}\n")


def list_deps():
    with open(args.use_deps_file) as f:
        result = subprocess.run(['pip', 'list'],
                                capture_output=True,
                                text=True, check=True)
        pip_packages = []
        for line in result.stdout.split('\n'):
            line = line.strip()
            if line and not line.startswith('#'):
                if '-' in line:
                    line = line.replace('-', '_')
                if 'litepolis_' in line.lower():
                    pip_packages.append(line)
        for line in f.readlines():
            line = line.strip()
            if line and not line.startswith('#'):
                if '-' in line:
                    line = line.replace('-', '_')
                package = line.strip()
                check_import(package)
                for pip_package in pip_packages:
                    if pip_package.startswith(package + " "):
                        print(pip_package)
                        break


def rm_deps(package):
    with open(args.use_deps_file, 'r') as f:
        lines = f.readlines()
    packages = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            if '-' in line:
                line = line.replace('-', '_')
            if 'litepolis_' in line.lower():
                packages.append(line)
    if package not in packages:
        raise ValueError(f"Package '{package}' not found in dependencies file.")
    else:
        packages.remove(package)
        with open(args.use_deps_file, 'w') as f:
            f.write('\n'.join(packages))


def main():
    if not os.path.exists(args.use_deps_file):
        args.use_deps_file = os.path.expanduser(args.use_deps_file)
        os.makedirs(os.path.dirname(args.use_deps_file), exist_ok=True)
        with open(args.use_deps_file, 'w') as f:
            # f.write('litepolis-router-example\n')
            # f.write('litepolis-middleware-example\n')
            # f.write('litepolis-ui-example\n')
            # if package API not backward compatible, rename to new package e.g. litepolis-router-example-v2
            pass

    if args.list_deps:
        list_deps()
    elif len(args.add_deps):
        for package in args.add_deps:
            add_deps(package)
    elif len(args.remove_deps):
        for package in args.remove_deps:
            rm_deps(package)
    elif len(args.serve):
        ray.init(address=args.serve)

        packages = []
        with open(args.use_deps_file) as f:
            for line in f.readlines():
                line = line.strip()
                if line and not line.startswith('#'):
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

        access_control_policies = []
        for line in routers + user_interfaces:
            m = importlib.import_module(line)
            try:
                app.include_router(
                    m.router,
                    prefix=m.prefix, #prefix = package_name of the extract module
                    dependencies=m.dependencies
                )
            except Exception as e:
                logging.exception(f"Error importing router {line}: {e}")

        for line in middlewares:
            m = importlib.import_module(line)
            try:
                m.add_middleware(app)
            except Exception as e:
                logging.exception(f"Error importing middleware {line}: {e}")

        app.include_router(
            public.router,
            prefix="/api/v1/public"
        )

        @serve.deployment
        @serve.ingress(app)
        class FastAPIWrapper:
            pass

        serve.run(FastAPIWrapper.bind(), route_prefix="/")

if __name__ == '__main__':
    main()
