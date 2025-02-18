from datetime import datetime
from app.models.models import Consultation, Medic, Patient
from app.core.db import db
from app.exceptions import NotFoundError


def get_consult(session, id_consult):
    consult_obj = session.query(Consultation).filter(Consultation.id == id_consult).first()
    if not consult_obj:
        raise NotFoundError("consult not found")

    return {
        "status_code": 200,
        "name_content": "consult",
        "content": consult_obj.to_json(),
        "msg": "consult returned successfully"
    }


def get_consults():
    consults_obj = db.session.query(Consultation).all()

    consults_json = [consult.to_json() for consult in consults_obj]

    return {
        "status": 200,
        "name_content": "consults",
        "content": consults_json,
        "msg": "consults returned successfully"
    }


def add_consult(body, session, id_medic, id_patient):
    consultation_date_str = f"{body["consult_date"]} {body["consult_time"]}"

    consult_datetime = datetime.strptime(consultation_date_str, "%d/%m/%Y %H:%M")

    patient_obj = session.query(Patient).get(id_patient)
    if not patient_obj:
        raise NotFoundError("Patient not found")
    medic_obj = session.query(Medic).get(id_medic)
    if not medic_obj:
        raise NotFoundError("Medic not found")

    notes = body.get("notes", "")

    new_consult = Consultation(
        patient_id=id_patient,
        medic_id=id_medic,
        consult_time=consult_datetime,
        notes=notes
    )

    session.add(new_consult)
    session.commit()

    return {
        "status": 201,
        "name_content": "consult",
        "content": new_consult.to_json(),
        "msg": "patient added successfully"
    }


def delete_consult(id_consult, session):
    consult_obj = session.query(Consultation).filter(Consultation.id == id_consult).first()
    if not consult_obj:
        raise NotFoundError("consult not found", 404)
    session.delete(consult_obj)
    session.commit()

    return {
        "status_code": 200,
        "name_content": "consult",
        "content": consult_obj.to_json(),
        "msg": "consult deleted successfully"
    }


def upd_consult(id_consult, session, body):
    consult_obj = session.query(Consultation).filter(Consultation.id == id_consult).first()
    if not consult_obj:
        raise NotFoundError("consult not found", 404)

    if 'consultation_date' in body and 'consultation_time' in body:
        consult_datetime = f"{body['consultation_date']} {body['consultation_time']}"
        new_date = datetime.strptime(consult_datetime, "%d/%m/%Y %H:%M")
        consult_obj.consult_time = new_date

    if "consultation_time" in body and "consultation_date" not in body:
        datetime_obj = consult_obj.consult_time

        date_str = datetime_obj.strftime("%Y-%m-%d")

        new_date = f"{date_str} {body["consultation_time"]}"
        new_date = datetime.strptime(new_date, "%Y-%m-%d %H:%M")

        consult_obj.consult_time = new_date

    elif "consultation_date" in body and "consultation_time" not in body:
        datetime_obj = consult_obj.consult_time

        time_str = datetime_obj.strftime("%H:%M")

        new_date = f"{body["consultation_date"]} {time_str}"
        new_date = datetime.strptime(new_date, "%d/%m/%Y %H:%M")

        consult_obj.consult_time = new_date

    if "medic_id" in body:
        medic_exist = Medic.query.filter_by(id=body["medic_id"]).first()
        if not medic_exist:
            raise NotFoundError("medic not found")
        consult_obj.medic_id = body["medic_id"]

    if "notes" in body:
        consult_obj.notes = body["notes"]

    session.commit()

    return {
        "status_code": 200,
        "name_content": "consult",
        "content": consult_obj.to_json(),
        "msg": "consult updated successfully"
    }
