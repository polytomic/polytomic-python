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
from ...types.bulk_discover import BulkDiscover
from ...types.bulk_schedule import BulkSchedule
from ...types.bulk_sync_dest_envelope import BulkSyncDestEnvelope
from ...types.bulk_sync_list_envelope import BulkSyncListEnvelope
from ...types.bulk_sync_response_envelope import BulkSyncResponseEnvelope
from ...types.bulk_sync_source_envelope import BulkSyncSourceEnvelope
from ...types.bulk_sync_source_schema_envelope import BulkSyncSourceSchemaEnvelope
from ...types.bulk_sync_source_status_envelope import BulkSyncSourceStatusEnvelope
from ...types.bulk_sync_status_envelope import BulkSyncStatusEnvelope
from ...types.rest_err_response import RestErrResponse
from .resources.executions.client import AsyncExecutionsClient, ExecutionsClient
from .resources.schemas.client import AsyncSchemasClient, SchemasClient

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class BulkSyncClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.executions = ExecutionsClient(client_wrapper=self._client_wrapper)
        self.schemas = SchemasClient(client_wrapper=self._client_wrapper)

    def get_destination(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkSyncDestEnvelope:
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
        client.bulk_sync.get_destination(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/bulk/dest/{jsonable_encoder(id)}"),
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
            return pydantic.parse_obj_as(BulkSyncDestEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_source(
        self,
        connection_id: str,
        *,
        refresh_schemas: typing.Optional[bool] = None,
        include_fields: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncSourceEnvelope:
        """
        Parameters:
            - connection_id: str.

            - refresh_schemas: typing.Optional[bool].

            - include_fields: typing.Optional[bool].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.get_source(
            connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            include_fields=True,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/bulk/source/{jsonable_encoder(connection_id)}"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "refresh_schemas": refresh_schemas,
                        "include_fields": include_fields,
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
            return pydantic.parse_obj_as(BulkSyncSourceEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_source_schema(
        self, connection_id: str, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkSyncSourceSchemaEnvelope:
        """
        Parameters:
            - connection_id: str.

            - schema_id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.get_source_schema(
            connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            schema_id="schema_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/bulk/source/{jsonable_encoder(connection_id)}/schema/{jsonable_encoder(schema_id)}",
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
            return pydantic.parse_obj_as(BulkSyncSourceSchemaEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_source_status(
        self, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkSyncSourceStatusEnvelope:
        """
        Parameters:
            - connection_id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.get_source_status(
            connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/bulk/source/{jsonable_encoder(connection_id)}/status"
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
            return pydantic.parse_obj_as(BulkSyncSourceStatusEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> BulkSyncListEnvelope:
        """
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/bulk/syncs"),
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
            return pydantic.parse_obj_as(BulkSyncListEnvelope, _response.json())  # type: ignore
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
        automatically_add_new_fields: typing.Optional[BulkDiscover] = OMIT,
        automatically_add_new_objects: typing.Optional[BulkDiscover] = OMIT,
        destination_configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        destination_connection_id: str,
        disable_record_timestamps: typing.Optional[bool] = OMIT,
        discover: typing.Optional[bool] = OMIT,
        mode: typing.Optional[str] = OMIT,
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        schedule: BulkSchedule,
        schemas: typing.Optional[typing.Sequence[str]] = OMIT,
        source_configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        source_connection_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncResponseEnvelope:
        """
        Parameters:
            - active: typing.Optional[bool].

            - automatically_add_new_fields: typing.Optional[BulkDiscover].

            - automatically_add_new_objects: typing.Optional[BulkDiscover].

            - destination_configuration: typing.Optional[typing.Dict[str, typing.Any]].

            - destination_connection_id: str.

            - disable_record_timestamps: typing.Optional[bool].

            - discover: typing.Optional[bool]. DEPRECATED: Use automatically_add_new_objects/automatically_add_new_fields instead

            - mode: typing.Optional[str].

            - name: str.

            - organization_id: typing.Optional[str].

            - policies: typing.Optional[typing.Sequence[str]].

            - schedule: BulkSchedule.

            - schemas: typing.Optional[typing.Sequence[str]].

            - source_configuration: typing.Optional[typing.Dict[str, typing.Any]].

            - source_connection_id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic import BulkSchedule, ScheduleFrequency
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.create(
            destination_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            name="name",
            schedule=BulkSchedule(
                frequency=ScheduleFrequency.MANUAL,
            ),
            source_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "destination_connection_id": destination_connection_id,
            "name": name,
            "schedule": schedule,
            "source_connection_id": source_connection_id,
        }
        if active is not OMIT:
            _request["active"] = active
        if automatically_add_new_fields is not OMIT:
            _request["automatically_add_new_fields"] = automatically_add_new_fields
        if automatically_add_new_objects is not OMIT:
            _request["automatically_add_new_objects"] = automatically_add_new_objects
        if destination_configuration is not OMIT:
            _request["destination_configuration"] = destination_configuration
        if disable_record_timestamps is not OMIT:
            _request["disable_record_timestamps"] = disable_record_timestamps
        if discover is not OMIT:
            _request["discover"] = discover
        if mode is not OMIT:
            _request["mode"] = mode
        if organization_id is not OMIT:
            _request["organization_id"] = organization_id
        if policies is not OMIT:
            _request["policies"] = policies
        if schemas is not OMIT:
            _request["schemas"] = schemas
        if source_configuration is not OMIT:
            _request["source_configuration"] = source_configuration
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/bulk/syncs"),
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
            return pydantic.parse_obj_as(BulkSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self,
        id: str,
        *,
        refresh_schemas: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncResponseEnvelope:
        """
        Parameters:
            - id: str.

            - refresh_schemas: typing.Optional[bool].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            refresh_schemas=True,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/bulk/syncs/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "refresh_schemas": refresh_schemas,
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
            return pydantic.parse_obj_as(BulkSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def remove(
        self,
        id: str,
        *,
        refresh_schemas: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - id: str.

            - refresh_schemas: typing.Optional[bool].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.remove(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            refresh_schemas=True,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/bulk/syncs/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "refresh_schemas": refresh_schemas,
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
        automatically_add_new_fields: typing.Optional[BulkDiscover] = OMIT,
        automatically_add_new_objects: typing.Optional[BulkDiscover] = OMIT,
        destination_configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        destination_connection_id: str,
        disable_record_timestamps: typing.Optional[bool] = OMIT,
        discover: typing.Optional[bool] = OMIT,
        mode: typing.Optional[str] = OMIT,
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        schedule: BulkSchedule,
        schemas: typing.Optional[typing.Sequence[str]] = OMIT,
        source_configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        source_connection_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncResponseEnvelope:
        """
        > 📘 Updating schemas
        >
        > Schema updates can be performed using the [Update Bulk Sync Schemas](https://docs.polytomic.com/reference/apiv3updatebulksyncschemas) endpoint.

        Parameters:
            - id: str.

            - active: typing.Optional[bool].

            - automatically_add_new_fields: typing.Optional[BulkDiscover].

            - automatically_add_new_objects: typing.Optional[BulkDiscover].

            - destination_configuration: typing.Optional[typing.Dict[str, typing.Any]].

            - destination_connection_id: str.

            - disable_record_timestamps: typing.Optional[bool].

            - discover: typing.Optional[bool]. DEPRECATED: Use automatically_add_new_objects/automatically_add_new_fields instead

            - mode: typing.Optional[str].

            - name: str.

            - organization_id: typing.Optional[str].

            - policies: typing.Optional[typing.Sequence[str]].

            - schedule: BulkSchedule.

            - schemas: typing.Optional[typing.Sequence[str]].

            - source_configuration: typing.Optional[typing.Dict[str, typing.Any]].

            - source_connection_id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic import BulkSchedule, ScheduleFrequency
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            destination_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            name="name",
            schedule=BulkSchedule(
                frequency=ScheduleFrequency.MANUAL,
            ),
            source_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "destination_connection_id": destination_connection_id,
            "name": name,
            "schedule": schedule,
            "source_connection_id": source_connection_id,
        }
        if active is not OMIT:
            _request["active"] = active
        if automatically_add_new_fields is not OMIT:
            _request["automatically_add_new_fields"] = automatically_add_new_fields
        if automatically_add_new_objects is not OMIT:
            _request["automatically_add_new_objects"] = automatically_add_new_objects
        if destination_configuration is not OMIT:
            _request["destination_configuration"] = destination_configuration
        if disable_record_timestamps is not OMIT:
            _request["disable_record_timestamps"] = disable_record_timestamps
        if discover is not OMIT:
            _request["discover"] = discover
        if mode is not OMIT:
            _request["mode"] = mode
        if organization_id is not OMIT:
            _request["organization_id"] = organization_id
        if policies is not OMIT:
            _request["policies"] = policies
        if schemas is not OMIT:
            _request["schemas"] = schemas
        if source_configuration is not OMIT:
            _request["source_configuration"] = source_configuration
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/bulk/syncs/{jsonable_encoder(id)}"),
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
            return pydantic.parse_obj_as(BulkSyncResponseEnvelope, _response.json())  # type: ignore
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
        client.bulk_sync.activate(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            request=ActivateSyncInput(
                active=True,
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/bulk/syncs/{jsonable_encoder(id)}/activate"
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

    def get_status(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> BulkSyncStatusEnvelope:
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
        client.bulk_sync.get_status(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/bulk/syncs/{jsonable_encoder(id)}/status"
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
            return pydantic.parse_obj_as(BulkSyncStatusEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncBulkSyncClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.executions = AsyncExecutionsClient(client_wrapper=self._client_wrapper)
        self.schemas = AsyncSchemasClient(client_wrapper=self._client_wrapper)

    async def get_destination(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkSyncDestEnvelope:
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
        await client.bulk_sync.get_destination(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/bulk/dest/{jsonable_encoder(id)}"),
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
            return pydantic.parse_obj_as(BulkSyncDestEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_source(
        self,
        connection_id: str,
        *,
        refresh_schemas: typing.Optional[bool] = None,
        include_fields: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncSourceEnvelope:
        """
        Parameters:
            - connection_id: str.

            - refresh_schemas: typing.Optional[bool].

            - include_fields: typing.Optional[bool].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.bulk_sync.get_source(
            connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            include_fields=True,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/bulk/source/{jsonable_encoder(connection_id)}"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "refresh_schemas": refresh_schemas,
                        "include_fields": include_fields,
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
            return pydantic.parse_obj_as(BulkSyncSourceEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_source_schema(
        self, connection_id: str, schema_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkSyncSourceSchemaEnvelope:
        """
        Parameters:
            - connection_id: str.

            - schema_id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.bulk_sync.get_source_schema(
            connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            schema_id="schema_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/bulk/source/{jsonable_encoder(connection_id)}/schema/{jsonable_encoder(schema_id)}",
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
            return pydantic.parse_obj_as(BulkSyncSourceSchemaEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_source_status(
        self, connection_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkSyncSourceStatusEnvelope:
        """
        Parameters:
            - connection_id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.bulk_sync.get_source_status(
            connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/bulk/source/{jsonable_encoder(connection_id)}/status"
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
            return pydantic.parse_obj_as(BulkSyncSourceStatusEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> BulkSyncListEnvelope:
        """
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.bulk_sync.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/bulk/syncs"),
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
            return pydantic.parse_obj_as(BulkSyncListEnvelope, _response.json())  # type: ignore
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
        automatically_add_new_fields: typing.Optional[BulkDiscover] = OMIT,
        automatically_add_new_objects: typing.Optional[BulkDiscover] = OMIT,
        destination_configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        destination_connection_id: str,
        disable_record_timestamps: typing.Optional[bool] = OMIT,
        discover: typing.Optional[bool] = OMIT,
        mode: typing.Optional[str] = OMIT,
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        schedule: BulkSchedule,
        schemas: typing.Optional[typing.Sequence[str]] = OMIT,
        source_configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        source_connection_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncResponseEnvelope:
        """
        Parameters:
            - active: typing.Optional[bool].

            - automatically_add_new_fields: typing.Optional[BulkDiscover].

            - automatically_add_new_objects: typing.Optional[BulkDiscover].

            - destination_configuration: typing.Optional[typing.Dict[str, typing.Any]].

            - destination_connection_id: str.

            - disable_record_timestamps: typing.Optional[bool].

            - discover: typing.Optional[bool]. DEPRECATED: Use automatically_add_new_objects/automatically_add_new_fields instead

            - mode: typing.Optional[str].

            - name: str.

            - organization_id: typing.Optional[str].

            - policies: typing.Optional[typing.Sequence[str]].

            - schedule: BulkSchedule.

            - schemas: typing.Optional[typing.Sequence[str]].

            - source_configuration: typing.Optional[typing.Dict[str, typing.Any]].

            - source_connection_id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic import BulkSchedule, ScheduleFrequency
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.bulk_sync.create(
            destination_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            name="name",
            schedule=BulkSchedule(
                frequency=ScheduleFrequency.MANUAL,
            ),
            source_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "destination_connection_id": destination_connection_id,
            "name": name,
            "schedule": schedule,
            "source_connection_id": source_connection_id,
        }
        if active is not OMIT:
            _request["active"] = active
        if automatically_add_new_fields is not OMIT:
            _request["automatically_add_new_fields"] = automatically_add_new_fields
        if automatically_add_new_objects is not OMIT:
            _request["automatically_add_new_objects"] = automatically_add_new_objects
        if destination_configuration is not OMIT:
            _request["destination_configuration"] = destination_configuration
        if disable_record_timestamps is not OMIT:
            _request["disable_record_timestamps"] = disable_record_timestamps
        if discover is not OMIT:
            _request["discover"] = discover
        if mode is not OMIT:
            _request["mode"] = mode
        if organization_id is not OMIT:
            _request["organization_id"] = organization_id
        if policies is not OMIT:
            _request["policies"] = policies
        if schemas is not OMIT:
            _request["schemas"] = schemas
        if source_configuration is not OMIT:
            _request["source_configuration"] = source_configuration
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/bulk/syncs"),
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
            return pydantic.parse_obj_as(BulkSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self,
        id: str,
        *,
        refresh_schemas: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncResponseEnvelope:
        """
        Parameters:
            - id: str.

            - refresh_schemas: typing.Optional[bool].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.bulk_sync.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            refresh_schemas=True,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/bulk/syncs/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "refresh_schemas": refresh_schemas,
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
            return pydantic.parse_obj_as(BulkSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def remove(
        self,
        id: str,
        *,
        refresh_schemas: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters:
            - id: str.

            - refresh_schemas: typing.Optional[bool].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.bulk_sync.remove(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            refresh_schemas=True,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/bulk/syncs/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "refresh_schemas": refresh_schemas,
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
        automatically_add_new_fields: typing.Optional[BulkDiscover] = OMIT,
        automatically_add_new_objects: typing.Optional[BulkDiscover] = OMIT,
        destination_configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        destination_connection_id: str,
        disable_record_timestamps: typing.Optional[bool] = OMIT,
        discover: typing.Optional[bool] = OMIT,
        mode: typing.Optional[str] = OMIT,
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        schedule: BulkSchedule,
        schemas: typing.Optional[typing.Sequence[str]] = OMIT,
        source_configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        source_connection_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncResponseEnvelope:
        """
        > 📘 Updating schemas
        >
        > Schema updates can be performed using the [Update Bulk Sync Schemas](https://docs.polytomic.com/reference/apiv3updatebulksyncschemas) endpoint.

        Parameters:
            - id: str.

            - active: typing.Optional[bool].

            - automatically_add_new_fields: typing.Optional[BulkDiscover].

            - automatically_add_new_objects: typing.Optional[BulkDiscover].

            - destination_configuration: typing.Optional[typing.Dict[str, typing.Any]].

            - destination_connection_id: str.

            - disable_record_timestamps: typing.Optional[bool].

            - discover: typing.Optional[bool]. DEPRECATED: Use automatically_add_new_objects/automatically_add_new_fields instead

            - mode: typing.Optional[str].

            - name: str.

            - organization_id: typing.Optional[str].

            - policies: typing.Optional[typing.Sequence[str]].

            - schedule: BulkSchedule.

            - schemas: typing.Optional[typing.Sequence[str]].

            - source_configuration: typing.Optional[typing.Dict[str, typing.Any]].

            - source_connection_id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic import BulkSchedule, ScheduleFrequency
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.bulk_sync.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            destination_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            name="name",
            schedule=BulkSchedule(
                frequency=ScheduleFrequency.MANUAL,
            ),
            source_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "destination_connection_id": destination_connection_id,
            "name": name,
            "schedule": schedule,
            "source_connection_id": source_connection_id,
        }
        if active is not OMIT:
            _request["active"] = active
        if automatically_add_new_fields is not OMIT:
            _request["automatically_add_new_fields"] = automatically_add_new_fields
        if automatically_add_new_objects is not OMIT:
            _request["automatically_add_new_objects"] = automatically_add_new_objects
        if destination_configuration is not OMIT:
            _request["destination_configuration"] = destination_configuration
        if disable_record_timestamps is not OMIT:
            _request["disable_record_timestamps"] = disable_record_timestamps
        if discover is not OMIT:
            _request["discover"] = discover
        if mode is not OMIT:
            _request["mode"] = mode
        if organization_id is not OMIT:
            _request["organization_id"] = organization_id
        if policies is not OMIT:
            _request["policies"] = policies
        if schemas is not OMIT:
            _request["schemas"] = schemas
        if source_configuration is not OMIT:
            _request["source_configuration"] = source_configuration
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/bulk/syncs/{jsonable_encoder(id)}"),
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
            return pydantic.parse_obj_as(BulkSyncResponseEnvelope, _response.json())  # type: ignore
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
        await client.bulk_sync.activate(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            request=ActivateSyncInput(
                active=True,
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/bulk/syncs/{jsonable_encoder(id)}/activate"
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

    async def get_status(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkSyncStatusEnvelope:
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
        await client.bulk_sync.get_status(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/bulk/syncs/{jsonable_encoder(id)}/status"
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
            return pydantic.parse_obj_as(BulkSyncStatusEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
