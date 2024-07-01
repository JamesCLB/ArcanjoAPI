from flask import Flask
from app.db import db
from app.config import Config
from flask_migrate import Migrate
from views.patients import patients_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(patients_bp)

    db.init_app(app)
    migrate = Migrate(app, db)

    return app
