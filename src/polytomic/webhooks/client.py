# This file was auto-generated from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError as core_api_error_ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.rest_err_response import RestErrResponse
from ..types.webhook_envelope import WebhookEnvelope
from ..types.webhook_list_envelope import WebhookListEnvelope

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class WebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> WebhookListEnvelope:
        """
        Webooks can be set up using the webhook API endpoints. Currently, only one
        webhook may be created per organization. The webhook will be called for events
        in that organization.

        Consult the [Events documentation](https://apidocs.polytomic.com/getting-started/events) for more information.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookListEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.webhooks.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/webhooks", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(WebhookListEnvelope, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        endpoint: str,
        secret: str,
        organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookEnvelope:
        """
        Webooks can be set up using the webhook API endpoints. Currently, only one
        webhook may be created per organization. The webhook will be called for events
        in that organization.

        Consult the [Events documentation](https://apidocs.polytomic.com/getting-started/events) for more information.

        Parameters
        ----------
        endpoint : str

        secret : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.webhooks.create(
            endpoint="https://example.com/webhook",
            secret="secret",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/webhooks",
            method="POST",
            json={"endpoint": endpoint, "organization_id": organization_id, "secret": secret},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(WebhookEnvelope, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> WebhookEnvelope:
        """
        Webooks can be set up using the webhook API endpoints. Currently, only one
        webhook may be created per organization. The webhook will be called for events
        in that organization.

        Consult the [Events documentation](https://apidocs.polytomic.com/getting-started/events) for more information.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.webhooks.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/webhooks/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(WebhookEnvelope, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        id: str,
        *,
        endpoint: str,
        secret: str,
        organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookEnvelope:
        """
        Webooks can be set up using the webhook API endpoints. Currently, only one
        webhook may be created per organization. The webhook will be called for events
        in that organization.

        Consult the [Events documentation](https://apidocs.polytomic.com/getting-started/events) for more information.

        Parameters
        ----------
        id : str

        endpoint : str

        secret : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.webhooks.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            endpoint="https://example.com/webhook",
            secret="secret",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/webhooks/{jsonable_encoder(id)}",
            method="PUT",
            json={"endpoint": endpoint, "organization_id": organization_id, "secret": secret},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(WebhookEnvelope, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def remove(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.webhooks.remove(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/webhooks/{jsonable_encoder(id)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)


class AsyncWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> WebhookListEnvelope:
        """
        Webooks can be set up using the webhook API endpoints. Currently, only one
        webhook may be created per organization. The webhook will be called for events
        in that organization.

        Consult the [Events documentation](https://apidocs.polytomic.com/getting-started/events) for more information.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookListEnvelope
            OK

        Examples
        --------
        import asyncio

        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/webhooks", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(WebhookListEnvelope, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        endpoint: str,
        secret: str,
        organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookEnvelope:
        """
        Webooks can be set up using the webhook API endpoints. Currently, only one
        webhook may be created per organization. The webhook will be called for events
        in that organization.

        Consult the [Events documentation](https://apidocs.polytomic.com/getting-started/events) for more information.

        Parameters
        ----------
        endpoint : str

        secret : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookEnvelope
            OK

        Examples
        --------
        import asyncio

        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.create(
                endpoint="https://example.com/webhook",
                secret="secret",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/webhooks",
            method="POST",
            json={"endpoint": endpoint, "organization_id": organization_id, "secret": secret},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(WebhookEnvelope, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> WebhookEnvelope:
        """
        Webooks can be set up using the webhook API endpoints. Currently, only one
        webhook may be created per organization. The webhook will be called for events
        in that organization.

        Consult the [Events documentation](https://apidocs.polytomic.com/getting-started/events) for more information.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookEnvelope
            OK

        Examples
        --------
        import asyncio

        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.get(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/webhooks/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(WebhookEnvelope, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        id: str,
        *,
        endpoint: str,
        secret: str,
        organization_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookEnvelope:
        """
        Webooks can be set up using the webhook API endpoints. Currently, only one
        webhook may be created per organization. The webhook will be called for events
        in that organization.

        Consult the [Events documentation](https://apidocs.polytomic.com/getting-started/events) for more information.

        Parameters
        ----------
        id : str

        endpoint : str

        secret : str

        organization_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookEnvelope
            OK

        Examples
        --------
        import asyncio

        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.update(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
                endpoint="https://example.com/webhook",
                secret="secret",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/webhooks/{jsonable_encoder(id)}",
            method="PUT",
            json={"endpoint": endpoint, "organization_id": organization_id, "secret": secret},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(WebhookEnvelope, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def remove(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhooks.remove(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/webhooks/{jsonable_encoder(id)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)
