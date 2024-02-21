import dotenv
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'piScan'))

dotenv.load_dotenv(os.path.join(PROJECT_ROOT, ".env"))


class Config:
    MIGRATIONS_DIR_PATH = os.path.join(PROJECT_ROOT, "database", "migrations")

    SCAN_FILES_DIR_PATH = os.path.join(PROJECT_ROOT, "files", "scans")
    SCAN_FILES_THUMBNAILS_DIR_PATH = os.path.join(PROJECT_ROOT, "files", "thumbnails")

    APP_PORT = 8000
    APP_HOST = "0.0.0.0"

    DEBUG_MODE = int(os.getenv("DEBUG", 0))

    DATABASE_URI = f"sqlite:////{PROJECT_ROOT}/database/app.sqlite3"
    REDIS_URI = "127.0.0.1" if DEBUG_MODE else "redis"
    REDIS_PORT = "6000"

    HOST_DOCS = int(os.getenv("HOST_DOCS", 0))
    SWAGGER_SCHEMA_PATH = os.path.join(PROJECT_ROOT, "swagger.json")
    SWAGGER_SERVERS = os.getenv("SWAGGER_SERVERS")
