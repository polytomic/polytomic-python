# This file was auto-generated from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError as core_api_error_ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ...errors.not_found_error import NotFoundError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.api_error import ApiError as types_api_error_ApiError
from ...types.bulk_sync_execution_envelope import BulkSyncExecutionEnvelope
from ...types.list_bulk_sync_executions_envelope import ListBulkSyncExecutionsEnvelope
from ...types.rest_err_response import RestErrResponse


class ExecutionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListBulkSyncExecutionsEnvelope:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListBulkSyncExecutionsEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            token="YOUR_TOKEN",
        )
        client.bulk_sync.executions.list_(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/executions", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ListBulkSyncExecutionsEnvelope, _response.json())  # type: ignore
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

    def get(
        self, id: str, exec_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkSyncExecutionEnvelope:
        """
        Parameters
        ----------
        id : str

        exec_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSyncExecutionEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            token="YOUR_TOKEN",
        )
        client.bulk_sync.executions.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            exec_id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/executions/{jsonable_encoder(exec_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncExecutionEnvelope, _response.json())  # type: ignore
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


class AsyncExecutionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListBulkSyncExecutionsEnvelope:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListBulkSyncExecutionsEnvelope
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            token="YOUR_TOKEN",
        )
        await client.bulk_sync.executions.list_(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/executions", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ListBulkSyncExecutionsEnvelope, _response.json())  # type: ignore
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

    async def get(
        self, id: str, exec_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkSyncExecutionEnvelope:
        """
        Parameters
        ----------
        id : str

        exec_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSyncExecutionEnvelope
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            token="YOUR_TOKEN",
        )
        await client.bulk_sync.executions.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            exec_id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/executions/{jsonable_encoder(exec_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncExecutionEnvelope, _response.json())  # type: ignore
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
