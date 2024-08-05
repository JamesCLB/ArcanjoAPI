from flask import Blueprint, request
from app.db import db
from app.controllers.consults import add_consult, get_consults, delete_consult, upd_consult, get_consult
from app.controllers import validate_json
from app.schemas import consultation_schema_post, consultation_schema_put

consult_bp = Blueprint("consults", __name__, url_prefix="/consults")


@consult_bp.route("/<int:id_consult>", methods=["GET"])
def get_consult_route(id_consult):
    session = db.session
    return get_consult(session, id_consult)


@consult_bp.route("/", methods=["GET"])
def get_consults_route():
    return get_consults()


@consult_bp.route("/<int:id_medic>/<int:id_patient>", methods=["POST"])
@validate_json(consultation_schema_post)
def post_consult_route(id_medic, id_patient):
    body = request.get_json()
    session = db.session
    return add_consult(body, session, id_medic, id_patient)


@consult_bp.route("/<int:id_consult>", methods=["DELETE"])
def delete_consult_route(id_consult):
    session = db.session
    return delete_consult(id_consult, session)


@consult_bp.route("/<int:id_consult>", methods=["PUT"])
@validate_json(consultation_schema_put)
def upd_consult_route(id_consult):
    session = db.session
    body = request.get_json()
    return upd_consult(id_consult, session, body)
