# This file was auto-generated from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .schedule_frequency import ScheduleFrequency


class BulkSchedule(pydantic_v1.BaseModel):
    day_of_month: typing.Optional[str] = None
    day_of_week: typing.Optional[str] = None
    frequency: ScheduleFrequency
    hour: typing.Optional[str] = None
    minute: typing.Optional[str] = None
    month: typing.Optional[str] = None
    multi: typing.Optional[BulkMultiScheduleConfiguration] = None

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


from .bulk_multi_schedule_configuration import BulkMultiScheduleConfiguration  # noqa: E402

BulkSchedule.update_forward_refs()
