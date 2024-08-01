from app.db import db
from datetime import date


class Patient(db.Model):
    __tablename__ = "patient"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {"id": self.id, "name": self.name, "age": self.age}


class Medic(db.Model):
    __tablename__ = "medic"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    specialty = db.Column(db.String(40), nullable=False)
    crm = db.Column(db.String(4), nullable=False)

    def to_json(self):
        return {"id": self.id, "name": self.name, "specialty": self.specialty, "crm": self.crm}


class Consultation(db.Model):
    __tablename__ = "consultations"
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"), nullable=False)
    medic_id = db.Column(db.Integer, db.ForeignKey("medic.id"), nullable=False)
    consult_time = db.Column(db.DateTime, nullable=False, default=date.today())
    notes = db.Column(db.Text, nullable=True, default="")

    patient = db.relationship("Patient", backref=db.backref("consultation", lazy=True))
    medic = db.relationship("Medic", backref=db.backref("consultation", lazy=True))

    def to_json(self):
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "medic_id": self.medic_id,
            "consult_time": self.consult_time,
            "notes": self.notes
        }
