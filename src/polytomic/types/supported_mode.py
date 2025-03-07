# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .sync_mode import SyncMode


class SupportedMode(pydantic_v1.BaseModel):
    id: typing.Optional[SyncMode] = None
    requires_identity: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    True if the sync mode requires an identity field mapping.
    """

    supports_per_field_mode: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    True if the target supports per-field sync modes.
    """

    supports_target_filters: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    True if the sync mode supports target filters.
    """

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
