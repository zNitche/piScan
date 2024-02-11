import subprocess
import uuid
import os
import re


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

        this_row_section = current_section
        this_row_parameter = current_parameter.copy()
        this_row_parameter_name = this_row_parameter.get("name")

        if 1 < index < len(options_output) - 1:
            if current_row.endswith(":"):
                current_section = current_row.replace(":", "")

            elif current_row.startswith("-"):
                current_parameter["name"] = current_row.replace("-", "")
                current_parameter["description"] = ""

            else:
                if current_parameter.get("name"):
                    current_parameter["description"] += f"{current_row}\n"

            if (this_row_parameter_name != current_parameter.get("name")) or (this_row_section != current_section):
                if this_row_parameter_name:
                    parameter_prefix = "--" if current_row.startswith("--") else "-"
                    this_row_parameter["name"] = f"{parameter_prefix}{this_row_parameter_name}"

                    current_parameters.append(this_row_parameter.copy())

            if this_row_section and this_row_section != current_section:
                options.append({"name": this_row_section, "parameters": current_parameters})

                current_parameter = {}
                current_parameters = []

        elif index == len(options_output) - 1:
            if this_row_parameter_name:
                parameter_prefix = "--" if current_row.startswith("--") else "-"
                this_row_parameter["name"] = f"{parameter_prefix}{this_row_parameter_name}"

                current_parameters.append(this_row_parameter.copy())

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


def perform_scan(device_id, file_path, extension, resolution, update_progress_callback=None):
    file_uuid = uuid.uuid4().hex
    file_path = os.path.join(file_path, file_uuid)

    cmd = f"scanimage -d {device_id} --progress --resolution {resolution} --format {extension} > {file_path}"

    try:
        process = subprocess.Popen(cmd,
                                   shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   universal_newlines=True)

        for row in process.stdout:
            if update_progress_callback:
                if "Progress:" in row:
                    regex = re.compile("Progress:(.*?)%")
                    result = regex.search(row)

                    progress = float(result.group(1).strip())
                    update_progress_callback(device_id, progress)

    except subprocess.CalledProcessError:
        pass

    return file_uuid if os.path.exists(file_path) else None
