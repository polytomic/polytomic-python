# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .mode import Mode
from .sync_destination_properties import SyncDestinationProperties
from .target_field import TargetField

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TargetResponse(pydantic.BaseModel):
    fields: typing.Optional[typing.List[TargetField]] = None
    id: typing.Optional[str] = None
    modes: typing.Optional[typing.List[Mode]] = None
    name: typing.Optional[str] = None
    properties: typing.Optional[SyncDestinationProperties] = None
    refreshed_at: typing.Optional[dt.datetime] = None

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
