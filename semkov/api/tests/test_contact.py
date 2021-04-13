import pytest
from django.urls import reverse


@pytest.mark.django_db
class ContactTest:

    def test_contact(self, client):
        response = client.post(
            reverse("api:contact"),
            data={"name": "test", "contact": "test", "message": "test"},
        )
        assert response.status_code == 200
        assert response.json()["status"] == 200
