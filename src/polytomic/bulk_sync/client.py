# This file was auto-generated from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError as core_api_error_ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.activate_sync_envelope import ActivateSyncEnvelope
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.bulk_discover import BulkDiscover
from ..types.bulk_schedule import BulkSchedule
from ..types.bulk_sync_dest_envelope import BulkSyncDestEnvelope
from ..types.bulk_sync_execution_envelope import BulkSyncExecutionEnvelope
from ..types.bulk_sync_list_envelope import BulkSyncListEnvelope
from ..types.bulk_sync_response_envelope import BulkSyncResponseEnvelope
from ..types.bulk_sync_source_envelope import BulkSyncSourceEnvelope
from ..types.bulk_sync_status_envelope import BulkSyncStatusEnvelope
from ..types.rest_err_response import RestErrResponse
from ..types.sync_mode import SyncMode
from .executions.client import AsyncExecutionsClient, ExecutionsClient
from .schemas.client import AsyncSchemasClient, SchemasClient
from .types.v_2_create_bulk_sync_request_schemas_item import V2CreateBulkSyncRequestSchemasItem
from .types.v_2_update_bulk_sync_request_schemas_item import V2UpdateBulkSyncRequestSchemasItem

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class BulkSyncClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.executions = ExecutionsClient(client_wrapper=self._client_wrapper)
        self.schemas = SchemasClient(client_wrapper=self._client_wrapper)

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> BulkSyncListEnvelope:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSyncListEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/bulk/syncs", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncListEnvelope, _response.json())  # type: ignore
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
        destination_connection_id: str,
        name: str,
        schedule: BulkSchedule,
        source_connection_id: str,
        active: typing.Optional[bool] = OMIT,
        automatically_add_new_fields: typing.Optional[BulkDiscover] = OMIT,
        automatically_add_new_objects: typing.Optional[BulkDiscover] = OMIT,
        destination_configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        disable_record_timestamps: typing.Optional[bool] = OMIT,
        discover: typing.Optional[bool] = OMIT,
        mode: typing.Optional[SyncMode] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        schemas: typing.Optional[typing.Sequence[V2CreateBulkSyncRequestSchemasItem]] = OMIT,
        source_configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncResponseEnvelope:
        """
        Parameters
        ----------
        destination_connection_id : str

        name : str

        schedule : BulkSchedule

        source_connection_id : str

        active : typing.Optional[bool]

        automatically_add_new_fields : typing.Optional[BulkDiscover]

        automatically_add_new_objects : typing.Optional[BulkDiscover]

        destination_configuration : typing.Optional[typing.Dict[str, typing.Any]]

        disable_record_timestamps : typing.Optional[bool]

        discover : typing.Optional[bool]
            DEPRECATED: Use automatically_add_new_objects/automatically_add_new_fields instead

        mode : typing.Optional[SyncMode]

        organization_id : typing.Optional[str]

        policies : typing.Optional[typing.Sequence[str]]

        schemas : typing.Optional[typing.Sequence[V2CreateBulkSyncRequestSchemasItem]]
            List of schemas to sync; if omitted, all schemas will be selected for syncing.

        source_configuration : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSyncResponseEnvelope
            OK

        Examples
        --------
        from polytomic import BulkSchedule
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.create(
            destination_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            name="My Bulk Sync",
            schedule=BulkSchedule(
                frequency="manual",
            ),
            source_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/bulk/syncs",
            method="POST",
            json={
                "active": active,
                "automatically_add_new_fields": automatically_add_new_fields,
                "automatically_add_new_objects": automatically_add_new_objects,
                "destination_configuration": destination_configuration,
                "destination_connection_id": destination_connection_id,
                "disable_record_timestamps": disable_record_timestamps,
                "discover": discover,
                "mode": mode,
                "name": name,
                "organization_id": organization_id,
                "policies": policies,
                "schedule": schedule,
                "schemas": schemas,
                "source_configuration": source_configuration,
                "source_connection_id": source_connection_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncResponseEnvelope, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 403:
                raise ForbiddenError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
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

    def get(
        self,
        id: str,
        *,
        refresh_schemas: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        refresh_schemas : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSyncResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            refresh_schemas=True,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}",
            method="GET",
            params={"refresh_schemas": refresh_schemas},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncResponseEnvelope, _response.json())  # type: ignore
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
        destination_connection_id: str,
        name: str,
        schedule: BulkSchedule,
        source_connection_id: str,
        active: typing.Optional[bool] = OMIT,
        automatically_add_new_fields: typing.Optional[BulkDiscover] = OMIT,
        automatically_add_new_objects: typing.Optional[BulkDiscover] = OMIT,
        destination_configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        disable_record_timestamps: typing.Optional[bool] = OMIT,
        discover: typing.Optional[bool] = OMIT,
        mode: typing.Optional[SyncMode] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        schemas: typing.Optional[typing.Sequence[V2UpdateBulkSyncRequestSchemasItem]] = OMIT,
        source_configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncResponseEnvelope:
        """
        > 📘 Updating schemas
        >
        > Schema updates can be performed using the [Update Bulk Sync Schemas](https://apidocs.polytomic.com/api-reference/bulk-sync/schemas/patch) endpoint.

        Parameters
        ----------
        id : str

        destination_connection_id : str

        name : str

        schedule : BulkSchedule

        source_connection_id : str

        active : typing.Optional[bool]

        automatically_add_new_fields : typing.Optional[BulkDiscover]

        automatically_add_new_objects : typing.Optional[BulkDiscover]

        destination_configuration : typing.Optional[typing.Dict[str, typing.Any]]

        disable_record_timestamps : typing.Optional[bool]

        discover : typing.Optional[bool]
            DEPRECATED: Use automatically_add_new_objects/automatically_add_new_fields instead

        mode : typing.Optional[SyncMode]

        organization_id : typing.Optional[str]

        policies : typing.Optional[typing.Sequence[str]]

        schemas : typing.Optional[typing.Sequence[V2UpdateBulkSyncRequestSchemasItem]]
            List of schemas to sync; if omitted, all schemas will be selected for syncing.

        source_configuration : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSyncResponseEnvelope
            OK

        Examples
        --------
        from polytomic import BulkSchedule
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            destination_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            name="My Bulk Sync",
            schedule=BulkSchedule(
                frequency="manual",
            ),
            source_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}",
            method="PUT",
            json={
                "active": active,
                "automatically_add_new_fields": automatically_add_new_fields,
                "automatically_add_new_objects": automatically_add_new_objects,
                "destination_configuration": destination_configuration,
                "destination_connection_id": destination_connection_id,
                "disable_record_timestamps": disable_record_timestamps,
                "discover": discover,
                "mode": mode,
                "name": name,
                "organization_id": organization_id,
                "policies": policies,
                "schedule": schedule,
                "schemas": schemas,
                "source_configuration": source_configuration,
                "source_connection_id": source_connection_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncResponseEnvelope, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
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

    def remove(
        self,
        id: str,
        *,
        refresh_schemas: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        refresh_schemas : typing.Optional[bool]

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
        client.bulk_sync.remove(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            refresh_schemas=True,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}",
            method="DELETE",
            params={"refresh_schemas": refresh_schemas},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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
        client.bulk_sync.activate(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            active=True,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/activate",
            method="POST",
            json={"active": active},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ActivateSyncEnvelope, _response.json())  # type: ignore
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

    def start(
        self,
        id: str,
        *,
        resync: typing.Optional[bool] = OMIT,
        schemas: typing.Optional[typing.Sequence[str]] = OMIT,
        test: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncExecutionEnvelope:
        """
        Parameters
        ----------
        id : str

        resync : typing.Optional[bool]

        schemas : typing.Optional[typing.Sequence[str]]

        test : typing.Optional[bool]

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
        client.bulk_sync.start(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/executions",
            method="POST",
            json={"resync": resync, "schemas": schemas, "test": test},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncExecutionEnvelope, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def get_status(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> BulkSyncStatusEnvelope:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSyncStatusEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.get_status(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/status", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncStatusEnvelope, _response.json())  # type: ignore
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

    def get_source(
        self,
        id: str,
        *,
        include_fields: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncSourceEnvelope:
        """
        Parameters
        ----------
        id : str

        include_fields : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSyncSourceEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.get_source(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            include_fields=True,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/connections/{jsonable_encoder(id)}/bulksync/source",
            method="GET",
            params={"include_fields": include_fields},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncSourceEnvelope, _response.json())  # type: ignore
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

    def get_destination(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkSyncDestEnvelope:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSyncDestEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.bulk_sync.get_destination(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/connections/{jsonable_encoder(id)}/bulksync/target", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncDestEnvelope, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 403:
                raise ForbiddenError(
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


class AsyncBulkSyncClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.executions = AsyncExecutionsClient(client_wrapper=self._client_wrapper)
        self.schemas = AsyncSchemasClient(client_wrapper=self._client_wrapper)

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> BulkSyncListEnvelope:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSyncListEnvelope
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
            await client.bulk_sync.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/bulk/syncs", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncListEnvelope, _response.json())  # type: ignore
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
        destination_connection_id: str,
        name: str,
        schedule: BulkSchedule,
        source_connection_id: str,
        active: typing.Optional[bool] = OMIT,
        automatically_add_new_fields: typing.Optional[BulkDiscover] = OMIT,
        automatically_add_new_objects: typing.Optional[BulkDiscover] = OMIT,
        destination_configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        disable_record_timestamps: typing.Optional[bool] = OMIT,
        discover: typing.Optional[bool] = OMIT,
        mode: typing.Optional[SyncMode] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        schemas: typing.Optional[typing.Sequence[V2CreateBulkSyncRequestSchemasItem]] = OMIT,
        source_configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncResponseEnvelope:
        """
        Parameters
        ----------
        destination_connection_id : str

        name : str

        schedule : BulkSchedule

        source_connection_id : str

        active : typing.Optional[bool]

        automatically_add_new_fields : typing.Optional[BulkDiscover]

        automatically_add_new_objects : typing.Optional[BulkDiscover]

        destination_configuration : typing.Optional[typing.Dict[str, typing.Any]]

        disable_record_timestamps : typing.Optional[bool]

        discover : typing.Optional[bool]
            DEPRECATED: Use automatically_add_new_objects/automatically_add_new_fields instead

        mode : typing.Optional[SyncMode]

        organization_id : typing.Optional[str]

        policies : typing.Optional[typing.Sequence[str]]

        schemas : typing.Optional[typing.Sequence[V2CreateBulkSyncRequestSchemasItem]]
            List of schemas to sync; if omitted, all schemas will be selected for syncing.

        source_configuration : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSyncResponseEnvelope
            OK

        Examples
        --------
        import asyncio

        from polytomic import BulkSchedule
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bulk_sync.create(
                destination_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                name="My Bulk Sync",
                schedule=BulkSchedule(
                    frequency="manual",
                ),
                source_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/bulk/syncs",
            method="POST",
            json={
                "active": active,
                "automatically_add_new_fields": automatically_add_new_fields,
                "automatically_add_new_objects": automatically_add_new_objects,
                "destination_configuration": destination_configuration,
                "destination_connection_id": destination_connection_id,
                "disable_record_timestamps": disable_record_timestamps,
                "discover": discover,
                "mode": mode,
                "name": name,
                "organization_id": organization_id,
                "policies": policies,
                "schedule": schedule,
                "schemas": schemas,
                "source_configuration": source_configuration,
                "source_connection_id": source_connection_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncResponseEnvelope, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 403:
                raise ForbiddenError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
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

    async def get(
        self,
        id: str,
        *,
        refresh_schemas: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        refresh_schemas : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSyncResponseEnvelope
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
            await client.bulk_sync.get(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
                refresh_schemas=True,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}",
            method="GET",
            params={"refresh_schemas": refresh_schemas},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncResponseEnvelope, _response.json())  # type: ignore
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
        destination_connection_id: str,
        name: str,
        schedule: BulkSchedule,
        source_connection_id: str,
        active: typing.Optional[bool] = OMIT,
        automatically_add_new_fields: typing.Optional[BulkDiscover] = OMIT,
        automatically_add_new_objects: typing.Optional[BulkDiscover] = OMIT,
        destination_configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        disable_record_timestamps: typing.Optional[bool] = OMIT,
        discover: typing.Optional[bool] = OMIT,
        mode: typing.Optional[SyncMode] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        schemas: typing.Optional[typing.Sequence[V2UpdateBulkSyncRequestSchemasItem]] = OMIT,
        source_configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncResponseEnvelope:
        """
        > 📘 Updating schemas
        >
        > Schema updates can be performed using the [Update Bulk Sync Schemas](https://apidocs.polytomic.com/api-reference/bulk-sync/schemas/patch) endpoint.

        Parameters
        ----------
        id : str

        destination_connection_id : str

        name : str

        schedule : BulkSchedule

        source_connection_id : str

        active : typing.Optional[bool]

        automatically_add_new_fields : typing.Optional[BulkDiscover]

        automatically_add_new_objects : typing.Optional[BulkDiscover]

        destination_configuration : typing.Optional[typing.Dict[str, typing.Any]]

        disable_record_timestamps : typing.Optional[bool]

        discover : typing.Optional[bool]
            DEPRECATED: Use automatically_add_new_objects/automatically_add_new_fields instead

        mode : typing.Optional[SyncMode]

        organization_id : typing.Optional[str]

        policies : typing.Optional[typing.Sequence[str]]

        schemas : typing.Optional[typing.Sequence[V2UpdateBulkSyncRequestSchemasItem]]
            List of schemas to sync; if omitted, all schemas will be selected for syncing.

        source_configuration : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSyncResponseEnvelope
            OK

        Examples
        --------
        import asyncio

        from polytomic import BulkSchedule
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bulk_sync.update(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
                destination_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                name="My Bulk Sync",
                schedule=BulkSchedule(
                    frequency="manual",
                ),
                source_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}",
            method="PUT",
            json={
                "active": active,
                "automatically_add_new_fields": automatically_add_new_fields,
                "automatically_add_new_objects": automatically_add_new_objects,
                "destination_configuration": destination_configuration,
                "destination_connection_id": destination_connection_id,
                "disable_record_timestamps": disable_record_timestamps,
                "discover": discover,
                "mode": mode,
                "name": name,
                "organization_id": organization_id,
                "policies": policies,
                "schedule": schedule,
                "schemas": schemas,
                "source_configuration": source_configuration,
                "source_connection_id": source_connection_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncResponseEnvelope, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
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

    async def remove(
        self,
        id: str,
        *,
        refresh_schemas: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        refresh_schemas : typing.Optional[bool]

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
            await client.bulk_sync.remove(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
                refresh_schemas=True,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}",
            method="DELETE",
            params={"refresh_schemas": refresh_schemas},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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
        import asyncio

        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.bulk_sync.activate(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
                active=True,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/activate",
            method="POST",
            json={"active": active},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ActivateSyncEnvelope, _response.json())  # type: ignore
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

    async def start(
        self,
        id: str,
        *,
        resync: typing.Optional[bool] = OMIT,
        schemas: typing.Optional[typing.Sequence[str]] = OMIT,
        test: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncExecutionEnvelope:
        """
        Parameters
        ----------
        id : str

        resync : typing.Optional[bool]

        schemas : typing.Optional[typing.Sequence[str]]

        test : typing.Optional[bool]

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
            await client.bulk_sync.start(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/executions",
            method="POST",
            json={"resync": resync, "schemas": schemas, "test": test},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncExecutionEnvelope, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def get_status(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkSyncStatusEnvelope:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSyncStatusEnvelope
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
            await client.bulk_sync.get_status(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/bulk/syncs/{jsonable_encoder(id)}/status", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncStatusEnvelope, _response.json())  # type: ignore
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

    async def get_source(
        self,
        id: str,
        *,
        include_fields: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkSyncSourceEnvelope:
        """
        Parameters
        ----------
        id : str

        include_fields : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSyncSourceEnvelope
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
            await client.bulk_sync.get_source(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
                include_fields=True,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/connections/{jsonable_encoder(id)}/bulksync/source",
            method="GET",
            params={"include_fields": include_fields},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncSourceEnvelope, _response.json())  # type: ignore
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

    async def get_destination(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BulkSyncDestEnvelope:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkSyncDestEnvelope
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
            await client.bulk_sync.get_destination(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/connections/{jsonable_encoder(id)}/bulksync/target", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(BulkSyncDestEnvelope, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 401:
                raise UnauthorizedError(pydantic_v1.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
            if _response.status_code == 403:
                raise ForbiddenError(
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
