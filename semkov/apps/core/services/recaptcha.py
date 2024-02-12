import logging
import requests
from django.conf import settings

logger = logging.getLogger(__name__)


def is_valid_recaptcha_token(token: str) -> bool:
    try:
        response = requests.post(
            "https://www.google.com/recaptcha/api/siteverify",
            data={
                "secret": settings.GOOGLE_RECAPTCHA_SECRET,
                "response": token,
            },
        )
        return response.json().get("success")
    except Exception as e:
        logger.warning(e)
    return False
