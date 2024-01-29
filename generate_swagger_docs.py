from piScan.api_spec import spec
from marshmallow import schema
from config import Config
import os
import json


def main():
    with open(os.path.join(Config.CURRENT_DIR, "swagger.json"), "w") as file:
        json_specs = json.dumps(spec.to_dict(), indent=2)
        file.write(json_specs)


if __name__ == '__main__':
    main()
