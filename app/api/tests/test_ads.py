import pytest

from core.models import BaseTest


@pytest.mark.django_db
class ContactTest(BaseTest):
    def test_not_logged(self, client):
        response = client.post(
            "/api/ads", data={"title": "test", "text": "test"}, HTTP_HOST=self.host
        )
        assert response.status_code == 200
        assert response.json()["status"] == 403

    def test_logged_in(self, client, create_and_login_user):
        response = client.post(
            "/api/ads", data={"title": "test", "text": "test"}, HTTP_HOST=self.host
        )
        assert response.status_code == 200
        assert response.json()["status"] == 403
