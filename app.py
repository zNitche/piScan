from piScan import create_app, PROJECT_ROOT
import dotenv
import os


dotenv.load_dotenv(os.path.join(PROJECT_ROOT, ".env"))

app = create_app()


if __name__ == "__main__":
    APP_PORT = app.config["APP_PORT"]
    APP_HOST = app.config["APP_HOST"]
    DEBUG_MODE = app.config["DEBUG_MODE"]

    app.run(debug=DEBUG_MODE, host=APP_HOST, port=APP_PORT, threaded=True)
