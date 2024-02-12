import os
from PIL import Image
from configs.config import Config


def get_path_to_file(file_uuid):
    return os.path.join(Config.SCAN_FILES_DIR_PATH, file_uuid)


def remove_scan_file(file_uuid):
    file_path = get_path_to_file(file_uuid)

    if os.path.exists(file_path):
        os.remove(file_path)


def get_file_details(file_uuid):
    width, height, size = 0, 0, 0
    file_path = get_path_to_file(file_uuid)

    if os.path.exists(file_path):
        size = os.path.getsize(file_path)

        with Image.open(file_path) as img:
            width, height = img.size

    return width, height, size
