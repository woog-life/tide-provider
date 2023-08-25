import json
from typing import Self, TypedDict

from httpx import Client


class TidalDataExtremum(TypedDict):
    isHighTide: bool
    time: str
    height: str


class ApiClient:
    def __init__(self, token: str):
        self._client = Client(
            headers={"Authorization": f"Bearer {token}"},
            timeout=240,
        )

    def push_tidal_data(self, lake_id: str, data: list[TidalDataExtremum]) -> None:
        response = self._client.put(
            f"https://api.woog.life/lake/{lake_id}/tides",
            json={
                "extrema": data,
            },
        )
        if not response.is_success:
            if response.content:
                error_message: str
                try:
                    error_message = response.json()["errorMessage"]
                except ValueError:
                    error_message = response.text
                except KeyError:
                    error_message = json.dumps(response.json())

                raise ConnectionError(
                    f"Got error response ({response.status_code}): {error_message}"
                )
            else:
                raise ConnectionError(f"Got response code {response.status_code}")

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.close()

    def close(self) -> None:
        self._client.close()
