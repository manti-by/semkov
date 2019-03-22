import pytest


@pytest.mark.django_db
class ViewsTest:

    @classmethod
    def setup_class(cls):
        cls.host = "127.0.0.1:8000"

    def test_index(self, client):
        response = client.get('/', HTTP_HOST=self.host)
        assert response.status_code == 200
