# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .run_after import RunAfter

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Schedule(pydantic.BaseModel):
    connection_id: typing.Optional[str] = None
    day_of_month: typing.Optional[str] = None
    day_of_week: typing.Optional[str] = None
    frequency: typing.Optional[str] = None
    hour: typing.Optional[str] = None
    job_id: typing.Optional[int] = None
    minute: typing.Optional[str] = None
    month: typing.Optional[str] = None
    run_after: typing.Optional[RunAfter] = None

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
