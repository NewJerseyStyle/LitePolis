import importlib
import argparse

from ray import serve
from fastapi import FastAPI, Depends

from routers import secure, public
from auth import get_user

parser = argparse.ArgumentParser()
parser.add_argument("--deps", type=str, required=True,
                    default="litepolis-pypi-deps.txt",
                    help="The file listing all litepolis packages needed.")
args = parser.parse_args()

app = FastAPI()

packages = []
with open(args.deps) as f:
    for line in f.readlines():
        if '-' in line:
            line.replace('-', '_')
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
    # check for API dependencies

access_control_policies = []
for line in routers + user_interfaces:
    m = importlib.import_module(line)
    try:
        app.include_router(
            m.router,
            prefix=m.prefix,
            dependencies=m.dependencies
        )
        if importlib.resources.is_resource(m, "rbac_policy.csv"):
            access_control_policies.append(
                importlib.resources.read_text(m, "rbac_policy.csv")
            )
    except:
        # log
        pass

for line in middlewares:
    m = importlib.import_module(line)
    try:
        m.add_middleware(app)
    except:
        # log
        pass

app.include_router(
    public.router,
    prefix="/api/v1/public"
)
app.include_router(
    secure.router,
    prefix="/api/v1/secure",
    dependencies=[Depends(get_user)]
)

@serve.deployment
@serve.ingress(app)
class FastAPIWrapper:
    pass

serve.run(FastAPIWrapper.bind(), route_prefix="/")