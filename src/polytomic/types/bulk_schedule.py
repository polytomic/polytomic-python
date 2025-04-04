# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .schedule_frequency import ScheduleFrequency
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ..core.pydantic_utilities import update_forward_refs


class BulkSchedule(UniversalBaseModel):
    day_of_month: typing.Optional[str] = None
    day_of_week: typing.Optional[str] = None
    frequency: ScheduleFrequency
    hour: typing.Optional[str] = None
    minute: typing.Optional[str] = None
    month: typing.Optional[str] = None
    multi: typing.Optional["BulkMultiScheduleConfiguration"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .bulk_itemized_schedule import BulkItemizedSchedule  # noqa: E402
from .bulk_multi_schedule_configuration import BulkMultiScheduleConfiguration  # noqa: E402

update_forward_refs(BulkSchedule)
