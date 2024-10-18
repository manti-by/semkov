import hashlib
import hmac
import logging

import requests


logger = logging.getLogger(__name__)


class AmonRaClient:
    def __init__(self, app_key: str, hash_key: str, base_url: str | None = None, timeout: int = 60):
        """Amon-Ra server client."""
        self.app_key = app_key
        self.hash_key = hash_key
        self.base_url = base_url
        self.timeout = timeout

    @staticmethod
    def get_data_hash(data: dict, secret_key: str) -> str:
        data_string = "\n".join([f"{k}={v}" for k, v in sorted(list(data.items()))]).encode()
        secret = hashlib.sha512(secret_key.encode()).digest()
        signature = hmac.new(key=secret, msg=data_string, digestmod=hashlib.sha512)
        return signature.hexdigest()

    def send_data(self, resource: str, data: dict) -> tuple[requests.Response | requests.RequestException, bool]:
        data["key"] = self.app_key
        data["hash"] = self.get_data_hash(data, self.hash_key)
        try:
            response = requests.post(f"{self.base_url}{resource}", json=data, timeout=self.timeout)
            return response, True
        except requests.RequestException as e:
            logger.error(e)
            return e, False

    def send_message(self, title: str, text: str) -> bool:
        _, success = self.send_data(resource="/api/v1/subscription/notification/", data={"title": title, "text": text})
        return success
