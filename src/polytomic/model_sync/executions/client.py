# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper
import typing
from ...core.request_options import RequestOptions
from ...types.list_execution_response_envelope import ListExecutionResponseEnvelope
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import parse_obj_as
from ...errors.unauthorized_error import UnauthorizedError
from ...types.rest_err_response import RestErrResponse
from ...errors.not_found_error import NotFoundError
from ...types.api_error import ApiError as types_api_error_ApiError
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError as core_api_error_ApiError
from ...types.get_execution_response_envelope import GetExecutionResponseEnvelope
from ...errors.internal_server_error import InternalServerError
from ...types.v_2_execution_log_type import V2ExecutionLogType
from ...types.execution_logs_response_envelope import ExecutionLogsResponseEnvelope
from ...errors.bad_request_error import BadRequestError
from ...core.client_wrapper import AsyncClientWrapper


class ExecutionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, sync_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListExecutionResponseEnvelope:
        """
        Parameters
        ----------
        sync_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListExecutionResponseEnvelope
            OK

        Examples
        --------
        from polytomic import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.executions.list(
            sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/syncs/{jsonable_encoder(sync_id)}/executions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ListExecutionResponseEnvelope,
                    parse_obj_as(
                        type_=ListExecutionResponseEnvelope,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        RestErrResponse,
                        parse_obj_as(
                            type_=RestErrResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, sync_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetExecutionResponseEnvelope:
        """
        Parameters
        ----------
        sync_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetExecutionResponseEnvelope
            OK

        Examples
        --------
        from polytomic import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.executions.get(
            sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/syncs/{jsonable_encoder(sync_id)}/executions/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    GetExecutionResponseEnvelope,
                    parse_obj_as(
                        type_=GetExecutionResponseEnvelope,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        RestErrResponse,
                        parse_obj_as(
                            type_=RestErrResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def get_log_urls(
        self,
        sync_id: str,
        id: str,
        type: V2ExecutionLogType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExecutionLogsResponseEnvelope:
        """
        Parameters
        ----------
        sync_id : str

        id : str

        type : V2ExecutionLogType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExecutionLogsResponseEnvelope
            OK

        Examples
        --------
        from polytomic import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.executions.get_log_urls(
            sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            type="records",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/syncs/{jsonable_encoder(sync_id)}/executions/{jsonable_encoder(id)}/{jsonable_encoder(type)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ExecutionLogsResponseEnvelope,
                    parse_obj_as(
                        type_=ExecutionLogsResponseEnvelope,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        RestErrResponse,
                        parse_obj_as(
                            type_=RestErrResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def get_logs(
        self,
        sync_id: str,
        id: str,
        type: V2ExecutionLogType,
        filename: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        sync_id : str

        id : str

        type : V2ExecutionLogType

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from polytomic import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.executions.get_logs(
            sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            id="0ecd09c1-b901-4d27-9053-f0367c427254",
            type="records",
            filename="path/to/file.json",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/syncs/{jsonable_encoder(sync_id)}/executions/{jsonable_encoder(id)}/{jsonable_encoder(type)}/{jsonable_encoder(filename)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        RestErrResponse,
                        parse_obj_as(
                            type_=RestErrResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)


class AsyncExecutionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, sync_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListExecutionResponseEnvelope:
        """
        Parameters
        ----------
        sync_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListExecutionResponseEnvelope
            OK

        Examples
        --------
        import asyncio

        from polytomic import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.model_sync.executions.list(
                sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/syncs/{jsonable_encoder(sync_id)}/executions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ListExecutionResponseEnvelope,
                    parse_obj_as(
                        type_=ListExecutionResponseEnvelope,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        RestErrResponse,
                        parse_obj_as(
                            type_=RestErrResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, sync_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetExecutionResponseEnvelope:
        """
        Parameters
        ----------
        sync_id : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetExecutionResponseEnvelope
            OK

        Examples
        --------
        import asyncio

        from polytomic import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.model_sync.executions.get(
                sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/syncs/{jsonable_encoder(sync_id)}/executions/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    GetExecutionResponseEnvelope,
                    parse_obj_as(
                        type_=GetExecutionResponseEnvelope,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        RestErrResponse,
                        parse_obj_as(
                            type_=RestErrResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def get_log_urls(
        self,
        sync_id: str,
        id: str,
        type: V2ExecutionLogType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExecutionLogsResponseEnvelope:
        """
        Parameters
        ----------
        sync_id : str

        id : str

        type : V2ExecutionLogType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExecutionLogsResponseEnvelope
            OK

        Examples
        --------
        import asyncio

        from polytomic import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.model_sync.executions.get_log_urls(
                sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
                type="records",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/syncs/{jsonable_encoder(sync_id)}/executions/{jsonable_encoder(id)}/{jsonable_encoder(type)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ExecutionLogsResponseEnvelope,
                    parse_obj_as(
                        type_=ExecutionLogsResponseEnvelope,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        RestErrResponse,
                        parse_obj_as(
                            type_=RestErrResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def get_logs(
        self,
        sync_id: str,
        id: str,
        type: V2ExecutionLogType,
        filename: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        sync_id : str

        id : str

        type : V2ExecutionLogType

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from polytomic import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.model_sync.executions.get_logs(
                sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                id="0ecd09c1-b901-4d27-9053-f0367c427254",
                type="records",
                filename="path/to/file.json",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/syncs/{jsonable_encoder(sync_id)}/executions/{jsonable_encoder(id)}/{jsonable_encoder(type)}/{jsonable_encoder(filename)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    typing.cast(
                        RestErrResponse,
                        parse_obj_as(
                            type_=RestErrResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)
