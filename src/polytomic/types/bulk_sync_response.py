# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .bulk_schedule import BulkSchedule

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BulkSyncResponse(pydantic.BaseModel):
    active: typing.Optional[bool] = None
    destination_configuration: typing.Optional[typing.Dict[str, typing.Any]] = None
    destination_connection_id: typing.Optional[str] = None
    discover: typing.Optional[bool] = None
    id: typing.Optional[str] = None
    mode: typing.Optional[str] = None
    name: typing.Optional[str] = None
    organization_id: typing.Optional[str] = None
    policies: typing.Optional[typing.List[str]] = None
    schedule: typing.Optional[BulkSchedule] = None
    source_configuration: typing.Optional[typing.Dict[str, typing.Any]] = None
    source_connection_id: typing.Optional[str] = None

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
