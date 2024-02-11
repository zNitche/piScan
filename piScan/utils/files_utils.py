import os


def remove_scan_file(files_path, file_uuid):
    file_path = os.path.join(files_path, file_uuid)

    if os.path.exists(file_path):
        os.remove(file_path)
