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
from ...types.connection_list_response_envelope import ConnectionListResponseEnvelope
from ...types.connection_parameter_values_response_envelope import ConnectionParameterValuesResponseEnvelope
from ...types.connection_response_envelope import ConnectionResponseEnvelope
from ...types.connection_type_response_envelope import ConnectionTypeResponseEnvelope
from ...types.create_connection_response_envelope import CreateConnectionResponseEnvelope
from ...types.get_connection_meta_envelope import GetConnectionMetaEnvelope
from ...types.model_field_response import ModelFieldResponse
from ...types.rest_err_response import RestErrResponse
from ...types.target_response_envelope import TargetResponseEnvelope

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ConnectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_types(self, *, request_options: typing.Optional[RequestOptions] = None) -> ConnectionTypeResponseEnvelope:
        """
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.connections.get_types()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/connection_types"),
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
            return pydantic.parse_obj_as(ConnectionTypeResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ConnectionListResponseEnvelope:
        """
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.connections.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/connections"),
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
            return pydantic.parse_obj_as(ConnectionListResponseEnvelope, _response.json())  # type: ignore
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
        configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        type: str,
        validate: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateConnectionResponseEnvelope:
        """
        Parameters:
            - configuration: typing.Optional[typing.Dict[str, typing.Any]].

            - name: str.

            - organization_id: typing.Optional[str].

            - policies: typing.Optional[typing.Sequence[str]].

            - redirect_url: typing.Optional[str]. URL to redirect to after completing OAuth flow.

            - type: str.

            - validate: typing.Optional[bool]. Validate connection configuration.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.connections.create(
            name="My Connection",
            redirect_url="https://example.com/oauth_redirect",
            type="s3",
            validate=True,
        )
        """
        _request: typing.Dict[str, typing.Any] = {"name": name, "type": type}
        if configuration is not OMIT:
            _request["configuration"] = configuration
        if organization_id is not OMIT:
            _request["organization_id"] = organization_id
        if policies is not OMIT:
            _request["policies"] = policies
        if redirect_url is not OMIT:
            _request["redirect_url"] = redirect_url
        if validate is not OMIT:
            _request["validate"] = validate
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/connections"),
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
            return pydantic.parse_obj_as(CreateConnectionResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def connect(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.connections.connect()
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/connections/connect"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
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
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ConnectionResponseEnvelope:
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
        client.connections.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}"),
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
            return pydantic.parse_obj_as(ConnectionResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def remove(
        self, id: str, *, force: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters:
            - id: str.

            - force: typing.Optional[bool].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.connections.remove(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            force=True,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "force": force,
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
        configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        reconnect: typing.Optional[bool] = OMIT,
        type: typing.Optional[str] = OMIT,
        validate: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateConnectionResponseEnvelope:
        """
        Parameters:
            - id: str.

            - configuration: typing.Optional[typing.Dict[str, typing.Any]].

            - name: str.

            - organization_id: typing.Optional[str].

            - policies: typing.Optional[typing.Sequence[str]].

            - reconnect: typing.Optional[bool].

            - type: typing.Optional[str].

            - validate: typing.Optional[bool]. Validate connection configuration.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.connections.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            name="My Connection",
            reconnect=False,
            type="s3",
            validate=True,
        )
        """
        _request: typing.Dict[str, typing.Any] = {"name": name}
        if configuration is not OMIT:
            _request["configuration"] = configuration
        if organization_id is not OMIT:
            _request["organization_id"] = organization_id
        if policies is not OMIT:
            _request["policies"] = policies
        if reconnect is not OMIT:
            _request["reconnect"] = reconnect
        if type is not OMIT:
            _request["type"] = type
        if validate is not OMIT:
            _request["validate"] = validate
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}"),
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
            return pydantic.parse_obj_as(CreateConnectionResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_parameter_values(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionParameterValuesResponseEnvelope:
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
        client.connections.get_parameter_values(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}/parameter_values"
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
            return pydantic.parse_obj_as(ConnectionParameterValuesResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_source(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetConnectionMetaEnvelope:
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
        client.connections.get_source(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}/source"
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
            return pydantic.parse_obj_as(GetConnectionMetaEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_source_fields(
        self,
        id: str,
        *,
        query: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelFieldResponse:
        """
        Parameters:
            - id: str.

            - query: typing.Optional[typing.Dict[str, typing.Any]].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.connections.get_source_fields(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if query is not OMIT:
            _request["query"] = query
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}/source/fields"
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
            return pydantic.parse_obj_as(ModelFieldResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_target(
        self,
        id: str,
        *,
        type: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectionMetaEnvelope:
        """
        Parameters:
            - id: str.

            - type: typing.Optional[str].

            - search: typing.Optional[str].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.connections.get_target(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            type="table",
            search="public.users",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}/target"
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
            return pydantic.parse_obj_as(GetConnectionMetaEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_target_fields(
        self,
        id: str,
        *,
        refresh: typing.Optional[bool] = OMIT,
        target: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TargetResponseEnvelope:
        """
        Parameters:
            - id: str.

            - refresh: typing.Optional[bool].

            - target: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import Polytomic

        client = Polytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        client.connections.get_target_fields(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            refresh=False,
            target="database.table",
        )
        """
        _request: typing.Dict[str, typing.Any] = {"target": target}
        if refresh is not OMIT:
            _request["refresh"] = refresh
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}/target/fields"
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
            return pydantic.parse_obj_as(TargetResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncConnectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionTypeResponseEnvelope:
        """
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.connections.get_types()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/connection_types"),
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
            return pydantic.parse_obj_as(ConnectionTypeResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ConnectionListResponseEnvelope:
        """
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.connections.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/connections"),
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
            return pydantic.parse_obj_as(ConnectionListResponseEnvelope, _response.json())  # type: ignore
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
        configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        redirect_url: typing.Optional[str] = OMIT,
        type: str,
        validate: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateConnectionResponseEnvelope:
        """
        Parameters:
            - configuration: typing.Optional[typing.Dict[str, typing.Any]].

            - name: str.

            - organization_id: typing.Optional[str].

            - policies: typing.Optional[typing.Sequence[str]].

            - redirect_url: typing.Optional[str]. URL to redirect to after completing OAuth flow.

            - type: str.

            - validate: typing.Optional[bool]. Validate connection configuration.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.connections.create(
            name="My Connection",
            redirect_url="https://example.com/oauth_redirect",
            type="s3",
            validate=True,
        )
        """
        _request: typing.Dict[str, typing.Any] = {"name": name, "type": type}
        if configuration is not OMIT:
            _request["configuration"] = configuration
        if organization_id is not OMIT:
            _request["organization_id"] = organization_id
        if policies is not OMIT:
            _request["policies"] = policies
        if redirect_url is not OMIT:
            _request["redirect_url"] = redirect_url
        if validate is not OMIT:
            _request["validate"] = validate
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/connections"),
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
            return pydantic.parse_obj_as(CreateConnectionResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def connect(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.connections.connect()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/connections/connect"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
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
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionResponseEnvelope:
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
        await client.connections.get(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}"),
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
            return pydantic.parse_obj_as(ConnectionResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def remove(
        self, id: str, *, force: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters:
            - id: str.

            - force: typing.Optional[bool].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.connections.remove(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            force=True,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "force": force,
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
        configuration: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        name: str,
        organization_id: typing.Optional[str] = OMIT,
        policies: typing.Optional[typing.Sequence[str]] = OMIT,
        reconnect: typing.Optional[bool] = OMIT,
        type: typing.Optional[str] = OMIT,
        validate: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateConnectionResponseEnvelope:
        """
        Parameters:
            - id: str.

            - configuration: typing.Optional[typing.Dict[str, typing.Any]].

            - name: str.

            - organization_id: typing.Optional[str].

            - policies: typing.Optional[typing.Sequence[str]].

            - reconnect: typing.Optional[bool].

            - type: typing.Optional[str].

            - validate: typing.Optional[bool]. Validate connection configuration.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.connections.update(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            name="My Connection",
            reconnect=False,
            type="s3",
            validate=True,
        )
        """
        _request: typing.Dict[str, typing.Any] = {"name": name}
        if configuration is not OMIT:
            _request["configuration"] = configuration
        if organization_id is not OMIT:
            _request["organization_id"] = organization_id
        if policies is not OMIT:
            _request["policies"] = policies
        if reconnect is not OMIT:
            _request["reconnect"] = reconnect
        if type is not OMIT:
            _request["type"] = type
        if validate is not OMIT:
            _request["validate"] = validate
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}"),
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
            return pydantic.parse_obj_as(CreateConnectionResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_parameter_values(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConnectionParameterValuesResponseEnvelope:
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
        await client.connections.get_parameter_values(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}/parameter_values"
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
            return pydantic.parse_obj_as(ConnectionParameterValuesResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_source(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetConnectionMetaEnvelope:
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
        await client.connections.get_source(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}/source"
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
            return pydantic.parse_obj_as(GetConnectionMetaEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_source_fields(
        self,
        id: str,
        *,
        query: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModelFieldResponse:
        """
        Parameters:
            - id: str.

            - query: typing.Optional[typing.Dict[str, typing.Any]].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.connections.get_source_fields(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if query is not OMIT:
            _request["query"] = query
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}/source/fields"
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
            return pydantic.parse_obj_as(ModelFieldResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_target(
        self,
        id: str,
        *,
        type: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetConnectionMetaEnvelope:
        """
        Parameters:
            - id: str.

            - type: typing.Optional[str].

            - search: typing.Optional[str].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.connections.get_target(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            type="table",
            search="public.users",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}/target"
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
            return pydantic.parse_obj_as(GetConnectionMetaEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_target_fields(
        self,
        id: str,
        *,
        refresh: typing.Optional[bool] = OMIT,
        target: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TargetResponseEnvelope:
        """
        Parameters:
            - id: str.

            - refresh: typing.Optional[bool].

            - target: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from polytomic.client import AsyncPolytomic

        client = AsyncPolytomic(
            x_polytomic_version="YOUR_X_POLYTOMIC_VERSION",
            token="YOUR_TOKEN",
        )
        await client.connections.get_target_fields(
            id="248df4b7-aa70-47b8-a036-33ac447e668d",
            refresh=False,
            target="database.table",
        )
        """
        _request: typing.Dict[str, typing.Any] = {"target": target}
        if refresh is not OMIT:
            _request["refresh"] = refresh
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/connections/{jsonable_encoder(id)}/target/fields"
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
            return pydantic.parse_obj_as(TargetResponseEnvelope, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(RestErrResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
