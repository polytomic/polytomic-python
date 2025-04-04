# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class BulkSyncCompletedEvent(UniversalBaseModel):
    destination_connection_id: typing.Optional[str] = None
    execution_id: typing.Optional[str] = None
    organization_id: typing.Optional[str] = None
    source_connection_id: typing.Optional[str] = None
    sync_id: typing.Optional[str] = None
    sync_name: typing.Optional[str] = None
    trigger_source: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
