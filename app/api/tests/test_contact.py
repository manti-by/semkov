import pytest

from core.models import BaseTest


@pytest.mark.django_db
class ContactTest(BaseTest):
    def test_contact(self, client):
        response = client.post(
            "/api/contact",
            data={"name": "test", "contact": "test", "message": "test"},
            HTTP_HOST=self.host,
        )
        assert response.status_code == 200
        assert response.json()["status"] == 200
