from app.models.models import Medic
from flask import jsonify
from app.controllers import make_response


def get_medic(id_medic):
    medic_obj = Medic.query.filter_by(id=id_medic).first()

    return medic_obj.to_json()


def get_all_medics():
    medics_obj = Medic.query.all()
    medics_json = [medic.to_json() for medic in medics_obj]

    return jsonify(medics_json)


def add_medic(body, session):
    try:
        if "name" not in body or body["name"].strip() == "":
            return make_response(400, "medic", {}, "medic name required")
        if "specialty" not in body or body["specialty"].strip() == "":
            return make_response(400, "medic", {}, "medic specialty required")
        if "crm" not in body or body["crm"].strip() == "":
            return make_response(400, "medic", {}, "medic crm required")

        new_medic = Medic(name=body["name"], specialty=body["specialty"], crm=body["crm"])

        session.add(new_medic)
        session.commit()

        return make_response(200, "medic", {}, "medic added")
    except Exception as e:
        print(e)
        return make_response(400, "medic", {}, "error to add the medic")


def delete_medic(id_medic, session):
    try:
        medic_obj = Medic.query.filter_by(id=id_medic).first()

        session.delete(medic_obj)
        session.commit()

        return make_response(200, "medic", {}, "medic deleted")
    except Exception as e:
        print(e)
        return make_response(400, "medic", {}, "error to delete patient")


def upd_medic(id_medic, body, session):
    try:
        medic_obj = Medic.query.filter_by(id=id_medic).first()
        if "name" in body:
            medic_obj.name = body["name"]
        if "specialty" in body:
            medic_obj.specialty = body["specialty"]
        if "crm" in body:
            medic_obj.crm = body["crm"]

        session.commit()

        return make_response(200, "medic", medic_obj.to_json(), "medic updated")
    except Exception as e:
        print(e)
        return make_response(200, "medic", {}, "error to update the medic")