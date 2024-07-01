from app.models.models import Patient
from app.controllers import make_response


def add_patient(body, session):
    try:
        if "name" not in body or body["name"].strip() == "":
            return print("error in name")
        name = body["name"]
        if "age" not in body or body["age"].strip() == "":
            return print("error in age")
        age = body["age"]

        new_patient = Patient(name=name, age=age)
        session.add(new_patient)
        session.commit()

        return make_response(201, "patient", new_patient.to_json(), "patient added")

    except Exception as e:
        print(e)
        return make_response(400, "patient", {}, "error to add the patient")
