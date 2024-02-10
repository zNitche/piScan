import subprocess
import uuid
import os
import sys


def check_device_availability(device_id):
    output = subprocess.check_output("scanimage --list-devices".split()).decode("utf-8")

    return False if device_id not in output else True


def perform_scan(device_id, file_path, extension, resolution):
    file_uuid = uuid.uuid4().hex
    file_path = os.path.join(file_path, file_uuid)

    cmd = f"scanimage -d {device_id} --progress --resolution {resolution} --format {extension} > {file_path}"

    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                               universal_newlines=True)

    for row in process.stdout:
       print(row, file=sys.stdout)

    return file_uuid if os.path.exists(file_path) else None
