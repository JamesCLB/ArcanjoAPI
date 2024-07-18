from flask import request, Blueprint

from app.controllers.patients import add_patient, get_all_patients, upd_patient, delete_patient, get_patient
from app.db import db

patients_bp = Blueprint("patients", __name__, url_prefix="/patients")


@patients_bp.route("/<int:id_patient>", methods=["GET"])
def get_patient_route(id_patient):
    return get_patient(id_patient)


@patients_bp.route("/", methods=["POST"])
def add_patient_route():
    body = request.get_json()
    session = db.session
    return add_patient(body, session)


@patients_bp.route("/", methods=["GET"])
def get_patients_route():
    return get_all_patients()


@patients_bp.route("/<int:id_patient>", methods=["PUT"])
def put_patient_route(id_patient):
    session = db.session
    body = request.get_json()
    return upd_patient(body, id_patient, session)


@patients_bp.route("/<int:id_patient>", methods=["DELETE"])
def delete_patient_route(id_patient):
    session = db.session
    return delete_patient(session, id_patient)
