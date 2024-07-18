from app.db import db


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {"id": self.id, "name": self.name, "age": self.age}


class Medic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    specialty = db.Column(db.String(40), nullable=False)
    crm = db.Column(db.String(4), nullable=False)

    def to_json(self):
        return {"id": self.id, "name": self.name, "specialty": self.specialty, "crm": self.crm}
