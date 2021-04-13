import pytest
from django.urls import reverse


@pytest.fixture
def create_and_login_user(client):
    client.post(
        reverse("api:register"),
        data={"identifier": "test", "password": "password"},
    )

    client.post(
        reverse("api:login"),
        data={"identifier": "test", "password": "password"},
    )
