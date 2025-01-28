from app import jwt
from functools import wraps
from flask_jwt_extended import get_current_user, verify_jwt_in_request
from flask_jwt_extended.exceptions import NoAuthorizationError
from app.models.models import Medic, Patient


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]

    medic = Medic.query.filter_by(id=identity["id"]).first()
    if medic:
        return medic

    patient = Patient.query.filter_by(id=identity["id"]).first()
    if patient:
        return patient

    return None


def check_acess(roles: [str] = []):
    def decorator(f):
        @wraps(f)
        def decorator_function(*args, **kwargs):
            verify_jwt_in_request()

            current_user = get_current_user()

            if current_user.role not in roles:
                raise NoAuthorizationError("Role is now allowed")

            return f(*args, **kwargs)

        return decorator_function()

    return decorator
