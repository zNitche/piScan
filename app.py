from piScan import create_app
from config import Config
import os


def generate_docs():
    if Config.HOST_DOCS:
        swagger_json_path = Config.SWAGGER_SCHEMA_PATH

        if swagger_json_path and not os.path.exists(swagger_json_path):
            from generate_swagger_docs import generate

            generate()


def init_files_structure():
    paths = [
        Config.SCAN_FILES_DIR_PATH,
        Config.SCAN_FILES_THUMBNAILS_DIR_PATH
    ]

    for path in paths:
        if not os.path.exists(path):
            os.mkdir(path)


init_files_structure()
generate_docs()

app = create_app()


if __name__ == "__main__":
    APP_PORT = app.config["APP_PORT"]
    APP_HOST = app.config["APP_HOST"]
    DEBUG_MODE = app.config["DEBUG_MODE"]

    app.run(debug=DEBUG_MODE, host=APP_HOST, port=APP_PORT, threaded=True)
