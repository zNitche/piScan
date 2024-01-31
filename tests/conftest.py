import pytest
from piScan import create_app
from configs.test_config import TestConfig


@pytest.fixture(scope="session")
def test_client():
    flask_app = create_app(TestConfig)
    client = flask_app.test_client()

    with flask_app.test_request_context():
        yield client
