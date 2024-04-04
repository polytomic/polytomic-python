# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .identity_function import IdentityFunction

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TargetField(pydantic.BaseModel):
    association: typing.Optional[bool] = None
    createable: typing.Optional[bool] = None
    description: typing.Optional[str] = None
    filterable: typing.Optional[bool] = None
    id: typing.Optional[str] = None
    identity_functions: typing.Optional[typing.List[IdentityFunction]] = None
    name: typing.Optional[str] = None
    required: typing.Optional[bool] = None
    source_type: typing.Optional[str] = None
    supports_identity: typing.Optional[bool] = None
    type: typing.Optional[str] = None
    updateable: typing.Optional[bool] = None

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
