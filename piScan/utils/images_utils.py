from PIL import Image
import os
from piScan.utils import files_utils
from config import Config


def get_file_details(file_uuid):
    width, height, size = 0, 0, 0
    file_path = files_utils.get_path_to_file(file_uuid)

    if os.path.exists(file_path):
        size = os.path.getsize(file_path)

        with Image.open(file_path) as img:
            width, height = img.size

    return width, height, size


def create_thumbnail(file_uuid, extension, size=(250, 250)):
    file_path = files_utils.get_path_to_file(file_uuid)

    if os.path.exists(file_path):
        output_path = os.path.join(Config.SCAN_FILES_THUMBNAILS_DIR_PATH, file_uuid)

        with Image.open(file_path) as img:
            img.thumbnail(size)
            img.save(output_path, extension)
