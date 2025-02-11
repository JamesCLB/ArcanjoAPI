from functools import wraps
from flask_jwt_extended import get_current_user, verify_jwt_in_request, JWTManager
from flask_jwt_extended.exceptions import NoAuthorizationError
from app.exceptions import AuthorizationError
from app.models.models import Medic, Patient

jwt = JWTManager()


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]

    if identity["role"] == "medic":
        return Medic.query.filter_by(id=identity["id"]).first()

    elif identity["role"] == "patient":
        return Patient.query.filter_by(id=identity["id"]).first()

    return None


def check_access(roles=None):
    if roles is None:
        roles = []

    def decorator(f):
        @wraps(f)
        def decorator_function(*args, **kwargs):
            verify_jwt_in_request()

            current_user = get_current_user()

            if current_user.role not in roles:
                raise AuthorizationError("Role is not allowed")

            return f(*args, **kwargs)

        return decorator_function

    return decorator
