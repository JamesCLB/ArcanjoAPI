from app.models.models import Patient
from app.exceptions import NotFoundError


def get_patient(id_patient):
    patient_obj = Patient.query.filter_by(id=id_patient).first()
    if not patient_obj:
        raise NotFoundError("patient not found")

    return {
        "status_code": 200,
        "content_name": "patient",
        "content": patient_obj.to_json(),
        "msg": "patient returned successfully"
    }


def add_patient(body, session):
    name = body["name"]
    age = body["age"]
    new_patient = Patient(name=name, age=age)
    session.add(new_patient)
    session.commit()

    return {
        'status': 201,
        'name_content': "patient",
        'content': new_patient.to_json(),
        'msg': 'Patient added successfully'
    }


def get_all_patients():
    patients_objs = Patient.query.all()
    patients_json = [patient.to_json() for patient in patients_objs]

    return {
        "status_code": 200,
        "content_name": "patients",
        "content": patients_json,
        "msg": "patients returned successfully"
    }


def upd_patient(body, patient_id, session):
    patient_obj = Patient.query.filter_by(id=patient_id).first()
    if not patient_obj:
        raise NotFoundError("Patient not found")
    if "name" in body:
        patient_obj.name = body["name"]
    if "age" in body:
        patient_obj.age = body["age"]
    session.commit()

    return {
        "status": 200,
        "name_content": "patient",
        "content": patient_obj.to_json(),
        "msg": "Patient updated successfully"
    }


def delete_patient(session, patient_id):
    patient_obj = Patient.query.filter_by(id=patient_id).first()
    if not patient_obj:
        raise NotFoundError("patient not found")

    session.delete(patient_obj)

    session.commit()

    return {
        "status_code": 200,
        "content_name": "patient",
        "content": patient_obj.to_json(),
        "msg": "patient deleted successfully"
    }
