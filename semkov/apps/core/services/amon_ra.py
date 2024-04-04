from django.conf import settings

from ..library.amon_ra import AmonRaClient

client = AmonRaClient(
    app_key=settings.AMON_RA_APP_KEY, hash_key=settings.AMON_RA_HASH_KEY, base_url=settings.AMON_RA_BASE_URL
)


def send_message(title: str, text: str) -> bool:
    return client.send_message(title, text)
