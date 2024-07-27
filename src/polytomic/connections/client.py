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
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.connect_card_response_envelope import ConnectCardResponseEnvelope
from ..types.connection_list_response_envelope import ConnectionListResponseEnvelope
from ..types.connection_parameter_values_response_envelope import ConnectionParameterValuesResponseEnvelope
from ..types.connection_response_envelope import ConnectionResponseEnvelope
from ..types.connection_type_response_envelope import ConnectionTypeResponseEnvelope
from ..types.create_connection_response_envelope import CreateConnectionResponseEnvelope
from ..types.rest_err_response import RestErrResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ConnectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_types(self, *, request_options: typing.Optional[RequestOptions] = None) -> ConnectionTypeResponseEnvelope:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionTypeResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.connections.get_types()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/connection_types", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ConnectionTypeResponseEnvelope, _response.json())  # type: ignore
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

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ConnectionListResponseEnvelope:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionListResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.connections.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/connections", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ConnectionListResponseEnvelope, _response.json())  # type: ignore
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
        configuration: typing.Dict[str, typing.Any],
        name: str,
        type: str,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        validate: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateConnectionResponseEnvelope:
        """
        Parameters
        ----------
        configuration : typing.Dict[str, typing.Any]

        name : str

        type : str

        organization_id : typing.Optional[str]

        policies : typing.Optional[typing.Sequence[str]]

        redirect_url : typing.Optional[str]
            URL to redirect to after completing OAuth flow.

        validate : typing.Optional[bool]
            Validate connection configuration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateConnectionResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.connections.create(
            configuration={
                "database": "example",
                "hostname": "postgres.example.com",
                "password": "password",
                "port": 5432,
                "username": "user",
            },
            name="My Postgres Connection",
            type="postgresql",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/connections",
            method="POST",
            json={
                "configuration": configuration,
                "name": name,
                "organization_id": organization_id,
                "policies": policies,
                "redirect_url": redirect_url,
                "type": type,
                "validate": validate,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CreateConnectionResponseEnvelope, _response.json())  # type: ignore
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

    def connect(
        self,
        *,
        name: str,
        redirect_url: str,
        connection: typing.Optional[str] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        whitelist: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectCardResponseEnvelope:
        """
        Parameters
        ----------
        name : str

        redirect_url : str

        connection : typing.Optional[str]

        organization_id : typing.Optional[str]

        type : typing.Optional[str]

        whitelist : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectCardResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.connections.connect(
            name="Salesforce Connection",
            redirect_url="redirect_url",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/connections/connect/",
            method="POST",
            json={
                "connection": connection,
                "name": name,
                "organization_id": organization_id,
                "redirect_url": redirect_url,
                "type": type,
                "whitelist": whitelist,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ConnectCardResponseEnvelope, _response.json())  # type: ignore
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

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ConnectionResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.connections.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/connections/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ConnectionResponseEnvelope, _response.json())  # type: ignore
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
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        reconnect: typing.Optional[bool] = OMIT,
        type: typing.Optional[str] = OMIT,
        validate: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateConnectionResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        configuration : typing.Dict[str, typing.Any]

        name : str

        organization_id : typing.Optional[str]

        policies : typing.Optional[typing.Sequence[str]]

        reconnect : typing.Optional[bool]

        type : typing.Optional[str]

        validate : typing.Optional[bool]
            Validate connection configuration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateConnectionResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.connections.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            configuration={
                "database": "example",
                "hostname": "postgres.example.com",
                "password": "password",
                "port": 5432,
                "username": "user",
            },
            name="My Postgres Connection",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/connections/{jsonable_encoder(id)}",
            method="PUT",
            json={
                "configuration": configuration,
                "name": name,
                "organization_id": organization_id,
                "policies": policies,
                "reconnect": reconnect,
                "type": type,
                "validate": validate,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CreateConnectionResponseEnvelope, _response.json())  # type: ignore
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

    def remove(
        self, id: str, *, force: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        force : typing.Optional[bool]

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
        client.connections.remove(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            force=True,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/connections/{jsonable_encoder(id)}",
            method="DELETE",
            params={"force": force},
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

    def get_parameter_values(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionParameterValuesResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionParameterValuesResponseEnvelope
            OK

        Examples
        --------
        from polytomic.client import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.connections.get_parameter_values(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/connections/{jsonable_encoder(id)}/parameter_values", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ConnectionParameterValuesResponseEnvelope, _response.json())  # type: ignore
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


class AsyncConnectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionTypeResponseEnvelope:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionTypeResponseEnvelope
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
            await client.connections.get_types()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/connection_types", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ConnectionTypeResponseEnvelope, _response.json())  # type: ignore
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

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ConnectionListResponseEnvelope:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionListResponseEnvelope
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
            await client.connections.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/connections", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ConnectionListResponseEnvelope, _response.json())  # type: ignore
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
        configuration: typing.Dict[str, typing.Any],
        name: str,
        type: str,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        validate: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateConnectionResponseEnvelope:
        """
        Parameters
        ----------
        configuration : typing.Dict[str, typing.Any]

        name : str

        type : str

        organization_id : typing.Optional[str]

        policies : typing.Optional[typing.Sequence[str]]

        redirect_url : typing.Optional[str]
            URL to redirect to after completing OAuth flow.

        validate : typing.Optional[bool]
            Validate connection configuration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateConnectionResponseEnvelope
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
            await client.connections.create(
                configuration={
                    "database": "example",
                    "hostname": "postgres.example.com",
                    "password": "password",
                    "port": 5432,
                    "username": "user",
                },
                name="My Postgres Connection",
                type="postgresql",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/connections",
            method="POST",
            json={
                "configuration": configuration,
                "name": name,
                "organization_id": organization_id,
                "policies": policies,
                "redirect_url": redirect_url,
                "type": type,
                "validate": validate,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CreateConnectionResponseEnvelope, _response.json())  # type: ignore
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

    async def connect(
        self,
        *,
        name: str,
        redirect_url: str,
        connection: typing.Optional[str] = OMIT,
        organization_id: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        whitelist: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConnectCardResponseEnvelope:
        """
        Parameters
        ----------
        name : str

        redirect_url : str

        connection : typing.Optional[str]

        organization_id : typing.Optional[str]

        type : typing.Optional[str]

        whitelist : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectCardResponseEnvelope
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
            await client.connections.connect(
                name="Salesforce Connection",
                redirect_url="redirect_url",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/connections/connect/",
            method="POST",
            json={
                "connection": connection,
                "name": name,
                "organization_id": organization_id,
                "redirect_url": redirect_url,
                "type": type,
                "whitelist": whitelist,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ConnectCardResponseEnvelope, _response.json())  # type: ignore
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
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionResponseEnvelope
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
            await client.connections.get(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/connections/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ConnectionResponseEnvelope, _response.json())  # type: ignore
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
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        reconnect: typing.Optional[bool] = OMIT,
        type: typing.Optional[str] = OMIT,
        validate: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateConnectionResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        configuration : typing.Dict[str, typing.Any]

        name : str

        organization_id : typing.Optional[str]

        policies : typing.Optional[typing.Sequence[str]]

        reconnect : typing.Optional[bool]

        type : typing.Optional[str]

        validate : typing.Optional[bool]
            Validate connection configuration.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateConnectionResponseEnvelope
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
            await client.connections.update(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
                configuration={
                    "database": "example",
                    "hostname": "postgres.example.com",
                    "password": "password",
                    "port": 5432,
                    "username": "user",
                },
                name="My Postgres Connection",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/connections/{jsonable_encoder(id)}",
            method="PUT",
            json={
                "configuration": configuration,
                "name": name,
                "organization_id": organization_id,
                "policies": policies,
                "reconnect": reconnect,
                "type": type,
                "validate": validate,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(CreateConnectionResponseEnvelope, _response.json())  # type: ignore
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

    async def remove(
        self, id: str, *, force: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        force : typing.Optional[bool]

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
            await client.connections.remove(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
                force=True,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/connections/{jsonable_encoder(id)}",
            method="DELETE",
            params={"force": force},
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

    async def get_parameter_values(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionParameterValuesResponseEnvelope:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConnectionParameterValuesResponseEnvelope
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
            await client.connections.get_parameter_values(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/connections/{jsonable_encoder(id)}/parameter_values", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ConnectionParameterValuesResponseEnvelope, _response.json())  # type: ignore
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
