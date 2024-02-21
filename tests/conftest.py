import pytest
from piScan import create_app


@pytest.fixture(scope="session")
def test_client():
    flask_app = create_app()
    flask_app.testing = True

    client = flask_app.test_client()

    with flask_app.test_request_context():
        yield client
