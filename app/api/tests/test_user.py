import pytest


@pytest.mark.django_db
class UserTest:
    @classmethod
    def setup_class(cls):
        cls.host = "127.0.0.1:8000"

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
