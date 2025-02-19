from datetime import timedelta


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost:5432/arcanjo"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "5f2c2f36b56d2b65d2c3d1b0d5e7f5c17a30f7f7f7182b70f084e3d6c2d29262"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
