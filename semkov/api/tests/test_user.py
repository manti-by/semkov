import pytest
from django.urls import reverse


@pytest.mark.django_db
class UserTest:

    def test_user(self, client):
        response = client.post(
            reverse("api:register"),
            data={"identifier": "test", "password": "password"},
        )
        assert response.status_code == 200
        assert response.json()["status"] == 200

        response = client.post(
            reverse("api:login"),
            data={"identifier": "test", "password": "password"},
        )
        assert response.status_code == 200
        assert response.json()["status"] == 200

        response = client.get(reverse("api:logout"))
        assert response.status_code == 200
        assert response.json()["status"] == 200
