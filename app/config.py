import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://user:password@postgres-service:5432/db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False