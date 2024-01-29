class ProcessesManager:
    def __init__(self):
        self.cache_client = None

    def setup(self, cache_client):
        self.cache_client = cache_client
