# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .bulk_schedule import BulkSchedule


class BulkSyncResponse(pydantic_v1.BaseModel):
    active: typing.Optional[bool] = None
    destination_configuration: typing.Optional[typing.Dict[str, typing.Any]] = pydantic_v1.Field(default=None)
    """
    Destination-specific bulk sync configuration. e.g. output schema name, s3 file format, etc.
    """

    destination_connection_id: typing.Optional[str] = None
    discover: typing.Optional[bool] = None
    id: typing.Optional[str] = None
    mode: typing.Optional[str] = None
    name: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Name of the bulk sync
    """

    organization_id: typing.Optional[str] = None
    policies: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    List of permissions policies applied to the bulk sync.
    """

    schedule: typing.Optional[BulkSchedule] = None
    source_configuration: typing.Optional[typing.Dict[str, typing.Any]] = pydantic_v1.Field(default=None)
    """
    Source-specific bulk sync configuration. e.g. replication slot name, sync lookback, etc.
    """

    source_connection_id: typing.Optional[str] = None

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
