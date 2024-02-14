# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...errors.unauthorized_error import UnauthorizedError
from ...types.rest_err_response import RestErrResponse
from ...types.v_2_activate_sync_envelope import V2ActivateSyncEnvelope
from ...types.v_2_activate_sync_input import V2ActivateSyncInput
from ...types.v_2_filter import V2Filter
from ...types.v_2_identity import V2Identity
from ...types.v_2_list_sync_response_envelope import V2ListSyncResponseEnvelope
from ...types.v_2_override import V2Override
from ...types.v_2_schedule import V2Schedule
from ...types.v_2_start_sync_response_envelope import V2StartSyncResponseEnvelope
from ...types.v_2_sync_field import V2SyncField
from ...types.v_2_sync_response_envelope import V2SyncResponseEnvelope
from ...types.v_2_sync_status_envelope import V2SyncStatusEnvelope
from ...types.v_2_target import V2Target
from .resources.executions.client import AsyncExecutionsClient, ExecutionsClient
from .types.v_2_create_sync_request_mode import V2CreateSyncRequestMode
from .types.v_2_update_sync_request_mode import V2UpdateSyncRequestMode

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

    def list(self) -> V2ListSyncResponseEnvelope:
        """
        from polytomic.client import Polytomic

        client = Polytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/syncs"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2ListSyncResponseEnvelope, _response.json())  # type: ignore
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
        fields: typing.Optional[typing.List[V2SyncField]] = OMIT,
        filter_logic: typing.Optional[str] = OMIT,
        filters: typing.Optional[typing.List[V2Filter]] = OMIT,
        identity: typing.Optional[V2Identity] = OMIT,
        mode: V2CreateSyncRequestMode,
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        override_fields: typing.Optional[typing.List[V2SyncField]] = OMIT,
        overrides: typing.Optional[typing.List[V2Override]] = OMIT,
        policies: typing.Optional[typing.List[str]] = OMIT,
        schedule: V2Schedule,
        sync_all_records: typing.Optional[bool] = OMIT,
        target: V2Target,
    ) -> V2SyncResponseEnvelope:
        """
        Parameters:
            - active: typing.Optional[bool].

            - fields: typing.Optional[typing.List[V2SyncField]].

            - filter_logic: typing.Optional[str].

            - filters: typing.Optional[typing.List[V2Filter]].

            - identity: typing.Optional[V2Identity].

            - mode: V2CreateSyncRequestMode.

            - name: str.

            - organization_id: typing.Optional[str].

            - override_fields: typing.Optional[typing.List[V2SyncField]].

            - overrides: typing.Optional[typing.List[V2Override]].

            - policies: typing.Optional[typing.List[str]].

            - schedule: V2Schedule.

            - sync_all_records: typing.Optional[bool].

            - target: V2Target.
        ---
        from polytomic import (
            V2CreateSyncRequestMode,
            V2Identity,
            V2Schedule,
            V2Source,
            V2SyncField,
            V2Target,
        )
        from polytomic.client import Polytomic

        client = Polytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.create(
            fields=[
                V2SyncField(
                    source=V2Source(
                        field="id",
                        model_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                    ),
                    target="name",
                )
            ],
            filter_logic="A and B or C",
            identity=V2Identity(
                function="function",
                source=V2Source(
                    field="id",
                    model_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                ),
                target="name",
            ),
            mode=V2CreateSyncRequestMode.UPDATE,
            name="Users Sync",
            schedule=V2Schedule(),
            target=V2Target(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                object="Users",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "mode": mode.value,
            "name": name,
            "schedule": schedule,
            "target": target,
        }
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
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2SyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str) -> V2SyncResponseEnvelope:
        """
        Parameters:
            - id: str.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2SyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def remove(self, id: str) -> None:
        """
        Parameters:
            - id: str.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.remove(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
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
        fields: typing.Optional[typing.List[V2SyncField]] = OMIT,
        filter_logic: typing.Optional[str] = OMIT,
        filters: typing.Optional[typing.List[V2Filter]] = OMIT,
        identity: typing.Optional[V2Identity] = OMIT,
        mode: V2UpdateSyncRequestMode,
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        override_fields: typing.Optional[typing.List[V2SyncField]] = OMIT,
        overrides: typing.Optional[typing.List[V2Override]] = OMIT,
        policies: typing.Optional[typing.List[str]] = OMIT,
        schedule: V2Schedule,
        sync_all_records: typing.Optional[bool] = OMIT,
        target: V2Target,
    ) -> V2SyncResponseEnvelope:
        """
        Parameters:
            - id: str.

            - active: typing.Optional[bool].

            - fields: typing.Optional[typing.List[V2SyncField]].

            - filter_logic: typing.Optional[str].

            - filters: typing.Optional[typing.List[V2Filter]].

            - identity: typing.Optional[V2Identity].

            - mode: V2UpdateSyncRequestMode.

            - name: str.

            - organization_id: typing.Optional[str].

            - override_fields: typing.Optional[typing.List[V2SyncField]].

            - overrides: typing.Optional[typing.List[V2Override]].

            - policies: typing.Optional[typing.List[str]].

            - schedule: V2Schedule.

            - sync_all_records: typing.Optional[bool].

            - target: V2Target.
        ---
        from polytomic import (
            V2Identity,
            V2Schedule,
            V2Source,
            V2SyncField,
            V2Target,
            V2UpdateSyncRequestMode,
        )
        from polytomic.client import Polytomic

        client = Polytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            fields=[
                V2SyncField(
                    source=V2Source(
                        field="id",
                        model_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                    ),
                    target="name",
                )
            ],
            filter_logic="A and B or C",
            identity=V2Identity(
                function="function",
                source=V2Source(
                    field="id",
                    model_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                ),
                target="name",
            ),
            mode=V2UpdateSyncRequestMode.UPDATE,
            name="Users Sync",
            schedule=V2Schedule(),
            target=V2Target(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                object="Users",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "mode": mode.value,
            "name": name,
            "schedule": schedule,
            "target": target,
        }
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
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{id}"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2SyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def activate(self, id: str, *, request: V2ActivateSyncInput) -> V2ActivateSyncEnvelope:
        """
        Parameters:
            - id: str.

            - request: V2ActivateSyncInput.
        ---
        from polytomic import V2ActivateSyncInput
        from polytomic.client import Polytomic

        client = Polytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.activate(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            request=V2ActivateSyncInput(
                active=True,
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{id}/activate"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2ActivateSyncEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def start(self, id: str, *, identities: typing.Optional[typing.List[str]] = OMIT) -> V2StartSyncResponseEnvelope:
        """
        Parameters:
            - id: str.

            - identities: typing.Optional[typing.List[str]].
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
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
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{id}/executions"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2StartSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_status(self, id: str) -> V2SyncStatusEnvelope:
        """
        Parameters:
            - id: str.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.model_sync.get_status(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{id}/status"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2SyncStatusEnvelope, _response.json())  # type: ignore
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

    async def list(self) -> V2ListSyncResponseEnvelope:
        """
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/syncs"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2ListSyncResponseEnvelope, _response.json())  # type: ignore
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
        fields: typing.Optional[typing.List[V2SyncField]] = OMIT,
        filter_logic: typing.Optional[str] = OMIT,
        filters: typing.Optional[typing.List[V2Filter]] = OMIT,
        identity: typing.Optional[V2Identity] = OMIT,
        mode: V2CreateSyncRequestMode,
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        override_fields: typing.Optional[typing.List[V2SyncField]] = OMIT,
        overrides: typing.Optional[typing.List[V2Override]] = OMIT,
        policies: typing.Optional[typing.List[str]] = OMIT,
        schedule: V2Schedule,
        sync_all_records: typing.Optional[bool] = OMIT,
        target: V2Target,
    ) -> V2SyncResponseEnvelope:
        """
        Parameters:
            - active: typing.Optional[bool].

            - fields: typing.Optional[typing.List[V2SyncField]].

            - filter_logic: typing.Optional[str].

            - filters: typing.Optional[typing.List[V2Filter]].

            - identity: typing.Optional[V2Identity].

            - mode: V2CreateSyncRequestMode.

            - name: str.

            - organization_id: typing.Optional[str].

            - override_fields: typing.Optional[typing.List[V2SyncField]].

            - overrides: typing.Optional[typing.List[V2Override]].

            - policies: typing.Optional[typing.List[str]].

            - schedule: V2Schedule.

            - sync_all_records: typing.Optional[bool].

            - target: V2Target.
        ---
        from polytomic import (
            V2CreateSyncRequestMode,
            V2Identity,
            V2Schedule,
            V2Source,
            V2SyncField,
            V2Target,
        )
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.create(
            fields=[
                V2SyncField(
                    source=V2Source(
                        field="id",
                        model_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                    ),
                    target="name",
                )
            ],
            filter_logic="A and B or C",
            identity=V2Identity(
                function="function",
                source=V2Source(
                    field="id",
                    model_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                ),
                target="name",
            ),
            mode=V2CreateSyncRequestMode.UPDATE,
            name="Users Sync",
            schedule=V2Schedule(),
            target=V2Target(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                object="Users",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "mode": mode.value,
            "name": name,
            "schedule": schedule,
            "target": target,
        }
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
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2SyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: str) -> V2SyncResponseEnvelope:
        """
        Parameters:
            - id: str.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2SyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def remove(self, id: str) -> None:
        """
        Parameters:
            - id: str.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.remove(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
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
        fields: typing.Optional[typing.List[V2SyncField]] = OMIT,
        filter_logic: typing.Optional[str] = OMIT,
        filters: typing.Optional[typing.List[V2Filter]] = OMIT,
        identity: typing.Optional[V2Identity] = OMIT,
        mode: V2UpdateSyncRequestMode,
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        override_fields: typing.Optional[typing.List[V2SyncField]] = OMIT,
        overrides: typing.Optional[typing.List[V2Override]] = OMIT,
        policies: typing.Optional[typing.List[str]] = OMIT,
        schedule: V2Schedule,
        sync_all_records: typing.Optional[bool] = OMIT,
        target: V2Target,
    ) -> V2SyncResponseEnvelope:
        """
        Parameters:
            - id: str.

            - active: typing.Optional[bool].

            - fields: typing.Optional[typing.List[V2SyncField]].

            - filter_logic: typing.Optional[str].

            - filters: typing.Optional[typing.List[V2Filter]].

            - identity: typing.Optional[V2Identity].

            - mode: V2UpdateSyncRequestMode.

            - name: str.

            - organization_id: typing.Optional[str].

            - override_fields: typing.Optional[typing.List[V2SyncField]].

            - overrides: typing.Optional[typing.List[V2Override]].

            - policies: typing.Optional[typing.List[str]].

            - schedule: V2Schedule.

            - sync_all_records: typing.Optional[bool].

            - target: V2Target.
        ---
        from polytomic import (
            V2Identity,
            V2Schedule,
            V2Source,
            V2SyncField,
            V2Target,
            V2UpdateSyncRequestMode,
        )
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            fields=[
                V2SyncField(
                    source=V2Source(
                        field="id",
                        model_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                    ),
                    target="name",
                )
            ],
            filter_logic="A and B or C",
            identity=V2Identity(
                function="function",
                source=V2Source(
                    field="id",
                    model_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                ),
                target="name",
            ),
            mode=V2UpdateSyncRequestMode.UPDATE,
            name="Users Sync",
            schedule=V2Schedule(),
            target=V2Target(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                object="Users",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {
            "mode": mode.value,
            "name": name,
            "schedule": schedule,
            "target": target,
        }
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
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{id}"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2SyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def activate(self, id: str, *, request: V2ActivateSyncInput) -> V2ActivateSyncEnvelope:
        """
        Parameters:
            - id: str.

            - request: V2ActivateSyncInput.
        ---
        from polytomic import V2ActivateSyncInput
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.activate(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            request=V2ActivateSyncInput(
                active=True,
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{id}/activate"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2ActivateSyncEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def start(
        self, id: str, *, identities: typing.Optional[typing.List[str]] = OMIT
    ) -> V2StartSyncResponseEnvelope:
        """
        Parameters:
            - id: str.

            - identities: typing.Optional[typing.List[str]].
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
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
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{id}/executions"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2StartSyncResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_status(self, id: str) -> V2SyncStatusEnvelope:
        """
        Parameters:
            - id: str.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            polytomic_version="YOUR_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.model_sync.get_status(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/syncs/{id}/status"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(V2SyncStatusEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)