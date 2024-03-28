from sqlalchemy import event
from piscan import models
from piscan.utils import files_utils


@event.listens_for(models.ScanFile, "after_delete")
def receive_after_scan_file_delete(mapper, connection, target):
    files_utils.remove_scan_file(target.uuid)
