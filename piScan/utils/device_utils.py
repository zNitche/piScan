import subprocess
import uuid
import os
import shutil
import re
import tempfile
from config import Config


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


def perform_scan(device_id, extension, resolution, update_progress_callback=None):
    tmp_file_prefix = "piscan_file_"
    file_uuid = uuid.uuid4().hex
    file_tmp_path = os.path.join(tempfile.gettempdir(), f"{tmp_file_prefix}{file_uuid}")
    file_target_path = os.path.join(Config.SCAN_FILES_DIR_PATH, file_uuid)

    cmd = f"scanimage -d {device_id} --progress --resolution {resolution} --format {extension} > {file_tmp_path}"

    try:
        process = subprocess.Popen(cmd,
                                   shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   universal_newlines=True)

        regex = re.compile("Progress:(.*?)%")

        for row in process.stdout:
            if update_progress_callback:
                result = regex.search(row)

                progress_result = result.group(1) if result and result.group(1) else None

                if progress_result:
                    progress = int(float(progress_result.strip()))
                    update_progress_callback(device_id, progress)

        if os.path.exists(file_tmp_path):
            shutil.copy2(file_tmp_path, file_target_path)

    except subprocess.CalledProcessError:
        pass

    return file_uuid if os.path.exists(file_target_path) else None


def parse_connected_devices(raw_data):
    data = []

    for row in raw_data:
        regex = re.compile("`(.*?)\'.*((?<=is a ).*$)")
        result = regex.search(row)

        if result:
            device_id = result.group(1)
            name = result.group(2)

            data.append({
                "name": name,
                "device_id": device_id
            })

    return data


def get_connected_devices():
    try:
        output = subprocess.check_output(f"scanimage --list-devices".split()).decode("utf-8")

        return parse_connected_devices(output.split("\n"))
    except subprocess.CalledProcessError:
        return []
