from piScan.api_spec import spec
from configs.config import Config
import json


def main():
    with open(Config.SWAGGER_SCHEMA_PATH, "w") as file:
        json_specs = json.dumps(spec.to_dict(), indent=2)
        file.write(json_specs)


if __name__ == '__main__':
    main()
