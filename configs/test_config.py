class TestConfig:
    TESTING = True
    DATABASE_URI = "sqlite:///:memory:"

    REDIS_URI = "127.0.0.1"
    REDIS_PORT = "6000"
