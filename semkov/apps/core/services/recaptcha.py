import logging

from django.conf import settings

import requests
from requests import RequestException


logger = logging.getLogger(__name__)


def is_valid_recaptcha_token(token: str) -> bool:
    try:
        response = requests.post(
            "https://www.google.com/recaptcha/api/siteverify",
            data={
                "secret": settings.GOOGLE_RECAPTCHA_SECRET,
                "response": token,
            },
            timeout=120,
        )
        return response.json().get("success")
    except RequestException as e:
        logger.warning(e)
    return False
