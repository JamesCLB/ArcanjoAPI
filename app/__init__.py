from flask import Flask
from app.db import db
from app.config import Config
from flask_migrate import Migrate
from app.views.patients import patients_bp
from app.views.medics import medics_bp
from app.views.consults import consult_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(patients_bp)
    app.register_blueprint(medics_bp)
    app.register_blueprint(consult_bp)

    db.init_app(app)
    migrate = Migrate(app, db)

    return app
