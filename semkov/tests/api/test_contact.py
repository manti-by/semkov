from unittest import mock

from django.urls import reverse

from semkov.tests import MockedResponse

import pytest


@pytest.mark.django_db
class ContactTest:
    @mock.patch("semkov.apps.core.services.recaptcha.requests")
    def test_contact(self, requests_mock, client):
        requests_mock.post.return_value = MockedResponse({"success": True})
        response = client.post(
            reverse("api:contact"),
            data={"name": "test", "contact": "test", "message": "test"},
        )
        assert response.status_code == 200
        assert response.json()["status"] == 200
