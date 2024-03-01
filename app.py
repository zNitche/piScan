from piScan import create_app, init_files_structure, generate_docs
import logging


def init_gunicorn_logger():
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


init_files_structure()
generate_docs()

app = create_app()


if __name__ == "__main__":
    APP_PORT = app.config["APP_PORT"]
    APP_HOST = app.config["APP_HOST"]
    DEBUG_MODE = app.config["DEBUG_MODE"]

    app.run(debug=DEBUG_MODE, host=APP_HOST, port=APP_PORT, threaded=True)

else:
    init_gunicorn_logger()
