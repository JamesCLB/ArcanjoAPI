from flask import request, Blueprint
from app.controllers import validate_json, make_response
from app.schemas import patient_schema_post, patient_schema_put
from app.controllers.patients import add_patient, get_all_patients, upd_patient, delete_patient, get_patient
from app.db import db
from app.exceptions import ValidationError, NotFoundError
from flask_jwt_extended import jwt_required

patients_bp = Blueprint("patients", __name__, url_prefix="/patients")


@patients_bp.route("/<int:id_patient>", methods=["GET"])
@jwt_required()
def get_patient_route(id_patient):
    try:
        response = get_patient(id_patient)

        return make_response(response["status_code"], response["content_name"], response["content"], response["msg"])
    except NotFoundError as e:
        print(e)
        return make_response(e.status_code, "patient", {}, f"Error: {str(e)}")
    except Exception as e:
        print(e)
        return make_response(500, "patient", {}, f"Error: {str(e)}")


@patients_bp.route("/", methods=["POST"])
@validate_json(patient_schema_post)
def add_patient_route():
    try:
        body = request.get_json()
        session = db.session
        response = add_patient(body, session)
        return make_response(response["status"],
                             response["name_content"],
                             response["content"],
                             response["msg"])
    except ValidationError as e:
        print(e)
        return make_response(e.status_code, 'patient', {}, f"erro {str(e)}")
    except Exception as e:
        print(e)
        return make_response(500, "patient", {}, f"erro: {str(e)}")


@patients_bp.route("/", methods=["GET"])
def get_patients_route():
    try:
        response = get_all_patients()
        return make_response(response["status_code"],
                             response["content_name"],
                             response["content"],
                             response["msg"])
    except Exception as e:
        print(e)
        return make_response(500, "patient", {}, f"error: {str(e)}")


@patients_bp.route("/<int:id_patient>", methods=["PUT"])
@validate_json(patient_schema_put)
def put_patient_route(id_patient):
    try:
        session = db.session
        body = request.get_json()
        response = upd_patient(body, id_patient, session)
        return make_response(response["status"],
                             response["name_content"],
                             response["content"],
                             response["msg"])
    except NotFoundError as e:
        print(e)
        return make_response(e.status_code, "patient", {}, f"error: {str(e)}")
    except Exception as e:
        print(e)
        return make_response(400, "patient", {}, f"error: {str(e)}")


@patients_bp.route("/<int:id_patient>", methods=["DELETE"])
def delete_patient_route(id_patient):
    try:
        session = db.session
        response = delete_patient(session, id_patient)

        return make_response(response["status_code"], response["content_name"], response["content"], response["msg"])
    except NotFoundError as e:
        print(e)
        return make_response(e.status_code, "patient", {}, f"error: {str(e)}")
    except Exception as e:
        print(e)
        return make_response(400, "patient", {}, f"error: {str(e)}")
