from api_docs import spec
from configs.config import Config
import json


def main():
    print("Generating swagger.json...")
    with open(Config.SWAGGER_SCHEMA_PATH, "w") as file:
        json_specs = json.dumps(spec.to_dict(), indent=2)
        file.write(json_specs)

    print(f"Done... Saved to: {Config.SWAGGER_SCHEMA_PATH}")


if __name__ == '__main__':
    main()
