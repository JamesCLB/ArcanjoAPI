from flask import Blueprint, request
from app.controllers.medics import get_all_medics, add_medic, delete_medic, upd_medic, get_medic, login_medic
from app.controllers import validate_json, make_response
from app.schemas import medics_schema_post, medics_schema_put
from app.db import db
from app.exceptions import NotFoundError, ConflictError, ValidationError
from flask_jwt_extended import jwt_required

medics_bp = Blueprint("medics", __name__, url_prefix="/medics")


@medics_bp.route("/login", methods=["POST"])
def login_medic_route():
    try:
        body = request.get_json()
        response = login_medic(body)

        return make_response(response["status_code"],
                             response["content_name"],
                             response["content"],
                             response["msg"])
    except NotFoundError as e:
        print(e)
        return make_response(e.status_code, "medic", {}, f"error: {str(e)}")
    except ValidationError as e:
        print(e)
        return make_response(e.status_code, "medic", {}, f"error: {str(e)}")
    except Exception as e:
        print(e)
        return make_response(500, "medic", {}, f"error: {str(e)}")


@medics_bp.route("/<int:id_medic>", methods=["GET"])
@jwt_required()
def get_medic_route(id_medic):
    try:
        response = get_medic(id_medic)
        return make_response(response["status_code"],
                             response["name_content"],
                             response["content"],
                             response["msg"])
    except NotFoundError as e:
        print(e)
        return make_response(e.status_code, "medic", {}, f"error: {str(e)}")


@medics_bp.route("/", methods=["GET"])
@jwt_required()
def get_medics_route():
    try:
        response = get_all_medics()
        return make_response(response["status_code"],
                             response["content_name"],
                             response["content"],
                             response["msg"])
    except Exception as e:
        print(e)
        return make_response(500, "medic", {}, f"error: {str(e)}")


@medics_bp.route("/", methods=["POST"])
@validate_json(medics_schema_post)
def add_medic_route():
    try:
        body = request.get_json()
        session = db.session

        response = add_medic(body, session)

        return make_response(response["status_code"],
                             response["content_name"],
                             response["content"],
                             response["msg"])
    except ConflictError as e:
        return make_response(409, "medic", {}, f"error: {str(e)}")
    except Exception as e:
        print(e)
        return make_response(500, "medic", {}, f"error: {str(e)}")


@medics_bp.route("/<int:id_medic>", methods=["DELETE"])
def delete_medic_route(id_medic):
    try:
        session = db.session
        response = delete_medic(id_medic, session)

        return make_response(response["status_code"], response["name_content"], response["content"], response["msg"])
    except NotFoundError as e:
        print(e)
        return make_response(e.status_code, "medic", {}, f"error: {str(e)}")
    except ConflictError as e:
        print(e)
        return make_response(e.status_code, "medic", {}, f"error: {str(e)}")
    except Exception as e:
        print(e)
        return make_response(500, "medic", {}, f"error: {str(e)}")


@medics_bp.route("/<int:id_medic>", methods=["PUT"])
@jwt_required()
@validate_json(medics_schema_put)
def put_medic_route(id_medic):
    try:
        session = db.session
        body = request.get_json()
        response = upd_medic(id_medic, body, session)

        return make_response(response["status_code"],
                             response["content_name"],
                             response["content"],
                             response["msg"])

    except NotFoundError as e:
        print(e)
        return make_response(404, "medic", {}, f"error: {str(e)}")

    except Exception as e:
        print(e)
        return make_response(500, "medic", {}, f"error: {str(e)}")
