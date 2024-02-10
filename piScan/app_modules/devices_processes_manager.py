class DevicesProcessesManager:
    def __init__(self):
        self.cache_client = None

    def setup(self, cache_client):
        self.cache_client = cache_client

    def set_device_availability_state(self, device_id, is_busy):
        self.cache_client.set_value(device_id, {"is_busy": is_busy})

    def get_device_availability_state(self, device_id):
        data = self.cache_client.get_value(device_id)

        return True if (data and data.get("is_busy") is False) else False
