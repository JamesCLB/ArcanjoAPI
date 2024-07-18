from app.models.models import Patient
from app.controllers import make_response
from flask import jsonify


def get_patient(id_patient):
    try:
        patient_obj = Patient.query.filter_by(id=id_patient).first()

        return patient_obj.to_json()
    except Exception as e:
        print(e)
        return make_response(400, "patient", {}, "error to get patient")


def add_patient(body, session):
    try:
        if "name" not in body or body["name"].strip() == "":
            return make_response(400, "patient", {}, "patient name required")
        name = body["name"]
        if "age" not in body:
            return make_response(400, "patient", {}, "patient age required")
        age = body["age"]

        new_patient = Patient(name=name, age=age)
        session.add(new_patient)
        session.commit()

        return make_response(201, "patient", new_patient.to_json(), "patient added")

    except Exception as e:
        print(e)
        return make_response(400, "patient", {}, "error to add the patient")


def get_all_patients():
    patients_objs = Patient.query.all()
    patients_json = [patient.to_json() for patient in patients_objs]

    return jsonify(patients_json)


def upd_patient(body, patient_id, session):
    try:
        patient_obj = Patient.query.filter_by(id=patient_id).first()
        previous_patient = []
        mod = []
        if "name" in body and body["name"].strip() != "":
            previous_patient.append(patient_obj.name)
            patient_obj.name = body["name"]
            mod.append(body["name"])
        if "age" in body and body["age"] > 0:
            previous_patient.append(patient_obj.age)
            patient_obj.age = body["age"]
            mod.append(body["age"])
        session.commit()

        return make_response(200, "patient", patient_obj, f"patient updated. Previous: {previous_patient} After: {mod}")

    except Exception as e:
        print(e)
        return make_response(400, "patient", {}, f"error to update the patient: {e}")


def delete_patient(session, patient_id):
    try:
        patient_obj = Patient.query.filter_by(id=patient_id).first()

        session.delete(patient_obj)
        session.commit()

        return make_response(200, "patient", patient_obj.to_json(), f"patient {patient_obj.name} deleted")
    except Exception as e:
        print(e)
        return make_response(400, "patient", {}, "error to delete patient")