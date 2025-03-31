from app.models.models import Medic, Consultation
from app.exceptions import NotFoundError, ConflictError, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token


def login_medic(body):
    password = body.get("password")
    email = body.get("email")
    if not password or not email:
        raise ValidationError("Email and password required")
    medic = Medic.query.filter_by(email=email).first()
    if not medic:
        raise NotFoundError("Medic with email not found")
    if not check_password_hash(medic.password_hash, password):
        raise ValidationError(f"Invalid credentials")
    print({"id": medic.id, "role": medic.role})
    token_jwt = create_access_token(identity={"id": medic.id, "role": medic.role})

    return {
        "status_code": 200,
        "content_name": "access_token",
        "content": token_jwt,
        "msg": "Login successfully"
    }


def get_medic(id_medic):
    medic_obj = Medic.query.filter_by(id=id_medic).first()
    if not medic_obj:
        raise NotFoundError(f"Medic with ID {id_medic} not found")

    return {
        "status_code": 200,
        "name_content": "medic",
        "content": medic_obj.to_json(),
        "msg": "Medic returned successfully"
    }


def get_all_medics():
    medics_obj = Medic.query.all()
    medics_json = [medic.to_json() for medic in medics_obj]

    return {
        "status_code": 200,
        "content_name": "medic",
        "content": medics_json,
        "msg": "Medics returned successfully"
    }


def add_medic(body, session):
    if Medic.query.filter_by(crm=body["crm"]).first():
        raise ConflictError(f"Medic with CRM {body["crm"]} already exist")

    if Medic.query.filter_by(email=body["email"]).first():
        raise ConflictError(f"Medic with email {body["email"]} already exist")

    password_hash = generate_password_hash(body["password"])
    del body["password"]

    new_medic = Medic(
        name=body["name"],
        specialty=body["specialty"],
        crm=body["crm"],
        email=body["email"],
        password_hash=password_hash,
        role=body["roles"])

    session.add(new_medic)
    session.commit()

    return {
        "status_code": 201,
        "content_name": "Medic",
        "content": new_medic.to_json(),
        "msg": "Medic added successfully"
    }


def delete_medic(medic_id, session):
    medic_obj = Medic.query.filter_by(id=medic_id).first()

    if not medic_obj:
        raise NotFoundError(f"Medic with ID {medic_id} not found")

    if len(Consultation.query.filter_by(medic_id=medic_id).all()) > 0:
        raise ConflictError(f"Medic with ID {medic_id} have associated consultations")

    session.delete(medic_obj)
    session.commit()

    return {
        "status_code": 200,
        "name_content": "Medic",
        "content": medic_obj.to_json(),
        "msg": "Medic deleted successfully"
    }


def upd_medic(id_medic, body, session):
    medic_obj = Medic.query.filter_by(id=id_medic).first()
    if not medic_obj:
        raise NotFoundError(f"Medic with ID {id_medic} not found")

    if "name" in body:
        medic_obj.name = body["name"]
    if "specialty" in body:
        medic_obj.specialty = body["specialty"]
    if "crm" in body:
        medic_obj.crm = body["crm"]

    session.commit()

    return {
        "status_code": 200,
        "content_name": "Medic",
        "content": medic_obj.to_json(),
        "msg": f"Medic updated successfully."
    }

