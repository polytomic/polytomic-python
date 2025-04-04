# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .sync_mode import SyncMode
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SupportedMode(UniversalBaseModel):
    id: typing.Optional[SyncMode] = None
    requires_identity: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the sync mode requires an identity field mapping.
    """

    supports_per_field_mode: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the target supports per-field sync modes.
    """

    supports_target_filters: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if the sync mode supports target filters.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
