from functools import wraps
from flask_jwt_extended import get_current_user, verify_jwt_in_request, JWTManager
from flask_jwt_extended.exceptions import NoAuthorizationError
from app.exceptions import AuthorizationError
from app.models.models import Medic, Patient

jwt = JWTManager()


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    if "medic" in identity["role"]:
        return Medic.query.filter_by(id=identity["id"]).first()

    elif "patient" in ["role"]:
        return Patient.query.filter_by(id=identity["id"]).first()

    return None


def check_access(acess_roles=None):
    if acess_roles is None:
        acess_roles = []

    def decorator(f):
        @wraps(f)
        def decorator_function(*args, **kwargs):
            verify_jwt_in_request()

            current_user = get_current_user()
            if not any(role in acess_roles for role in current_user.role):
                raise AuthorizationError("Role is not allowed")

            return f(*args, **kwargs)

        return decorator_function

    return decorator
