from main import app


def test_health_returns_ok():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_add_returns_sum():
    client = app.test_client()
    response = client.get("/add/7/5")

    assert response.status_code == 200
    assert response.get_json() == {"a": 7, "b": 5, "result": 12}


def test_add_rejects_non_integer_values():
    client = app.test_client()
    response = client.get("/add/a/5")

    assert response.status_code == 404
