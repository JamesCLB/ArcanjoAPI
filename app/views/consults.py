from flask import Blueprint, request
from app.core.db import db
from app.controllers.consults import add_consult, get_consults, delete_consult, upd_consult, get_consult
from app.utils import validate_json
from app.schemas import consultation_schema_post, consultation_schema_put
from app.utils import make_response
from app.exceptions import NotFoundError

consult_bp = Blueprint("consults", __name__, url_prefix="/consults")


@consult_bp.route("/<int:id_consult>", methods=["GET"])
def get_consult_route(id_consult):
    try:
        session = db.session
        response = get_consult(session, id_consult)

        return make_response(response["status_code"], response["name_content"], response["content"], response["msg"])
    except NotFoundError as e:
        print(e)
        return make_response(e.status_code, "consult", {}, f"error: {str(e)}")
    except Exception as e:
        print(e)
        return make_response(500, "consult", {}, f"error: {str(e)}")


@consult_bp.route("/", methods=["GET"])
def get_consults_route():
    try:
        response = get_consults()
        return make_response(response["status"], response["name_content"], response["content"], response["msg"])
    except Exception as e:
        print(e)
        return make_response(500, "consults", {}, f"error: {str(e)}")


@consult_bp.route("/<int:id_medic>/<int:id_patient>", methods=["POST"])
@validate_json(consultation_schema_post)
def post_consult_route(id_medic, id_patient):
    try:
        body = request.get_json()
        session = db.session
        response = add_consult(body, session, id_medic, id_patient)
        return make_response(response["status"], response["name_content"], response["content"], response["msg"])
    except NotFoundError as e:
        print(e)
        return make_response(e.status_code, "consult", {}, f"error: {str(e)}")
    except Exception as e:
        print(e)
        return make_response(500, "consult", {}, f"error: {str(e)}")


@consult_bp.route("/<int:id_consult>", methods=["DELETE"])
def delete_consult_route(id_consult):
    try:
        session = db.session
        response = delete_consult(id_consult, session)

        return make_response(response["status_code"], response["name_content"], response["content"], response["msg"])
    except NotFoundError as e:
        print(e)
        return make_response(e.status_code, "consult", {}, f"error: {str(e)}")
    except Exception as e:
        print(e)
        return make_response(500, "consult", {}, f"error: {str(e)}")


@consult_bp.route("/<int:id_consult>", methods=["PUT"])
@validate_json(consultation_schema_put)
def upd_consult_route(id_consult):
    try:
        session = db.session
        body = request.get_json()

        response = upd_consult(id_consult, session, body)

        return make_response(response["status_code"], response["name_content"], response["content"], response["msg"])
    except NotFoundError as e:
        print(e)
        return make_response(500, "consult", {}, f"error: {str(e)}")
