# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .execution_status import ExecutionStatus
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class SyncCompletedEvent(UniversalBaseModel):
    deleted_records: typing.Optional[typing.List[str]] = None
    error_count: typing.Optional[int] = None
    errored_records: typing.Optional[typing.List[str]] = None
    execution_id: typing.Optional[str] = None
    inserted_count: typing.Optional[int] = None
    inserted_records: typing.Optional[typing.List[str]] = None
    organization_id: typing.Optional[str] = None
    record_count: typing.Optional[int] = None
    status: typing.Optional[ExecutionStatus] = None
    sync_id: typing.Optional[str] = None
    sync_name: typing.Optional[str] = None
    target_connection_id: typing.Optional[str] = None
    total_records: typing.Optional[typing.List[str]] = None
    trigger: typing.Optional[str] = None
    updated_count: typing.Optional[int] = None
    updated_records: typing.Optional[typing.List[str]] = None
    upserted_count: typing.Optional[int] = None
    warning_count: typing.Optional[int] = None
    warnings: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
