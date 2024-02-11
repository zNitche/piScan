import os
from PIL import Image


def remove_scan_file(files_path, file_uuid):
    file_path = os.path.join(files_path, file_uuid)

    if os.path.exists(file_path):
        os.remove(file_path)


def get_file_details(files_path, file_uuid):
    width, height, size = 0, 0, 0
    file_path = os.path.join(files_path, file_uuid)

    if os.path.exists(file_path):
        size = os.path.getsize(file_path)

        with Image.open(file_path) as img:
            width, height = img.size

    return width, height, size
