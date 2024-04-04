# This file was auto-generated from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .bulk_selective_mode import BulkSelectiveMode

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BulkItemizedSchedule(pydantic.BaseModel):
    item: BulkSelectiveMode
    schedule: BulkSchedule

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


from .bulk_schedule import BulkSchedule  # noqa: E402

BulkItemizedSchedule.update_forward_refs()
