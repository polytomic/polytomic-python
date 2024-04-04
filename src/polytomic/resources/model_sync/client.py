# This file was auto-generated from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ...errors.unauthorized_error import UnauthorizedError
from ...types.activate_sync_envelope import ActivateSyncEnvelope
from ...types.activate_sync_input import ActivateSyncInput
from ...types.filter import Filter
from ...types.identity import Identity
from ...types.list_model_sync_response_envelope import ListModelSyncResponseEnvelope
from ...types.model_sync_field import ModelSyncField
from ...types.model_sync_response_envelope import ModelSyncResponseEnvelope
from ...types.override import Override
from ...types.rest_err_response import RestErrResponse
from ...types.schedule import Schedule
from ...types.schedule_option_response_envelope import ScheduleOptionResponseEnvelope
from ...types.start_model_sync_response_envelope import StartModelSyncResponseEnvelope
from ...types.sync_status_envelope import SyncStatusEnvelope
from ...types.target import Target
from .resources.executions.client import AsyncExecutionsClient, ExecutionsClient

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ModelSyncClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.executions = ExecutionsClient(client_wrapper=self._client_wrapper)

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListModelSyncResponseEnvelope:
        """
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/syncs"),
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
            return pydantic.parse_obj_as(ListModelSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        active: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[ModelSyncField]] = OMIT,
        filter_logic: typing.Optional[str] = OMIT,
        filters: typing.Optional[typing.Sequence[Filter]] = OMIT,
        identity: typing.Optional[Identity] = OMIT,
        mode: str,
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        override_fields: typing.Optional[typing.Sequence[ModelSyncField]] = OMIT,
        overrides: typing.Optional[typing.Sequence[Override]] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        schedule: Schedule,
        sync_all_records: typing.Optional[bool] = OMIT,
        target: Target,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelSyncResponseEnvelope:
        """
        Parameters:
            - active: typing.Optional[bool].

            - fields: typing.Optional[typing.Sequence[ModelSyncField]].

            - filter_logic: typing.Optional[str].

            - filters: typing.Optional[typing.Sequence[Filter]].

            - identity: typing.Optional[Identity].

            - mode: str.

            - name: str.

            - organization_id: typing.Optional[str].

            - override_fields: typing.Optional[typing.Sequence[ModelSyncField]].

            - overrides: typing.Optional[typing.Sequence[Override]].

            - policies: typing.Optional[typing.Sequence[str]].

            - schedule: Schedule.

            - sync_all_records: typing.Optional[bool].

            - target: Target.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic import Identity, ModelSyncField, Schedule, Source, Target
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.create(
            fields=[
                ModelSyncField(
                    source=Source(
                        field="id",
                        model_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                    ),
                    target="name",
                )
            ],
            filter_logic="A and B or C",
            identity=Identity(
                function="Equality",
                source=Source(
                    field="id",
                    model_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                ),
                target="name",
            ),
            mode="create",
            name="Users Sync",
            schedule=Schedule(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                frequency="daily",
            ),
            sync_all_records=False,
            target=Target(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                object="Users",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {"mode": mode, "name": name, "schedule": schedule, "target": target}
        if active is not OMIT:
            _request["active"] = active
        if fields is not OMIT:
            _request["fields"] = fields
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
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/syncs"),
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
            return pydantic.parse_obj_as(ModelSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_schedule_options(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScheduleOptionResponseEnvelope:
        """
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.get_schedule_options()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/syncs/schedules"),
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
            return pydantic.parse_obj_as(ScheduleOptionResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ModelSyncResponseEnvelope:
        """
        Parameters:
            - id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}"),
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
            return pydantic.parse_obj_as(ModelSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def remove(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters:
            - id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.remove(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}"),
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
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        id: str,
        *,
        active: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[ModelSyncField]] = OMIT,
        filter_logic: typing.Optional[str] = OMIT,
        filters: typing.Optional[typing.Sequence[Filter]] = OMIT,
        identity: typing.Optional[Identity] = OMIT,
        mode: str,
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        override_fields: typing.Optional[typing.Sequence[ModelSyncField]] = OMIT,
        overrides: typing.Optional[typing.Sequence[Override]] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        schedule: Schedule,
        sync_all_records: typing.Optional[bool] = OMIT,
        target: Target,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelSyncResponseEnvelope:
        """
        Parameters:
            - id: str.

            - active: typing.Optional[bool].

            - fields: typing.Optional[typing.Sequence[ModelSyncField]].

            - filter_logic: typing.Optional[str].

            - filters: typing.Optional[typing.Sequence[Filter]].

            - identity: typing.Optional[Identity].

            - mode: str.

            - name: str.

            - organization_id: typing.Optional[str].

            - override_fields: typing.Optional[typing.Sequence[ModelSyncField]].

            - overrides: typing.Optional[typing.Sequence[Override]].

            - policies: typing.Optional[typing.Sequence[str]].

            - schedule: Schedule.

            - sync_all_records: typing.Optional[bool].

            - target: Target.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic import Identity, ModelSyncField, Schedule, Source, Target
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            fields=[
                ModelSyncField(
                    source=Source(
                        field="id",
                        model_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                    ),
                    target="name",
                )
            ],
            filter_logic="A and B or C",
            identity=Identity(
                function="Equality",
                source=Source(
                    field="id",
                    model_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                ),
                target="name",
            ),
            mode="create",
            name="Users Sync",
            schedule=Schedule(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                frequency="daily",
            ),
            sync_all_records=False,
            target=Target(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                object="Users",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {"mode": mode, "name": name, "schedule": schedule, "target": target}
        if active is not OMIT:
            _request["active"] = active
        if fields is not OMIT:
            _request["fields"] = fields
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
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}"),
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
            return pydantic.parse_obj_as(ModelSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def activate(
        self, id: str, *, request: ActivateSyncInput, request_options: typing.Optional[RequestOptions] = None
    ) -> ActivateSyncEnvelope:
        """
        Parameters:
            - id: str.

            - request: ActivateSyncInput.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic import ActivateSyncInput
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.activate(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            request=ActivateSyncInput(
                active=True,
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}/activate"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
            return pydantic.parse_obj_as(ActivateSyncEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def start(
        self,
        id: str,
        *,
        identities: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StartModelSyncResponseEnvelope:
        """
        Parameters:
            - id: str.

            - identities: typing.Optional[typing.Sequence[str]].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.start(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if identities is not OMIT:
            _request["identities"] = identities
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
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
            return pydantic.parse_obj_as(StartModelSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_status(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> SyncStatusEnvelope:
        """
        Parameters:
            - id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.get_status(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}/status"),
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
            return pydantic.parse_obj_as(SyncStatusEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncModelSyncClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.executions = AsyncExecutionsClient(client_wrapper=self._client_wrapper)

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListModelSyncResponseEnvelope:
        """
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/syncs"),
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
            return pydantic.parse_obj_as(ListModelSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        active: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[ModelSyncField]] = OMIT,
        filter_logic: typing.Optional[str] = OMIT,
        filters: typing.Optional[typing.Sequence[Filter]] = OMIT,
        identity: typing.Optional[Identity] = OMIT,
        mode: str,
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        override_fields: typing.Optional[typing.Sequence[ModelSyncField]] = OMIT,
        overrides: typing.Optional[typing.Sequence[Override]] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        schedule: Schedule,
        sync_all_records: typing.Optional[bool] = OMIT,
        target: Target,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelSyncResponseEnvelope:
        """
        Parameters:
            - active: typing.Optional[bool].

            - fields: typing.Optional[typing.Sequence[ModelSyncField]].

            - filter_logic: typing.Optional[str].

            - filters: typing.Optional[typing.Sequence[Filter]].

            - identity: typing.Optional[Identity].

            - mode: str.

            - name: str.

            - organization_id: typing.Optional[str].

            - override_fields: typing.Optional[typing.Sequence[ModelSyncField]].

            - overrides: typing.Optional[typing.Sequence[Override]].

            - policies: typing.Optional[typing.Sequence[str]].

            - schedule: Schedule.

            - sync_all_records: typing.Optional[bool].

            - target: Target.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic import Identity, ModelSyncField, Schedule, Source, Target
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.create(
            fields=[
                ModelSyncField(
                    source=Source(
                        field="id",
                        model_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                    ),
                    target="name",
                )
            ],
            filter_logic="A and B or C",
            identity=Identity(
                function="Equality",
                source=Source(
                    field="id",
                    model_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                ),
                target="name",
            ),
            mode="create",
            name="Users Sync",
            schedule=Schedule(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                frequency="daily",
            ),
            sync_all_records=False,
            target=Target(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                object="Users",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {"mode": mode, "name": name, "schedule": schedule, "target": target}
        if active is not OMIT:
            _request["active"] = active
        if fields is not OMIT:
            _request["fields"] = fields
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
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/syncs"),
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
            return pydantic.parse_obj_as(ModelSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_schedule_options(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScheduleOptionResponseEnvelope:
        """
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.get_schedule_options()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/syncs/schedules"),
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
            return pydantic.parse_obj_as(ScheduleOptionResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ModelSyncResponseEnvelope:
        """
        Parameters:
            - id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}"),
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
            return pydantic.parse_obj_as(ModelSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def remove(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters:
            - id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.remove(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}"),
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
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        id: str,
        *,
        active: typing.Optional[bool] = OMIT,
        fields: typing.Optional[typing.Sequence[ModelSyncField]] = OMIT,
        filter_logic: typing.Optional[str] = OMIT,
        filters: typing.Optional[typing.Sequence[Filter]] = OMIT,
        identity: typing.Optional[Identity] = OMIT,
        mode: str,
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        override_fields: typing.Optional[typing.Sequence[ModelSyncField]] = OMIT,
        overrides: typing.Optional[typing.Sequence[Override]] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        schedule: Schedule,
        sync_all_records: typing.Optional[bool] = OMIT,
        target: Target,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelSyncResponseEnvelope:
        """
        Parameters:
            - id: str.

            - active: typing.Optional[bool].

            - fields: typing.Optional[typing.Sequence[ModelSyncField]].

            - filter_logic: typing.Optional[str].

            - filters: typing.Optional[typing.Sequence[Filter]].

            - identity: typing.Optional[Identity].

            - mode: str.

            - name: str.

            - organization_id: typing.Optional[str].

            - override_fields: typing.Optional[typing.Sequence[ModelSyncField]].

            - overrides: typing.Optional[typing.Sequence[Override]].

            - policies: typing.Optional[typing.Sequence[str]].

            - schedule: Schedule.

            - sync_all_records: typing.Optional[bool].

            - target: Target.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic import Identity, ModelSyncField, Schedule, Source, Target
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            fields=[
                ModelSyncField(
                    source=Source(
                        field="id",
                        model_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                    ),
                    target="name",
                )
            ],
            filter_logic="A and B or C",
            identity=Identity(
                function="Equality",
                source=Source(
                    field="id",
                    model_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                ),
                target="name",
            ),
            mode="create",
            name="Users Sync",
            schedule=Schedule(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                frequency="daily",
            ),
            sync_all_records=False,
            target=Target(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                object="Users",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {"mode": mode, "name": name, "schedule": schedule, "target": target}
        if active is not OMIT:
            _request["active"] = active
        if fields is not OMIT:
            _request["fields"] = fields
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
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}"),
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
            return pydantic.parse_obj_as(ModelSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def activate(
        self, id: str, *, request: ActivateSyncInput, request_options: typing.Optional[RequestOptions] = None
    ) -> ActivateSyncEnvelope:
        """
        Parameters:
            - id: str.

            - request: ActivateSyncInput.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic import ActivateSyncInput
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.activate(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            request=ActivateSyncInput(
                active=True,
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}/activate"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
            return pydantic.parse_obj_as(ActivateSyncEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def start(
        self,
        id: str,
        *,
        identities: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StartModelSyncResponseEnvelope:
        """
        Parameters:
            - id: str.

            - identities: typing.Optional[typing.Sequence[str]].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.start(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if identities is not OMIT:
            _request["identities"] = identities
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
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
            return pydantic.parse_obj_as(StartModelSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_status(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SyncStatusEnvelope:
        """
        Parameters:
            - id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.get_status(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{jsonable_encoder(id)}/status"),
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
            return pydantic.parse_obj_as(SyncStatusEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
