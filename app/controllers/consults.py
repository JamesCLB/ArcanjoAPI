from datetime import datetime
from app.controllers import make_response
from app.models.models import Consultation, Medic, Patient
from app.db import db


def get_consult(session, id_consult):
    consult_obj = session.query(Consultation).filter(Consultation.id == id_consult).first()
    return make_response(200, "consult", consult_obj.to_json())


def get_consults():
    try:
        consults_obj = db.session.query(Consultation).all()

        consults_json = [consult.to_json() for consult in consults_obj]

        return make_response(200, "consults", consults_json, "consults")
    except Exception as e:
        print(e)
        return make_response(400, "consults", {}, "error to get consults")


def add_consult(body, session, id_medic, id_patient):
    try:
        if "consult_date" not in body or body["consult_date"].strip() == "":
            return make_response(400, "consult", {}, "consult date required")
        if "consult_time" not in body or body["consult_time"].strip() == "":
            return make_response(400, "consult", {}, "consult time required")

        consultation_date_str = f"{body["consult_date"]} {body["consult_time"]}"

        consult_datetime = datetime.strptime(consultation_date_str, "%d/%m/%Y %H:%M")

        patient_obj = session.query(Patient).get(id_patient)
        if not patient_obj:
            return make_response(404, "patient", {}, "error to find patient")
        medic_obj = session.query(Medic).get(id_medic)
        if not medic_obj:
            return make_response(404, "medic", {}, "error to find medic")

        notes = body.get("notes", "")

        new_consult = Consultation(patient_id=id_patient,
                                   medic_id=id_medic,
                                   consult_time=consult_datetime,
                                   notes=notes)

        session.add(new_consult)
        session.commit()

        return make_response(201, "consult", new_consult.to_json(), "consult added successfully")
    except Exception as e:
        print(e)
        return make_response(400, "medic", {}, "error to add consultation")


def delete_consult(id_consult, session):
    try:
        consult_obj = session.query(Consultation).filter(Consultation.id == id_consult).first()

        session.delete(consult_obj)
        session.commit()

        return make_response(200, "consult", consult_obj.to_json(), "consult deleted")
    except Exception as e:
        print(e)
        return make_response(400, "consult", {}, "error to delete consult")


def upd_consult(id_consult, session, body):
    try:
        consult_obj = session.query(Consultation).filter(Consultation.id == id_consult).first()

        if "consult_time" in body and body["consult_time"].strip() != "":
            consult_obj.consult_time = body["consult_time"]
        if "notes" in body and body["notes"].strip() != "":
            consult_obj.notes = body["notes"]

        session.commit()

        return make_response(200, "consult", consult_obj.to_json(), "consult updated")
    except Exception as e:
        print(e)
        return make_response(400, "consult", {}, "error to update the consult")
