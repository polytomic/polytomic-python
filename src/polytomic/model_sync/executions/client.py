# This file was auto-generated from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError as core_api_error_ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ...errors.bad_request_error import BadRequestError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.api_error import ApiError as types_api_error_ApiError
from ...types.execution_logs_response_envelope import ExecutionLogsResponseEnvelope
from ...types.get_execution_response_envelope import GetExecutionResponseEnvelope
from ...types.list_execution_response_envelope import ListExecutionResponseEnvelope
from ...types.rest_err_response import RestErrResponse


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
        from polytomic.client import Polytomic

        client = Polytomic(
            token="YOUR_TOKEN",
        )
        client.model_sync.executions.list(
            sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(sync_id)}/executions"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ListExecutionResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        try:
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
        from polytomic.client import Polytomic

        client = Polytomic(
            token="YOUR_TOKEN",
        )
        client.model_sync.executions.get(
            sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/syncs/{jsonable_encoder(sync_id)}/executions/{jsonable_encoder(id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(GetExecutionResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def get_log_urls(
        self, sync_id: str, id: str, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExecutionLogsResponseEnvelope:
        """
        Parameters
        ----------
        sync_id : str

        id : str

        type : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExecutionLogsResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            token="YOUR_TOKEN",
        )
        client.model_sync.executions.get_log_urls(
            sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            type="records",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/syncs/{jsonable_encoder(sync_id)}/executions/{jsonable_encoder(id)}/{jsonable_encoder(type)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ExecutionLogsResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def get_logs(
        self,
        sync_id: str,
        id: str,
        type: str,
        filename: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        sync_id : str

        id : str

        type : str

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            token="YOUR_TOKEN",
        )
        client.model_sync.executions.get_logs(
            sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            type="records",
            filename="path/to/file.json",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/syncs/{jsonable_encoder(sync_id)}/executions/{jsonable_encoder(id)}/{jsonable_encoder(type)}/{jsonable_encoder(filename)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
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
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            token="YOUR_TOKEN",
        )
        await client.model_sync.executions.list(
            sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(sync_id)}/executions"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ListExecutionResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        try:
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
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            token="YOUR_TOKEN",
        )
        await client.model_sync.executions.get(
            sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/syncs/{jsonable_encoder(sync_id)}/executions/{jsonable_encoder(id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(GetExecutionResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def get_log_urls(
        self, sync_id: str, id: str, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExecutionLogsResponseEnvelope:
        """
        Parameters
        ----------
        sync_id : str

        id : str

        type : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExecutionLogsResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            token="YOUR_TOKEN",
        )
        await client.model_sync.executions.get_log_urls(
            sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            type="records",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/syncs/{jsonable_encoder(sync_id)}/executions/{jsonable_encoder(id)}/{jsonable_encoder(type)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ExecutionLogsResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def get_logs(
        self,
        sync_id: str,
        id: str,
        type: str,
        filename: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        sync_id : str

        id : str

        type : str

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            token="YOUR_TOKEN",
        )
        await client.model_sync.executions.get_logs(
            sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            type="records",
            filename="path/to/file.json",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/syncs/{jsonable_encoder(sync_id)}/executions/{jsonable_encoder(id)}/{jsonable_encoder(type)}/{jsonable_encoder(filename)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)
