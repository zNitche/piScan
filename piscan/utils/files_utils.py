import os
from config import Config


def get_path_to_file(file_uuid):
    return os.path.join(Config.SCAN_FILES_DIR_PATH, file_uuid)


def get_path_to_thumbnail(file_uuid):
    return os.path.join(Config.SCAN_FILES_THUMBNAILS_DIR_PATH, file_uuid)


def remove_scan_file(file_uuid):
    file_path = get_path_to_file(file_uuid)
    thumbnail_path = get_path_to_thumbnail(file_uuid)

    if os.path.exists(file_path):
        os.remove(file_path)

    if os.path.exists(thumbnail_path):
        os.remove(thumbnail_path)
