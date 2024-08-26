# This file was auto-generated from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError as core_api_error_ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ...errors.bad_request_error import BadRequestError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.api_error import ApiError as types_api_error_ApiError
from ...types.bulk_sync_execution_envelope import BulkSyncExecutionEnvelope
from ...types.list_bulk_sync_execution_status_envelope import ListBulkSyncExecutionStatusEnvelope
from ...types.list_bulk_sync_executions_envelope import ListBulkSyncExecutionsEnvelope
from ...types.rest_err_response import RestErrResponse
from ...types.v_4_bulk_sync_execution_logs_envelope import V4BulkSyncExecutionLogsEnvelope
from ...types.v_4_export_sync_logs_envelope import V4ExportSyncLogsEnvelope


class ExecutionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_status(
        self,
        *,
        all_: typing.Optional[bool] = None,
        active: typing.Optional[bool] = None,
        sync_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListBulkSyncExecutionStatusEnvelope:
        """
        Parameters
        ----------
        all_ : typing.Optional[bool]
            Return the execution status of all syncs in the organization

        active : typing.Optional[bool]
            Return the execution status of all active syncs in the organization

        sync_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Return the execution status of the specified sync; this may be supplied multiple times.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListBulkSyncExecutionStatusEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.executions.list_status(
            all_=True,
            active=True,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/bulk/syncs/status",
            method="GET",
            params={"all": all_, "active": active, "sync_id": sync_id},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ListBulkSyncExecutionStatusEnvelope, _response.json())  # type: ignore
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

    def list(
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
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.executions.list(
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
            version="YOUR_VERSION",
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

    def get_logs(
        self, sync_id: str, execution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V4BulkSyncExecutionLogsEnvelope:
        """
        Parameters
        ----------
        sync_id : str

        execution_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V4BulkSyncExecutionLogsEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.executions.get_logs(
            sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            execution_id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(sync_id)}/executions/{jsonable_encoder(execution_id)}/logs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(V4BulkSyncExecutionLogsEnvelope, _response.json())  # type: ignore
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

    def export_logs(
        self,
        sync_id: str,
        execution_id: str,
        *,
        notify: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V4ExportSyncLogsEnvelope:
        """
        Parameters
        ----------
        sync_id : str

        execution_id : str

        notify : typing.Optional[bool]
            Send a notification to the user when the logs are ready for download.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V4ExportSyncLogsEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.executions.export_logs(
            sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            execution_id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(sync_id)}/executions/{jsonable_encoder(execution_id)}/logs/export",
            method="POST",
            params={"notify": notify},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(V4ExportSyncLogsEnvelope, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
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


class AsyncExecutionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_status(
        self,
        *,
        all_: typing.Optional[bool] = None,
        active: typing.Optional[bool] = None,
        sync_id: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListBulkSyncExecutionStatusEnvelope:
        """
        Parameters
        ----------
        all_ : typing.Optional[bool]
            Return the execution status of all syncs in the organization

        active : typing.Optional[bool]
            Return the execution status of all active syncs in the organization

        sync_id : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Return the execution status of the specified sync; this may be supplied multiple times.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListBulkSyncExecutionStatusEnvelope
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
            await client.bulk_sync.executions.list_status(
                all_=True,
                active=True,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/bulk/syncs/status",
            method="GET",
            params={"all": all_, "active": active, "sync_id": sync_id},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ListBulkSyncExecutionStatusEnvelope, _response.json())  # type: ignore
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

    async def list(
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
        import asyncio

        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bulk_sync.executions.list(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
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
        import asyncio

        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bulk_sync.executions.get(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
                exec_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
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

    async def get_logs(
        self, sync_id: str, execution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V4BulkSyncExecutionLogsEnvelope:
        """
        Parameters
        ----------
        sync_id : str

        execution_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V4BulkSyncExecutionLogsEnvelope
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
            await client.bulk_sync.executions.get_logs(
                sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                execution_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(sync_id)}/executions/{jsonable_encoder(execution_id)}/logs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(V4BulkSyncExecutionLogsEnvelope, _response.json())  # type: ignore
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

    async def export_logs(
        self,
        sync_id: str,
        execution_id: str,
        *,
        notify: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V4ExportSyncLogsEnvelope:
        """
        Parameters
        ----------
        sync_id : str

        execution_id : str

        notify : typing.Optional[bool]
            Send a notification to the user when the logs are ready for download.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V4ExportSyncLogsEnvelope
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
            await client.bulk_sync.executions.export_logs(
                sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                execution_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(sync_id)}/executions/{jsonable_encoder(execution_id)}/logs/export",
            method="POST",
            params={"notify": notify},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(V4ExportSyncLogsEnvelope, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
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
