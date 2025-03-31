from flask import Blueprint, request
from app.controllers.medics import get_all_medics, add_medic, delete_medic, upd_medic, get_medic, login_medic
from app.utils import validate_json, make_response
from app.schemas import medics_schema_login, medics_schema_put, medics_schema_add
from app.core.db import db
from app.exceptions import NotFoundError, ConflictError, AuthorizationError
from flask_jwt_extended import jwt_required
from app.core.auth import check_access
from jsonschema import ValidationError

medics_bp = Blueprint("medics", __name__, url_prefix="/medics")


@medics_bp.app_errorhandler(Exception)
def handle_validation_error(error):
    return make_response(500, "Exception", {"medic"}, f"Error: {error.msg}")


@medics_bp.app_errorhandler(ValidationError)
def handle_validation_error(error):
    error_msg = f"Validation error in field: {error.path[0]} : {error.message}" if error.path else f"{error.message}"
    return make_response(400, "Validation error", {}, error_msg)


@medics_bp.app_errorhandler(NotFoundError)
def handle_not_found_error(error):
    return make_response(error.status_code, "Not found error", {}, error.msg)


@medics_bp.app_errorhandler(ConflictError)
def handle_conflict_error(error):
    return make_response(error.status_code, "Conflict error", {}, error.msg)


@medics_bp.app_errorhandler(AuthorizationError)
def handle_authorization_error(error):
    return make_response(error.status_code, "Authorization error", {}, error.msg)


@medics_bp.route("/login", methods=["POST"])
@validate_json(medics_schema_login)
def login_medic_route():
    body = request.get_json()
    response = login_medic(body)

    return make_response(response["status_code"],
                         response["content_name"],
                         response["content"],
                         response["msg"])


@medics_bp.route("/<int:id_medic>", methods=["GET"])
@check_access(["medic"])
@jwt_required()
def get_medic_route(id_medic):
    response = get_medic(id_medic)
    return make_response(response["status_code"],
                         response["name_content"],
                         response["content"],
                         response["msg"])


@medics_bp.route("/", methods=["GET"])
@check_access(["medic"])
@jwt_required()
def get_medics_route():
    response = get_all_medics()
    return make_response(response["status_code"],
                         response["content_name"],
                         response["content"],
                         response["msg"])


@medics_bp.route("/", methods=["POST"])
@jwt_required()
@validate_json(medics_schema_add)
@check_access(["admin"])
def add_medic_route():
    body = request.get_json()
    session = db.session

    response = add_medic(body, session)

    return make_response(response["status_code"],
                         response["content_name"],
                         response["content"],
                         response["msg"])


@medics_bp.route("/<int:id_medic>", methods=["DELETE"])
@check_access("admin")
def delete_medic_route(id_medic):
    session = db.session
    response = delete_medic(id_medic, session)

    return make_response(response["status_code"], response["name_content"], response["content"], response["msg"])


@medics_bp.route("/<int:id_medic>", methods=["PUT"])
@jwt_required()
@check_access("admin")
@validate_json(medics_schema_put)
def put_medic_route(id_medic):
    session = db.session
    body = request.get_json()
    response = upd_medic(id_medic, body, session)

    return make_response(response["status_code"],
                         response["content_name"],
                         response["content"],
                         response["msg"])
