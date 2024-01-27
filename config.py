import dotenv
import os


dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".env"))


class Config:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    MIGRATIONS_DIR_PATH = os.path.join(CURRENT_DIR, "database", "migrations")

    APP_PORT = 8080
    APP_HOST = "0.0.0.0"
    DEBUG_MODE = os.getenv("DEBUG", 0)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = f"sqlite:////{CURRENT_DIR}/database/app.sqlite3"
