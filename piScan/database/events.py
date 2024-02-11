from sqlalchemy import event
from configs.config import Config
from piScan import models
from piScan.utils import files_utils


@event.listens_for(models.ScanFile, "after_delete")
def receive_after_scan_file_delete(mapper, connection, target):
    files_path = Config.SCAN_FILES_DIR_PATH

    if files_path:
        files_utils.remove_scan_file(files_path, target.uuid)
