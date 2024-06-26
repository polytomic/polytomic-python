# This file was auto-generated from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError as core_api_error_ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ...errors.forbidden_error import ForbiddenError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.api_error import ApiError as types_api_error_ApiError
from ...types.bulk_field import BulkField
from ...types.bulk_filter import BulkFilter
from ...types.bulk_schema import BulkSchema
from ...types.bulk_schema_envelope import BulkSchemaEnvelope
from ...types.list_bulk_schema import ListBulkSchema
from ...types.rest_err_response import RestErrResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SchemasClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_(
        self,
        id: str,
        *,
        filters: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListBulkSchema:
        """
        Parameters
        ----------
        id : str

        filters : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListBulkSchema
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            token="YOUR_TOKEN",
        )
        client.bulk_sync.schemas.list_(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/schemas",
            method="GET",
            params={"filters": jsonable_encoder(filters)},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ListBulkSchema, _response.json())  # type: ignore
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

    def patch(
        self,
        id: str,
        *,
        schemas: typing.Optional[typing.Sequence[BulkSchema]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListBulkSchema:
        """
        Parameters
        ----------
        id : str

        schemas : typing.Optional[typing.Sequence[BulkSchema]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListBulkSchema
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            token="YOUR_TOKEN",
        )
        client.bulk_sync.schemas.patch(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/schemas",
            method="PATCH",
            json={"schemas": schemas},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ListBulkSchema, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 403:
                raise ForbiddenError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
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

    def get(
        self, id: str, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkSchemaEnvelope:
        """
        Parameters
        ----------
        id : str

        schema_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSchemaEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            token="YOUR_TOKEN",
        )
        client.bulk_sync.schemas.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            schema_id="Contact",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/schemas/{jsonable_encoder(schema_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSchemaEnvelope, _response.json())  # type: ignore
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
        schema_id: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[BulkField]] = OMIT,
        filters: typing.Optional[typing.Sequence[BulkFilter]] = OMIT,
        partition_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSchemaEnvelope:
        """
        Parameters
        ----------
        id : str

        schema_id : str

        enabled : typing.Optional[bool]

        fields : typing.Optional[typing.Sequence[BulkField]]

        filters : typing.Optional[typing.Sequence[BulkFilter]]

        partition_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSchemaEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            token="YOUR_TOKEN",
        )
        client.bulk_sync.schemas.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            schema_id="contact",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/schemas/{jsonable_encoder(schema_id)}",
            method="PUT",
            json={"enabled": enabled, "fields": fields, "filters": filters, "partition_key": partition_key},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSchemaEnvelope, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 403:
                raise ForbiddenError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
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


class AsyncSchemasClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_(
        self,
        id: str,
        *,
        filters: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListBulkSchema:
        """
        Parameters
        ----------
        id : str

        filters : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListBulkSchema
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            token="YOUR_TOKEN",
        )
        await client.bulk_sync.schemas.list_(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/schemas",
            method="GET",
            params={"filters": jsonable_encoder(filters)},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ListBulkSchema, _response.json())  # type: ignore
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

    async def patch(
        self,
        id: str,
        *,
        schemas: typing.Optional[typing.Sequence[BulkSchema]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListBulkSchema:
        """
        Parameters
        ----------
        id : str

        schemas : typing.Optional[typing.Sequence[BulkSchema]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListBulkSchema
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            token="YOUR_TOKEN",
        )
        await client.bulk_sync.schemas.patch(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/schemas",
            method="PATCH",
            json={"schemas": schemas},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ListBulkSchema, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 403:
                raise ForbiddenError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
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

    async def get(
        self, id: str, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkSchemaEnvelope:
        """
        Parameters
        ----------
        id : str

        schema_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSchemaEnvelope
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            token="YOUR_TOKEN",
        )
        await client.bulk_sync.schemas.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            schema_id="Contact",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/schemas/{jsonable_encoder(schema_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSchemaEnvelope, _response.json())  # type: ignore
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
        schema_id: str,
        *,
        enabled: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[BulkField]] = OMIT,
        filters: typing.Optional[typing.Sequence[BulkFilter]] = OMIT,
        partition_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSchemaEnvelope:
        """
        Parameters
        ----------
        id : str

        schema_id : str

        enabled : typing.Optional[bool]

        fields : typing.Optional[typing.Sequence[BulkField]]

        filters : typing.Optional[typing.Sequence[BulkFilter]]

        partition_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSchemaEnvelope
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            token="YOUR_TOKEN",
        )
        await client.bulk_sync.schemas.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            schema_id="contact",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/schemas/{jsonable_encoder(schema_id)}",
            method="PUT",
            json={"enabled": enabled, "fields": fields, "filters": filters, "partition_key": partition_key},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSchemaEnvelope, _response.json())  # type: ignore
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 403:
                raise ForbiddenError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
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
