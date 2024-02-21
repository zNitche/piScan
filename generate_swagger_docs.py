from api_docs import spec
from configs.config import Config
import json
import dotenv
import os
from piScan import PROJECT_ROOT


dotenv.load_dotenv(os.path.join(PROJECT_ROOT, ".env"))


def generate():
    print("Generating swagger.json...")

    try:
        with open(Config.SWAGGER_SCHEMA_PATH, "w") as file:
            json_specs = json.dumps(spec.to_dict(), indent=2)
            file.write(json_specs)

        print(f"Done... Saved to: {Config.SWAGGER_SCHEMA_PATH}")

    except Exception as e:
        print(f"Error while generating swagger json: {str(e)}")


if __name__ == '__main__':
    generate()
