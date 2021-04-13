import pytest
from django.urls import reverse


@pytest.mark.django_db
class AdsTest:

    def test_not_logged(self, client):
        response = client.post(
            reverse("api:ads"), data={"title": "test", "text": "test"}
        )
        assert response.status_code == 200
        assert response.json()["status"] == 403

    def test_logged_in(self, client, create_and_login_user):
        response = client.post(
            reverse("api:ads"), data={"title": "test", "text": "test"}
        )
        assert response.status_code == 200
        assert response.json()["status"] == 403
