# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .connection_type_schema import ConnectionTypeSchema

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ConnectionResponseSchema(pydantic.BaseModel):
    api_calls_last_24_hours: typing.Optional[int] = pydantic.Field(default=None)
    """
    API calls made to service in the last 24h (supported integrations only).
    """

    configuration: typing.Optional[typing.Dict[str, typing.Any]] = None
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    organization_id: typing.Optional[str] = None
    policies: typing.Optional[typing.List[str]] = None
    status: typing.Optional[str] = None
    status_error: typing.Optional[str] = None
    type: typing.Optional[ConnectionTypeSchema] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
