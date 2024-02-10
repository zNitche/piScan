import subprocess
import uuid
import os
import sys


def parse_device_options(options_output):
    options = []

    current_section = ""
    current_parameters = []
    current_parameter = {
        "name": "",
        "description": ""
    }

    for index, row in enumerate(options_output):
        current_row = row.strip()

        if 1 < index < len(options_output) - 1:
            if current_row.endswith(":"):
                section = current_row.replace(":", "")

                if section != current_section:
                    if current_section:
                        current_parameter_name = current_parameter.get("name")

                        if current_parameter_name:
                            parameter_prefix = "--" if current_row.startswith("--") else "-"
                            current_parameter["name"] = f"{parameter_prefix}{current_parameter_name}"

                            current_parameters.append(current_parameter.copy())

                        options.append({"name": current_section, "parameters": current_parameters})

                        current_parameter = {}
                        current_parameters = []

                    current_section = section

            elif current_row.startswith("-"):
                parameter_name = current_row.replace("-", "")
                current_parameter_name = current_parameter.get("name")

                if parameter_name != current_parameter_name:
                    if current_parameter_name:
                        parameter_prefix = "--" if current_row.startswith("--") else "-"
                        current_parameter["name"] = f"{parameter_prefix}{current_parameter_name}"

                        current_parameters.append(current_parameter.copy())

                    current_parameter["name"] = parameter_name
                    current_parameter["description"] = ""

            else:
                if current_parameter.get("name"):
                    current_parameter["description"] += f"{current_row}\n"

        elif index == len(options_output) - 1:
            options.append({"name": current_section, "parameters": current_parameters})

    parsed_output = {
        "header": options_output[1],
        "options": options
    }

    return parsed_output


def check_device_availability(device_id):
    try:
        subprocess.check_output(f"scanimage -d {device_id} -A".split()).decode("utf-8")

        return True
    except subprocess.CalledProcessError:
        return False


def get_device_options(device_id):
    try:
        output = subprocess.check_output(f"scanimage -d {device_id} -A".split()).decode("utf-8")

        return parse_device_options(output.split("\n"))
    except subprocess.CalledProcessError:
        return None


def perform_scan(device_id, file_path, extension, resolution):
    file_uuid = uuid.uuid4().hex
    file_path = os.path.join(file_path, file_uuid)

    cmd = f"scanimage -d {device_id} --progress --resolution {resolution} --format {extension} > {file_path}"

    try:
        process = subprocess.Popen(cmd,
                                   shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   universal_newlines=True)

        for row in process.stdout:
           print(row, file=sys.stdout)

    except subprocess.CalledProcessError:
        pass

    return file_uuid if os.path.exists(file_path) else None
