import os
import casbin
from fastapi_authz import CasbinMiddleware

def add_middleware(app):
    RBAC_MODEL_CONF = os.get('RBAC_MODEL_CONF', None)
    RBAC_POLICY_CSV = os.get('RBAC_POLICY_CSV', None)
    if (RBAC_MODEL_CONF and os.path.exists(RBAC_MODEL_CONF)
        and RBAC_POLICY_CSV and os.path.exists(RBAC_POLICY_CSV)):
        enforcer = casbin.Enforcer(RBAC_MODEL_CONF, RBAC_POLICY_CSV)
        app.add_middleware(CasbinMiddleware, enforcer=enforcer)
    return app