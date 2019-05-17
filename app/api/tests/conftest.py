import pytest


@pytest.fixture
def default_host():
    return "127.0.0.1:8000"


@pytest.fixture
def create_and_login_user(default_host, client):
    client.post(
        "/api/register",
        data={"identifier": "test", "password": "password"},
        HTTP_HOST=default_host,
    )

    client.post(
        "/api/login",
        data={"identifier": "test", "password": "password"},
        HTTP_HOST=default_host,
    )
