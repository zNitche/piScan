class DevicesProcessesManager:
    def __init__(self):
        self.cache_client = None

    def setup(self, cache_client):
        self.cache_client = cache_client

    def set_device_availability_state(self, device_id, is_available):
        self.cache_client.set_value(device_id, {"is_available": is_available})

    def get_device_availability_state(self, device_id):
        data = self.cache_client.get_value(device_id)
        is_available = False if (data and not data.get("is_available")) else True

        return is_available

    def set_scan_progress_for_device(self, device_id, progress):
        current_device_data = self.cache_client.get_value(device_id)
        current_device_data["progress"] = progress

        self.cache_client.set_value(device_id, current_device_data)

    def get_scan_progress_for_device(self, device_id):
        current_device_data = self.cache_client.get_value(device_id)

        is_running = True if (current_device_data and not current_device_data.get("is_available")) else False
        progress = current_device_data.get("progress") if is_running else 0
        progress = progress if progress is not None else 0

        return progress, is_running
