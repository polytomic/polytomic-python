# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .run_after import RunAfter
from .schedule_frequency import ScheduleFrequency


class Schedule(pydantic_v1.BaseModel):
    connection_id: typing.Optional[str] = None
    day_of_month: typing.Optional[str] = None
    day_of_week: typing.Optional[str] = None
    frequency: typing.Optional[ScheduleFrequency] = None
    hour: typing.Optional[str] = None
    job_id: typing.Optional[int] = None
    minute: typing.Optional[str] = None
    month: typing.Optional[str] = None
    run_after: typing.Optional[RunAfter] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
