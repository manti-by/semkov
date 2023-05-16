import pytest


@pytest.mark.django_db
class HomeViewsTest:
    def test_index(self, client):
        response = client.get("/")
        assert response.status_code == 200
