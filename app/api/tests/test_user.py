import pytest

from core.models import BaseTest


@pytest.mark.django_db
class UserTest(BaseTest):
    def test_user(self, client):
        response = client.post(
            "/api/register",
            data={"identifier": "test", "password": "password"},
            HTTP_HOST=self.host,
        )
        assert response.status_code == 200
        assert response.json()["status"] == 200

        response = client.post(
            "/api/login",
            data={"identifier": "test", "password": "password"},
            HTTP_HOST=self.host,
        )
        assert response.status_code == 200
        assert response.json()["status"] == 200

        response = client.get("/api/logout", HTTP_HOST=self.host)
        assert response.status_code == 200
        assert response.json()["status"] == 200
