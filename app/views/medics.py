from flask import Blueprint, request
from app.controllers.medics import get_all_medics, add_medic, delete_medic
from app.db import db

medics_bp = Blueprint("medics", __name__, url_prefix="/medics")


@medics_bp.route("/", methods=["GET"])
def get_medics_route():
    return get_all_medics()


@medics_bp.route("/", methods=["POST"])
def add_medic_route():
    body = request.get_json()
    session = db.session

    return add_medic(body, session)


@medics_bp.route("/<int:id_medic>", methods=["DELETE"])
def delete_medic_route(id_medic):
    session = db.session
    return delete_medic(id_medic, session)