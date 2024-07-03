# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .execution_status import ExecutionStatus


class SyncCompletedEvent(pydantic_v1.BaseModel):
    deleted_records: typing.Optional[typing.List[str]] = None
    error_count: typing.Optional[int] = None
    errored_records: typing.Optional[typing.List[str]] = None
    execution_id: typing.Optional[str] = None
    inserted_count: typing.Optional[int] = None
    inserted_records: typing.Optional[typing.List[str]] = None
    name: typing.Optional[str] = None
    organization_id: typing.Optional[str] = None
    record_count: typing.Optional[int] = None
    status: typing.Optional[ExecutionStatus] = None
    sync_id: typing.Optional[str] = None
    target_connection_id: typing.Optional[str] = None
    total_records: typing.Optional[typing.List[str]] = None
    trigger: typing.Optional[str] = None
    updated_count: typing.Optional[int] = None
    updated_records: typing.Optional[typing.List[str]] = None
    upserted_count: typing.Optional[int] = None
    warning_count: typing.Optional[int] = None
    warnings: typing.Optional[typing.List[str]] = None

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
