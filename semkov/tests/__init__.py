from typing import Any
from unittest.mock import MagicMock


class MockedResponse(MagicMock):
    def __init__(
        self,
        data: dict | list | str | bytes | object,
        status_code: int | None = 200,
        reason: str | None = "OK",
        *args: Any,
        **kw: Any,
    ):
        """Attach data, status_code and reason to the response object."""
        super().__init__(*args, **kw)
        self.data = data
        self.status_code = status_code
        self.reason = reason

    @property
    def ok(self) -> bool:
        return self.status_code == 200

    @property
    def headers(self) -> dict:
        return {"content-type": "application/json"}

    @property
    def content(self) -> dict | list | str:
        return self.data

    def json(self):
        return self.data
