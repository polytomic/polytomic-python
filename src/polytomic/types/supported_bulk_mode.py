# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .sync_mode import SyncMode
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class SupportedBulkMode(UniversalBaseModel):
    description: typing.Optional[str] = None
    id: typing.Optional[SyncMode] = None
    label: typing.Optional[str] = None
    requires_identity: typing.Optional[bool] = None
    supports_field_sync_mode: typing.Optional[bool] = None
    supports_target_filters: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
