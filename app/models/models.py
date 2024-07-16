from app.db import db


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {"id": self.id, "name": self.name, "age": self.age}

