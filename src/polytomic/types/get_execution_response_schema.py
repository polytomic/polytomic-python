# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .execution_counts import ExecutionCounts
from .execution_status import ExecutionStatus

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class GetExecutionResponseSchema(pydantic.BaseModel):
    completed_at: typing.Optional[dt.datetime] = None
    counts: typing.Optional[ExecutionCounts] = None
    created_at: typing.Optional[dt.datetime] = None
    errors: typing.Optional[typing.List[str]] = None
    id: typing.Optional[str] = None
    started_at: typing.Optional[dt.datetime] = None
    status: typing.Optional[ExecutionStatus] = None
    type: typing.Optional[str] = None

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
