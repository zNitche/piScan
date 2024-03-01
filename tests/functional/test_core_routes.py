from flask import url_for


def test_health_check(test_client):
    response = test_client.get(url_for("core.health_check"), follow_redirects=False)

    assert response.status_code == 200
    assert response.request.path == url_for("core.health_check")
