from flask import request, Blueprint

from app.controllers.patients import add_patient
from app.db import db

patients_bp = Blueprint("patients", __name__, "/patients")


@patients_bp.route("/", methods=["POST"])
def add_patient_route():
    body = request.get_json()
    session = db.session
    return add_patient(body, session)

