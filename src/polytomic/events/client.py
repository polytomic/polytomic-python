# This file was auto-generated from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError as core_api_error_ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.event_types_envelope import EventTypesEnvelope
from ..types.events_envelope import EventsEnvelope
from ..types.rest_err_response import RestErrResponse


class EventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        starting_after: typing.Optional[dt.datetime] = None,
        ending_before: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> EventsEnvelope:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        type : typing.Optional[str]

        starting_after : typing.Optional[dt.datetime]

        ending_before : typing.Optional[dt.datetime]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventsEnvelope
            OK

        Examples
        --------
        import datetime

        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.events.list(
            organization_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            starting_after=datetime.datetime.fromisoformat(
                "2020-01-01 00:00:00+00:00",
            ),
            ending_before=datetime.datetime.fromisoformat(
                "2020-01-01 00:00:00+00:00",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/events",
            method="GET",
            params={
                "organization_id": organization_id,
                "type": type,
                "starting_after": serialize_datetime(starting_after) if starting_after is not None else None,
                "ending_before": serialize_datetime(ending_before) if ending_before is not None else None,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(EventsEnvelope, _response.json())  # type: ignore
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

    def get_types(self, *, request_options: typing.Optional[RequestOptions] = None) -> EventTypesEnvelope:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventTypesEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.events.get_types()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/events_types", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(EventTypesEnvelope, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)


class AsyncEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        organization_id: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        starting_after: typing.Optional[dt.datetime] = None,
        ending_before: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> EventsEnvelope:
        """
        Parameters
        ----------
        organization_id : typing.Optional[str]

        type : typing.Optional[str]

        starting_after : typing.Optional[dt.datetime]

        ending_before : typing.Optional[dt.datetime]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventsEnvelope
            OK

        Examples
        --------
        import asyncio
        import datetime

        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.events.list(
                organization_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                starting_after=datetime.datetime.fromisoformat(
                    "2020-01-01 00:00:00+00:00",
                ),
                ending_before=datetime.datetime.fromisoformat(
                    "2020-01-01 00:00:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/events",
            method="GET",
            params={
                "organization_id": organization_id,
                "type": type,
                "starting_after": serialize_datetime(starting_after) if starting_after is not None else None,
                "ending_before": serialize_datetime(ending_before) if ending_before is not None else None,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(EventsEnvelope, _response.json())  # type: ignore
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

    async def get_types(self, *, request_options: typing.Optional[RequestOptions] = None) -> EventTypesEnvelope:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EventTypesEnvelope
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
            await client.events.get_types()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/events_types", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(EventTypesEnvelope, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)
