# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.organizations_envelope import OrganizationsEnvelope
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unauthorized_error import UnauthorizedError
from ..types.rest_err_response import RestErrResponse
from ..errors.internal_server_error import InternalServerError
from ..types.api_error import ApiError as types_api_error_ApiError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError as core_api_error_ApiError
from ..types.organization_envelope import OrganizationEnvelope
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..core.jsonable_encoder import jsonable_encoder
from ..errors.not_found_error import NotFoundError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class OrganizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> OrganizationsEnvelope:
        """
        > 🚧 Requires partner key
        >
        > Organization endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationsEnvelope
            OK

        Examples
        --------
        from polytomic import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.organization.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/organizations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    OrganizationsEnvelope,
                    parse_obj_as(
                        type_=OrganizationsEnvelope,  # type: ignore
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

    def create(
        self,
        *,
        name: str,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        issuer: typing.Optional[str] = OMIT,
        sso_domain: typing.Optional[str] = OMIT,
        sso_org_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationEnvelope:
        """
        > 🚧 Requires partner key
        >
        > Organization endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).

        Parameters
        ----------
        name : str

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        issuer : typing.Optional[str]

        sso_domain : typing.Optional[str]

        sso_org_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationEnvelope
            OK

        Examples
        --------
        from polytomic import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.organization.create(
            name="My Organization",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/organizations",
            method="POST",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "issuer": issuer,
                "name": name,
                "sso_domain": sso_domain,
                "sso_org_id": sso_org_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    OrganizationEnvelope,
                    parse_obj_as(
                        type_=OrganizationEnvelope,  # type: ignore
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> OrganizationEnvelope:
        """
        > 🚧 Requires partner key
        >
        > Organization endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationEnvelope
            OK

        Examples
        --------
        from polytomic import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.organization.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/organizations/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    OrganizationEnvelope,
                    parse_obj_as(
                        type_=OrganizationEnvelope,  # type: ignore
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

    def update(
        self,
        id: str,
        *,
        name: str,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        issuer: typing.Optional[str] = OMIT,
        sso_domain: typing.Optional[str] = OMIT,
        sso_org_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationEnvelope:
        """
        > 🚧 Requires partner key
        >
        > Organization endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).

        Parameters
        ----------
        id : str

        name : str

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        issuer : typing.Optional[str]

        sso_domain : typing.Optional[str]

        sso_org_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationEnvelope
            OK

        Examples
        --------
        from polytomic import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.organization.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            name="My Organization",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/organizations/{jsonable_encoder(id)}",
            method="PUT",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "issuer": issuer,
                "name": name,
                "sso_domain": sso_domain,
                "sso_org_id": sso_org_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    OrganizationEnvelope,
                    parse_obj_as(
                        type_=OrganizationEnvelope,  # type: ignore
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def remove(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        > 🚧 Requires partner key
        >
        > Organization endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).

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
        from polytomic import Polytomic

        client = Polytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )
        client.organization.remove(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/organizations/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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


class AsyncOrganizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> OrganizationsEnvelope:
        """
        > 🚧 Requires partner key
        >
        > Organization endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationsEnvelope
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
            await client.organization.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/organizations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    OrganizationsEnvelope,
                    parse_obj_as(
                        type_=OrganizationsEnvelope,  # type: ignore
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

    async def create(
        self,
        *,
        name: str,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        issuer: typing.Optional[str] = OMIT,
        sso_domain: typing.Optional[str] = OMIT,
        sso_org_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationEnvelope:
        """
        > 🚧 Requires partner key
        >
        > Organization endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).

        Parameters
        ----------
        name : str

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        issuer : typing.Optional[str]

        sso_domain : typing.Optional[str]

        sso_org_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationEnvelope
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
            await client.organization.create(
                name="My Organization",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/organizations",
            method="POST",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "issuer": issuer,
                "name": name,
                "sso_domain": sso_domain,
                "sso_org_id": sso_org_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    OrganizationEnvelope,
                    parse_obj_as(
                        type_=OrganizationEnvelope,  # type: ignore
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> OrganizationEnvelope:
        """
        > 🚧 Requires partner key
        >
        > Organization endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationEnvelope
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
            await client.organization.get(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/organizations/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    OrganizationEnvelope,
                    parse_obj_as(
                        type_=OrganizationEnvelope,  # type: ignore
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

    async def update(
        self,
        id: str,
        *,
        name: str,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        issuer: typing.Optional[str] = OMIT,
        sso_domain: typing.Optional[str] = OMIT,
        sso_org_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationEnvelope:
        """
        > 🚧 Requires partner key
        >
        > Organization endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).

        Parameters
        ----------
        id : str

        name : str

        client_id : typing.Optional[str]

        client_secret : typing.Optional[str]

        issuer : typing.Optional[str]

        sso_domain : typing.Optional[str]

        sso_org_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationEnvelope
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
            await client.organization.update(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
                name="My Organization",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/organizations/{jsonable_encoder(id)}",
            method="PUT",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "issuer": issuer,
                "name": name,
                "sso_domain": sso_domain,
                "sso_org_id": sso_org_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    OrganizationEnvelope,
                    parse_obj_as(
                        type_=OrganizationEnvelope,  # type: ignore
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def remove(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        > 🚧 Requires partner key
        >
        > Organization endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).

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
        import asyncio

        from polytomic import AsyncPolytomic

        client = AsyncPolytomic(
            version="YOUR_VERSION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organization.remove(
                id="248df4b7-aa70-47b8-a036-33ac447e668d",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/organizations/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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
