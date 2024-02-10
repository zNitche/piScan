import subprocess


def check_device_availability(device_id):
    output = subprocess.check_output("scanimage --list-devices".split()).decode("utf-8")

    return False if device_id not in output else True
