import pytest

from core.models import BaseTest


@pytest.mark.django_db
class HomeViewsTest(BaseTest):
    def test_index(self, client):
        response = client.get("/", HTTP_HOST=self.host)
        assert response.status_code == 200
