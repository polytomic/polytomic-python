# This file was auto-generated from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError as core_api_error_ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.activate_sync_envelope import ActivateSyncEnvelope
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.enrichment import Enrichment
from ..types.filter import Filter
from ..types.get_connection_meta_envelope import GetConnectionMetaEnvelope
from ..types.get_model_sync_source_meta_envelope import GetModelSyncSourceMetaEnvelope
from ..types.identity import Identity
from ..types.list_model_sync_response_envelope import ListModelSyncResponseEnvelope
from ..types.model_field_response import ModelFieldResponse
from ..types.model_sync_field import ModelSyncField
from ..types.model_sync_response_envelope import ModelSyncResponseEnvelope
from ..types.override import Override
from ..types.rest_err_response import RestErrResponse
from ..types.schedule import Schedule
from ..types.schedule_option_response_envelope import ScheduleOptionResponseEnvelope
from ..types.start_model_sync_response_envelope import StartModelSyncResponseEnvelope
from ..types.sync_status_envelope import SyncStatusEnvelope
from ..types.target import Target
from ..types.target_response_envelope import TargetResponseEnvelope
from .executions.client import AsyncExecutionsClient, ExecutionsClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ModelSyncClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.executions = ExecutionsClient(client_wrapper=self._client_wrapper)

    def get_source(
        self,
        id: str,
        *,
        params: typing.Optional[typing.Dict[str, typing.Optional[typing.Sequence[str]]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetModelSyncSourceMetaEnvelope:
        """
        Parameters
        ----------
        id : str

        params : typing.Optional[typing.Dict[str, typing.Optional[typing.Sequence[str]]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetModelSyncSourceMetaEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.get_source(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}/modelsync/source"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "params": jsonable_encoder(params),
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
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
            return pydantic_v1.parse_obj_as(GetModelSyncSourceMetaEnvelope, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
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

    def get_source_fields(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ModelFieldResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelFieldResponse
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.get_source_fields(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/connections/{jsonable_encoder(id)}/modelsync/source/fields",
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
            return pydantic_v1.parse_obj_as(ModelFieldResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
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

    def get_target(
        self,
        id: str,
        *,
        type: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectionMetaEnvelope:
        """
        Parameters
        ----------
        id : str

        type : typing.Optional[str]

        search : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectionMetaEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.get_target(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}/modelsync/target"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "type": type,
                        "search": search,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
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
            return pydantic_v1.parse_obj_as(GetConnectionMetaEnvelope, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
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

    def get_target_fields(
        self,
        id: str,
        *,
        target: str,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TargetResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        target : str

        refresh : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TargetResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.get_target_fields(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            target="database.table",
            refresh=False,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/connections/{jsonable_encoder(id)}/modelsync/target/fields",
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "target": target,
                        "refresh": refresh,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
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
            return pydantic_v1.parse_obj_as(TargetResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
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

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListModelSyncResponseEnvelope:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListModelSyncResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/syncs"),
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
            return pydantic_v1.parse_obj_as(ListModelSyncResponseEnvelope, _response.json())  # type: ignore
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

    def create(
        self,
        *,
        fields: typing.Sequence[ModelSyncField],
        mode: str,
        name: str,
        schedule: Schedule,
        target: Target,
        active: typing.Optional[bool] = OMIT,
        enricher: typing.Optional[Enrichment] = OMIT,
        filter_logic: typing.Optional[str] = OMIT,
        filters: typing.Optional[typing.Sequence[Filter]] = OMIT,
        identity: typing.Optional[Identity] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        override_fields: typing.Optional[typing.Sequence[ModelSyncField]] = OMIT,
        overrides: typing.Optional[typing.Sequence[Override]] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        sync_all_records: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelSyncResponseEnvelope:
        """
        Parameters
        ----------
        fields : typing.Sequence[ModelSyncField]
            Fields to sync from source to target.

        mode : str

        name : str

        schedule : Schedule

        target : Target

        active : typing.Optional[bool]

        enricher : typing.Optional[Enrichment]

        filter_logic : typing.Optional[str]

        filters : typing.Optional[typing.Sequence[Filter]]

        identity : typing.Optional[Identity]

        organization_id : typing.Optional[str]

        override_fields : typing.Optional[typing.Sequence[ModelSyncField]]
            Values to set in the target unconditionally.

        overrides : typing.Optional[typing.Sequence[Override]]
            Conditional value replacement for fields.

        policies : typing.Optional[typing.Sequence[str]]

        sync_all_records : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelSyncResponseEnvelope
            OK

        Examples
        --------
        from polytomic import ModelSyncField, Schedule, Target
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.create(
            fields=[
                ModelSyncField(
                    target="name",
                )
            ],
            mode="create",
            name="Users Sync",
            schedule=Schedule(),
            target=Target(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                object="Users",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "fields": fields,
            "mode": mode,
            "name": name,
            "schedule": schedule,
            "target": target,
        }
        if active is not OMIT:
            _request["active"] = active
        if enricher is not OMIT:
            _request["enricher"] = enricher
        if filter_logic is not OMIT:
            _request["filter_logic"] = filter_logic
        if filters is not OMIT:
            _request["filters"] = filters
        if identity is not OMIT:
            _request["identity"] = identity
        if organization_id is not OMIT:
            _request["organization_id"] = organization_id
        if override_fields is not OMIT:
            _request["override_fields"] = override_fields
        if overrides is not OMIT:
            _request["overrides"] = overrides
        if policies is not OMIT:
            _request["policies"] = policies
        if sync_all_records is not OMIT:
            _request["sync_all_records"] = sync_all_records
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/syncs"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
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
            return pydantic_v1.parse_obj_as(ModelSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def get_schedule_options(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScheduleOptionResponseEnvelope:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleOptionResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.get_schedule_options()
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/syncs/schedules"),
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
            return pydantic_v1.parse_obj_as(ScheduleOptionResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ModelSyncResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelSyncResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}"),
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
            return pydantic_v1.parse_obj_as(ModelSyncResponseEnvelope, _response.json())  # type: ignore
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

    def update(
        self,
        id: str,
        *,
        fields: typing.Sequence[ModelSyncField],
        mode: str,
        name: str,
        schedule: Schedule,
        target: Target,
        active: typing.Optional[bool] = OMIT,
        enricher: typing.Optional[Enrichment] = OMIT,
        filter_logic: typing.Optional[str] = OMIT,
        filters: typing.Optional[typing.Sequence[Filter]] = OMIT,
        identity: typing.Optional[Identity] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        override_fields: typing.Optional[typing.Sequence[ModelSyncField]] = OMIT,
        overrides: typing.Optional[typing.Sequence[Override]] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        sync_all_records: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelSyncResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        fields : typing.Sequence[ModelSyncField]
            Fields to sync from source to target.

        mode : str

        name : str

        schedule : Schedule

        target : Target

        active : typing.Optional[bool]

        enricher : typing.Optional[Enrichment]

        filter_logic : typing.Optional[str]

        filters : typing.Optional[typing.Sequence[Filter]]

        identity : typing.Optional[Identity]

        organization_id : typing.Optional[str]

        override_fields : typing.Optional[typing.Sequence[ModelSyncField]]
            Values to set in the target unconditionally.

        overrides : typing.Optional[typing.Sequence[Override]]
            Conditional value replacement for fields.

        policies : typing.Optional[typing.Sequence[str]]

        sync_all_records : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelSyncResponseEnvelope
            OK

        Examples
        --------
        from polytomic import ModelSyncField, Schedule, Target
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            fields=[
                ModelSyncField(
                    target="name",
                )
            ],
            mode="create",
            name="Users Sync",
            schedule=Schedule(),
            target=Target(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                object="Users",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "fields": fields,
            "mode": mode,
            "name": name,
            "schedule": schedule,
            "target": target,
        }
        if active is not OMIT:
            _request["active"] = active
        if enricher is not OMIT:
            _request["enricher"] = enricher
        if filter_logic is not OMIT:
            _request["filter_logic"] = filter_logic
        if filters is not OMIT:
            _request["filters"] = filters
        if identity is not OMIT:
            _request["identity"] = identity
        if organization_id is not OMIT:
            _request["organization_id"] = organization_id
        if override_fields is not OMIT:
            _request["override_fields"] = override_fields
        if overrides is not OMIT:
            _request["overrides"] = overrides
        if policies is not OMIT:
            _request["policies"] = policies
        if sync_all_records is not OMIT:
            _request["sync_all_records"] = sync_all_records
        _response = self._client_wrapper.httpx_client.request(
            method="PUT",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
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
            return pydantic_v1.parse_obj_as(ModelSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
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
        client.model_sync.remove(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}"),
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
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
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

    def activate(
        self, id: str, *, active: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> ActivateSyncEnvelope:
        """
        Parameters
        ----------
        id : str

        active : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActivateSyncEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.activate(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            active=True,
        )
        """
        _request: typing.Dict[str, typing.Any] = {"active": active}
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}/activate"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
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
            return pydantic_v1.parse_obj_as(ActivateSyncEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
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

    def start(
        self,
        id: str,
        *,
        identities: typing.Optional[typing.Sequence[str]] = OMIT,
        resync: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StartModelSyncResponseEnvelope:
        """
        > 🚧 Force full resync
        >
        > Use caution when setting the `resync` parameter to `true`. This will force a full resync of the data from the source system. This can be a time-consuming operation and may impact the performance of the source system. It is recommended to only use this option when necessary.

        Parameters
        ----------
        id : str

        identities : typing.Optional[typing.Sequence[str]]

        resync : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StartModelSyncResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.start(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if identities is not OMIT:
            _request["identities"] = identities
        if resync is not OMIT:
            _request["resync"] = resync
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}/executions"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
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
            return pydantic_v1.parse_obj_as(StartModelSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
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

    def get_status(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> SyncStatusEnvelope:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncStatusEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.get_status(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}/status"
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
            return pydantic_v1.parse_obj_as(SyncStatusEnvelope, _response.json())  # type: ignore
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


class AsyncModelSyncClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.executions = AsyncExecutionsClient(client_wrapper=self._client_wrapper)

    async def get_source(
        self,
        id: str,
        *,
        params: typing.Optional[typing.Dict[str, typing.Optional[typing.Sequence[str]]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetModelSyncSourceMetaEnvelope:
        """
        Parameters
        ----------
        id : str

        params : typing.Optional[typing.Dict[str, typing.Optional[typing.Sequence[str]]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetModelSyncSourceMetaEnvelope
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.get_source(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}/modelsync/source"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "params": jsonable_encoder(params),
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
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
            return pydantic_v1.parse_obj_as(GetModelSyncSourceMetaEnvelope, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
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

    async def get_source_fields(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ModelFieldResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelFieldResponse
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.get_source_fields(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/connections/{jsonable_encoder(id)}/modelsync/source/fields",
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
            return pydantic_v1.parse_obj_as(ModelFieldResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
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

    async def get_target(
        self,
        id: str,
        *,
        type: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectionMetaEnvelope:
        """
        Parameters
        ----------
        id : str

        type : typing.Optional[str]

        search : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetConnectionMetaEnvelope
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.get_target(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}/modelsync/target"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "type": type,
                        "search": search,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
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
            return pydantic_v1.parse_obj_as(GetConnectionMetaEnvelope, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
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

    async def get_target_fields(
        self,
        id: str,
        *,
        target: str,
        refresh: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TargetResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        target : str

        refresh : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TargetResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.get_target_fields(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            target="database.table",
            refresh=False,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/connections/{jsonable_encoder(id)}/modelsync/target/fields",
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "target": target,
                        "refresh": refresh,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
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
            return pydantic_v1.parse_obj_as(TargetResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
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

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListModelSyncResponseEnvelope:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListModelSyncResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/syncs"),
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
            return pydantic_v1.parse_obj_as(ListModelSyncResponseEnvelope, _response.json())  # type: ignore
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

    async def create(
        self,
        *,
        fields: typing.Sequence[ModelSyncField],
        mode: str,
        name: str,
        schedule: Schedule,
        target: Target,
        active: typing.Optional[bool] = OMIT,
        enricher: typing.Optional[Enrichment] = OMIT,
        filter_logic: typing.Optional[str] = OMIT,
        filters: typing.Optional[typing.Sequence[Filter]] = OMIT,
        identity: typing.Optional[Identity] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        override_fields: typing.Optional[typing.Sequence[ModelSyncField]] = OMIT,
        overrides: typing.Optional[typing.Sequence[Override]] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        sync_all_records: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelSyncResponseEnvelope:
        """
        Parameters
        ----------
        fields : typing.Sequence[ModelSyncField]
            Fields to sync from source to target.

        mode : str

        name : str

        schedule : Schedule

        target : Target

        active : typing.Optional[bool]

        enricher : typing.Optional[Enrichment]

        filter_logic : typing.Optional[str]

        filters : typing.Optional[typing.Sequence[Filter]]

        identity : typing.Optional[Identity]

        organization_id : typing.Optional[str]

        override_fields : typing.Optional[typing.Sequence[ModelSyncField]]
            Values to set in the target unconditionally.

        overrides : typing.Optional[typing.Sequence[Override]]
            Conditional value replacement for fields.

        policies : typing.Optional[typing.Sequence[str]]

        sync_all_records : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelSyncResponseEnvelope
            OK

        Examples
        --------
        from polytomic import ModelSyncField, Schedule, Target
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.create(
            fields=[
                ModelSyncField(
                    target="name",
                )
            ],
            mode="create",
            name="Users Sync",
            schedule=Schedule(),
            target=Target(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                object="Users",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "fields": fields,
            "mode": mode,
            "name": name,
            "schedule": schedule,
            "target": target,
        }
        if active is not OMIT:
            _request["active"] = active
        if enricher is not OMIT:
            _request["enricher"] = enricher
        if filter_logic is not OMIT:
            _request["filter_logic"] = filter_logic
        if filters is not OMIT:
            _request["filters"] = filters
        if identity is not OMIT:
            _request["identity"] = identity
        if organization_id is not OMIT:
            _request["organization_id"] = organization_id
        if override_fields is not OMIT:
            _request["override_fields"] = override_fields
        if overrides is not OMIT:
            _request["overrides"] = overrides
        if policies is not OMIT:
            _request["policies"] = policies
        if sync_all_records is not OMIT:
            _request["sync_all_records"] = sync_all_records
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/syncs"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
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
            return pydantic_v1.parse_obj_as(ModelSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def get_schedule_options(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScheduleOptionResponseEnvelope:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScheduleOptionResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.get_schedule_options()
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/syncs/schedules"),
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
            return pydantic_v1.parse_obj_as(ScheduleOptionResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ModelSyncResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelSyncResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}"),
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
            return pydantic_v1.parse_obj_as(ModelSyncResponseEnvelope, _response.json())  # type: ignore
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

    async def update(
        self,
        id: str,
        *,
        fields: typing.Sequence[ModelSyncField],
        mode: str,
        name: str,
        schedule: Schedule,
        target: Target,
        active: typing.Optional[bool] = OMIT,
        enricher: typing.Optional[Enrichment] = OMIT,
        filter_logic: typing.Optional[str] = OMIT,
        filters: typing.Optional[typing.Sequence[Filter]] = OMIT,
        identity: typing.Optional[Identity] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        override_fields: typing.Optional[typing.Sequence[ModelSyncField]] = OMIT,
        overrides: typing.Optional[typing.Sequence[Override]] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        sync_all_records: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelSyncResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        fields : typing.Sequence[ModelSyncField]
            Fields to sync from source to target.

        mode : str

        name : str

        schedule : Schedule

        target : Target

        active : typing.Optional[bool]

        enricher : typing.Optional[Enrichment]

        filter_logic : typing.Optional[str]

        filters : typing.Optional[typing.Sequence[Filter]]

        identity : typing.Optional[Identity]

        organization_id : typing.Optional[str]

        override_fields : typing.Optional[typing.Sequence[ModelSyncField]]
            Values to set in the target unconditionally.

        overrides : typing.Optional[typing.Sequence[Override]]
            Conditional value replacement for fields.

        policies : typing.Optional[typing.Sequence[str]]

        sync_all_records : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelSyncResponseEnvelope
            OK

        Examples
        --------
        from polytomic import ModelSyncField, Schedule, Target
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            fields=[
                ModelSyncField(
                    target="name",
                )
            ],
            mode="create",
            name="Users Sync",
            schedule=Schedule(),
            target=Target(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                object="Users",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "fields": fields,
            "mode": mode,
            "name": name,
            "schedule": schedule,
            "target": target,
        }
        if active is not OMIT:
            _request["active"] = active
        if enricher is not OMIT:
            _request["enricher"] = enricher
        if filter_logic is not OMIT:
            _request["filter_logic"] = filter_logic
        if filters is not OMIT:
            _request["filters"] = filters
        if identity is not OMIT:
            _request["identity"] = identity
        if organization_id is not OMIT:
            _request["organization_id"] = organization_id
        if override_fields is not OMIT:
            _request["override_fields"] = override_fields
        if overrides is not OMIT:
            _request["overrides"] = overrides
        if policies is not OMIT:
            _request["policies"] = policies
        if sync_all_records is not OMIT:
            _request["sync_all_records"] = sync_all_records
        _response = await self._client_wrapper.httpx_client.request(
            method="PUT",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
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
            return pydantic_v1.parse_obj_as(ModelSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
            )
        try:
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
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.remove(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}"),
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
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
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

    async def activate(
        self, id: str, *, active: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> ActivateSyncEnvelope:
        """
        Parameters
        ----------
        id : str

        active : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActivateSyncEnvelope
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.activate(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            active=True,
        )
        """
        _request: typing.Dict[str, typing.Any] = {"active": active}
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}/activate"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
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
            return pydantic_v1.parse_obj_as(ActivateSyncEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
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

    async def start(
        self,
        id: str,
        *,
        identities: typing.Optional[typing.Sequence[str]] = OMIT,
        resync: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StartModelSyncResponseEnvelope:
        """
        > 🚧 Force full resync
        >
        > Use caution when setting the `resync` parameter to `true`. This will force a full resync of the data from the source system. This can be a time-consuming operation and may impact the performance of the source system. It is recommended to only use this option when necessary.

        Parameters
        ----------
        id : str

        identities : typing.Optional[typing.Sequence[str]]

        resync : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StartModelSyncResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.start(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if identities is not OMIT:
            _request["identities"] = identities
        if resync is not OMIT:
            _request["resync"] = resync
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}/executions"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
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
            return pydantic_v1.parse_obj_as(StartModelSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json()))  # type: ignore
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

    async def get_status(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SyncStatusEnvelope:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncStatusEnvelope
            OK

        Examples
        --------
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.get_status(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}/status"
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
            return pydantic_v1.parse_obj_as(SyncStatusEnvelope, _response.json())  # type: ignore
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
