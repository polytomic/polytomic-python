# This file was auto-generated from our API Definition.

import typing

import httpx

from .http_client import AsyncHttpClient, HttpClient


class BaseClientWrapper:
    def __init__(
        self,
        *,
        token: typing.Union[str, typing.Callable[[], str]],
        base_url: str,
        timeout: typing.Optional[float] = None,
    ):
        self._token = token
        self._base_url = base_url
        self._timeout = timeout

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {
            "X-Fern-Language": "Python",
            "X-Fern-SDK-Name": "polytomic",
            "X-Fern-SDK-Version": "1.5.0",
        }
        headers["Authorization"] = f"Bearer {self._get_token()}"
        headers["X-Polytomic-Version"] = "2024-02-08"
        return headers

    def _get_token(self) -> str:
        if isinstance(self._token, str):
            return self._token
        else:
            return self._token()

    def get_base_url(self) -> str:
        return self._base_url

    def get_timeout(self) -> typing.Optional[float]:
        return self._timeout


class SyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        token: typing.Union[str, typing.Callable[[], str]],
        base_url: str,
        timeout: typing.Optional[float] = None,
        httpx_client: httpx.Client,
    ):
        super().__init__(token=token, base_url=base_url, timeout=timeout)
        self.httpx_client = HttpClient(httpx_client=httpx_client)


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        token: typing.Union[str, typing.Callable[[], str]],
        base_url: str,
        timeout: typing.Optional[float] = None,
        httpx_client: httpx.AsyncClient,
    ):
        super().__init__(token=token, base_url=base_url, timeout=timeout)
        self.httpx_client = AsyncHttpClient(httpx_client=httpx_client)
