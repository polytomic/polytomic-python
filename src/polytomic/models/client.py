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
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.enrichment import Enrichment
from ..types.get_model_sync_source_meta_envelope import GetModelSyncSourceMetaEnvelope
from ..types.model_list_response_envelope import ModelListResponseEnvelope
from ..types.model_model_field_request import ModelModelFieldRequest
from ..types.model_relation import ModelRelation
from ..types.model_response_envelope import ModelResponseEnvelope
from ..types.model_sample_response_envelope import ModelSampleResponseEnvelope
from ..types.rest_err_response import RestErrResponse
from ..types.v_2_enricher_configuration import V2EnricherConfiguration
from ..types.v_2_get_enrichment_input_fields_response_envelope import V2GetEnrichmentInputFieldsResponseEnvelope

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ModelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_enrichment_source(
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
        client.models.get_enrichment_source(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/connections/{jsonable_encoder(id)}/modelsync/enrichment-source",
            method="GET",
            params={"params": jsonable_encoder(params)},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(GetModelSyncSourceMetaEnvelope, _response.json())  # type: ignore
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

    def post(
        self,
        connection_id: str,
        *,
        configuration: typing.Optional[V2EnricherConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2GetEnrichmentInputFieldsResponseEnvelope:
        """
        For a given connection and enrichment configuration, provides the valid sets of input fields.

        Parameters
        ----------
        connection_id : str

        configuration : typing.Optional[V2EnricherConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2GetEnrichmentInputFieldsResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.models.post(
            connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/enrichment/{jsonable_encoder(connection_id)}/inputfields",
            method="POST",
            json={"configuration": configuration},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(V2GetEnrichmentInputFieldsResponseEnvelope, _response.json())  # type: ignore
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

    def preview(
        self,
        *,
        configuration: typing.Dict[str, typing.Any],
        connection_id: str,
        name: str,
        async_: typing.Optional[bool] = None,
        additional_fields: typing.Optional[typing.Sequence[ModelModelFieldRequest]] = OMIT,
        enricher: typing.Optional[Enrichment] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        identifier: typing.Optional[str] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        relations: typing.Optional[typing.Sequence[ModelRelation]] = OMIT,
        tracking_columns: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelResponseEnvelope:
        """
        Parameters
        ----------
        configuration : typing.Dict[str, typing.Any]

        connection_id : str

        name : str

        async_ : typing.Optional[bool]

        additional_fields : typing.Optional[typing.Sequence[ModelModelFieldRequest]]

        enricher : typing.Optional[Enrichment]

        fields : typing.Optional[typing.Sequence[str]]

        identifier : typing.Optional[str]

        labels : typing.Optional[typing.Sequence[str]]

        organization_id : typing.Optional[str]

        policies : typing.Optional[typing.Sequence[str]]

        relations : typing.Optional[typing.Sequence[ModelRelation]]

        tracking_columns : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.models.preview(
            configuration={"table": "public.users"},
            connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            name="Users",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/model-preview",
            method="POST",
            params={"async": async_},
            json={
                "additional_fields": additional_fields,
                "configuration": configuration,
                "connection_id": connection_id,
                "enricher": enricher,
                "fields": fields,
                "identifier": identifier,
                "labels": labels,
                "name": name,
                "organization_id": organization_id,
                "policies": policies,
                "relations": relations,
                "tracking_columns": tracking_columns,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ModelResponseEnvelope, _response.json())  # type: ignore
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

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ModelListResponseEnvelope:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelListResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.models.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/models", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ModelListResponseEnvelope, _response.json())  # type: ignore
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

    def create(
        self,
        *,
        configuration: typing.Dict[str, typing.Any],
        connection_id: str,
        name: str,
        async_: typing.Optional[bool] = None,
        additional_fields: typing.Optional[typing.Sequence[ModelModelFieldRequest]] = OMIT,
        enricher: typing.Optional[Enrichment] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        identifier: typing.Optional[str] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        relations: typing.Optional[typing.Sequence[ModelRelation]] = OMIT,
        tracking_columns: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelResponseEnvelope:
        """
        Parameters
        ----------
        configuration : typing.Dict[str, typing.Any]

        connection_id : str

        name : str

        async_ : typing.Optional[bool]

        additional_fields : typing.Optional[typing.Sequence[ModelModelFieldRequest]]

        enricher : typing.Optional[Enrichment]

        fields : typing.Optional[typing.Sequence[str]]

        identifier : typing.Optional[str]

        labels : typing.Optional[typing.Sequence[str]]

        organization_id : typing.Optional[str]

        policies : typing.Optional[typing.Sequence[str]]

        relations : typing.Optional[typing.Sequence[ModelRelation]]

        tracking_columns : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.models.create(
            configuration={"table": "public.users"},
            connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            name="Users",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/models",
            method="POST",
            params={"async": async_},
            json={
                "additional_fields": additional_fields,
                "configuration": configuration,
                "connection_id": connection_id,
                "enricher": enricher,
                "fields": fields,
                "identifier": identifier,
                "labels": labels,
                "name": name,
                "organization_id": organization_id,
                "policies": policies,
                "relations": relations,
                "tracking_columns": tracking_columns,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ModelResponseEnvelope, _response.json())  # type: ignore
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

    def get(
        self, id: str, *, async_: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ModelResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        async_ : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.models.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/models/{jsonable_encoder(id)}",
            method="GET",
            params={"async": async_},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ModelResponseEnvelope, _response.json())  # type: ignore
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

    def update(
        self,
        id: str,
        *,
        configuration: typing.Dict[str, typing.Any],
        connection_id: str,
        name: str,
        async_: typing.Optional[bool] = None,
        additional_fields: typing.Optional[typing.Sequence[ModelModelFieldRequest]] = OMIT,
        enricher: typing.Optional[Enrichment] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        identifier: typing.Optional[str] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        relations: typing.Optional[typing.Sequence[ModelRelation]] = OMIT,
        tracking_columns: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        configuration : typing.Dict[str, typing.Any]

        connection_id : str

        name : str

        async_ : typing.Optional[bool]

        additional_fields : typing.Optional[typing.Sequence[ModelModelFieldRequest]]

        enricher : typing.Optional[Enrichment]

        fields : typing.Optional[typing.Sequence[str]]

        identifier : typing.Optional[str]

        labels : typing.Optional[typing.Sequence[str]]

        organization_id : typing.Optional[str]

        policies : typing.Optional[typing.Sequence[str]]

        relations : typing.Optional[typing.Sequence[ModelRelation]]

        tracking_columns : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.models.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            async_=False,
            configuration={"table": "public.users"},
            connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            name="Users",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/models/{jsonable_encoder(id)}",
            method="PUT",
            params={"async": async_},
            json={
                "additional_fields": additional_fields,
                "configuration": configuration,
                "connection_id": connection_id,
                "enricher": enricher,
                "fields": fields,
                "identifier": identifier,
                "labels": labels,
                "name": name,
                "organization_id": organization_id,
                "policies": policies,
                "relations": relations,
                "tracking_columns": tracking_columns,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ModelResponseEnvelope, _response.json())  # type: ignore
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

    def remove(
        self, id: str, *, async_: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        async_ : typing.Optional[bool]

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
        client.models.remove(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/models/{jsonable_encoder(id)}",
            method="DELETE",
            params={"async": async_},
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

    def sample(
        self, id: str, *, async_: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ModelSampleResponseEnvelope:
        """
        Returns sample records from the model. The first ten records that the source provides will be returned after being enriched (if applicable). Synchronous requests must complete within 10s. If either querying or enrichment exceeds 10s, please use the async option.

        Parameters
        ----------
        id : str

        async_ : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelSampleResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.models.sample(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/models/{jsonable_encoder(id)}/sample",
            method="GET",
            params={"async": async_},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ModelSampleResponseEnvelope, _response.json())  # type: ignore
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


class AsyncModelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_enrichment_source(
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
        import asyncio

        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.models.get_enrichment_source(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/connections/{jsonable_encoder(id)}/modelsync/enrichment-source",
            method="GET",
            params={"params": jsonable_encoder(params)},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(GetModelSyncSourceMetaEnvelope, _response.json())  # type: ignore
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

    async def post(
        self,
        connection_id: str,
        *,
        configuration: typing.Optional[V2EnricherConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V2GetEnrichmentInputFieldsResponseEnvelope:
        """
        For a given connection and enrichment configuration, provides the valid sets of input fields.

        Parameters
        ----------
        connection_id : str

        configuration : typing.Optional[V2EnricherConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V2GetEnrichmentInputFieldsResponseEnvelope
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
            await client.models.post(
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/enrichment/{jsonable_encoder(connection_id)}/inputfields",
            method="POST",
            json={"configuration": configuration},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(V2GetEnrichmentInputFieldsResponseEnvelope, _response.json())  # type: ignore
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

    async def preview(
        self,
        *,
        configuration: typing.Dict[str, typing.Any],
        connection_id: str,
        name: str,
        async_: typing.Optional[bool] = None,
        additional_fields: typing.Optional[typing.Sequence[ModelModelFieldRequest]] = OMIT,
        enricher: typing.Optional[Enrichment] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        identifier: typing.Optional[str] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        relations: typing.Optional[typing.Sequence[ModelRelation]] = OMIT,
        tracking_columns: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelResponseEnvelope:
        """
        Parameters
        ----------
        configuration : typing.Dict[str, typing.Any]

        connection_id : str

        name : str

        async_ : typing.Optional[bool]

        additional_fields : typing.Optional[typing.Sequence[ModelModelFieldRequest]]

        enricher : typing.Optional[Enrichment]

        fields : typing.Optional[typing.Sequence[str]]

        identifier : typing.Optional[str]

        labels : typing.Optional[typing.Sequence[str]]

        organization_id : typing.Optional[str]

        policies : typing.Optional[typing.Sequence[str]]

        relations : typing.Optional[typing.Sequence[ModelRelation]]

        tracking_columns : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelResponseEnvelope
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
            await client.models.preview(
                configuration={"table": "public.users"},
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                name="Users",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/model-preview",
            method="POST",
            params={"async": async_},
            json={
                "additional_fields": additional_fields,
                "configuration": configuration,
                "connection_id": connection_id,
                "enricher": enricher,
                "fields": fields,
                "identifier": identifier,
                "labels": labels,
                "name": name,
                "organization_id": organization_id,
                "policies": policies,
                "relations": relations,
                "tracking_columns": tracking_columns,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ModelResponseEnvelope, _response.json())  # type: ignore
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

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ModelListResponseEnvelope:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelListResponseEnvelope
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
            await client.models.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/models", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ModelListResponseEnvelope, _response.json())  # type: ignore
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

    async def create(
        self,
        *,
        configuration: typing.Dict[str, typing.Any],
        connection_id: str,
        name: str,
        async_: typing.Optional[bool] = None,
        additional_fields: typing.Optional[typing.Sequence[ModelModelFieldRequest]] = OMIT,
        enricher: typing.Optional[Enrichment] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        identifier: typing.Optional[str] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        relations: typing.Optional[typing.Sequence[ModelRelation]] = OMIT,
        tracking_columns: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelResponseEnvelope:
        """
        Parameters
        ----------
        configuration : typing.Dict[str, typing.Any]

        connection_id : str

        name : str

        async_ : typing.Optional[bool]

        additional_fields : typing.Optional[typing.Sequence[ModelModelFieldRequest]]

        enricher : typing.Optional[Enrichment]

        fields : typing.Optional[typing.Sequence[str]]

        identifier : typing.Optional[str]

        labels : typing.Optional[typing.Sequence[str]]

        organization_id : typing.Optional[str]

        policies : typing.Optional[typing.Sequence[str]]

        relations : typing.Optional[typing.Sequence[ModelRelation]]

        tracking_columns : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelResponseEnvelope
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
            await client.models.create(
                configuration={"table": "public.users"},
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                name="Users",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/models",
            method="POST",
            params={"async": async_},
            json={
                "additional_fields": additional_fields,
                "configuration": configuration,
                "connection_id": connection_id,
                "enricher": enricher,
                "fields": fields,
                "identifier": identifier,
                "labels": labels,
                "name": name,
                "organization_id": organization_id,
                "policies": policies,
                "relations": relations,
                "tracking_columns": tracking_columns,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ModelResponseEnvelope, _response.json())  # type: ignore
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

    async def get(
        self, id: str, *, async_: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ModelResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        async_ : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelResponseEnvelope
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
            await client.models.get(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/models/{jsonable_encoder(id)}",
            method="GET",
            params={"async": async_},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ModelResponseEnvelope, _response.json())  # type: ignore
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

    async def update(
        self,
        id: str,
        *,
        configuration: typing.Dict[str, typing.Any],
        connection_id: str,
        name: str,
        async_: typing.Optional[bool] = None,
        additional_fields: typing.Optional[typing.Sequence[ModelModelFieldRequest]] = OMIT,
        enricher: typing.Optional[Enrichment] = OMIT,
        fields: typing.Optional[typing.Sequence[str]] = OMIT,
        identifier: typing.Optional[str] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        relations: typing.Optional[typing.Sequence[ModelRelation]] = OMIT,
        tracking_columns: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        configuration : typing.Dict[str, typing.Any]

        connection_id : str

        name : str

        async_ : typing.Optional[bool]

        additional_fields : typing.Optional[typing.Sequence[ModelModelFieldRequest]]

        enricher : typing.Optional[Enrichment]

        fields : typing.Optional[typing.Sequence[str]]

        identifier : typing.Optional[str]

        labels : typing.Optional[typing.Sequence[str]]

        organization_id : typing.Optional[str]

        policies : typing.Optional[typing.Sequence[str]]

        relations : typing.Optional[typing.Sequence[ModelRelation]]

        tracking_columns : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelResponseEnvelope
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
            await client.models.update(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
                async_=False,
                configuration={"table": "public.users"},
                connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
                name="Users",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/models/{jsonable_encoder(id)}",
            method="PUT",
            params={"async": async_},
            json={
                "additional_fields": additional_fields,
                "configuration": configuration,
                "connection_id": connection_id,
                "enricher": enricher,
                "fields": fields,
                "identifier": identifier,
                "labels": labels,
                "name": name,
                "organization_id": organization_id,
                "policies": policies,
                "relations": relations,
                "tracking_columns": tracking_columns,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ModelResponseEnvelope, _response.json())  # type: ignore
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

    async def remove(
        self, id: str, *, async_: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        async_ : typing.Optional[bool]

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
            await client.models.remove(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/models/{jsonable_encoder(id)}",
            method="DELETE",
            params={"async": async_},
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

    async def sample(
        self, id: str, *, async_: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ModelSampleResponseEnvelope:
        """
        Returns sample records from the model. The first ten records that the source provides will be returned after being enriched (if applicable). Synchronous requests must complete within 10s. If either querying or enrichment exceeds 10s, please use the async option.

        Parameters
        ----------
        id : str

        async_ : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ModelSampleResponseEnvelope
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
            await client.models.sample(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/models/{jsonable_encoder(id)}/sample",
            method="GET",
            params={"async": async_},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ModelSampleResponseEnvelope, _response.json())  # type: ignore
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
