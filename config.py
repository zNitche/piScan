import dotenv
import os


dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".env"))


class Config:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    MIGRATIONS_DIR_PATH = os.path.join(CURRENT_DIR, "database", "migrations")

    ROOT_URL_PREFIX = "/api"

    APP_PORT = 8080
    APP_HOST = "0.0.0.0"
    DEBUG_MODE = os.getenv("DEBUG", 0)

    DATABASE_URI = f"sqlite:////{CURRENT_DIR}/database/app.sqlite3"
