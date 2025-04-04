# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
from .bulk_field import BulkField
from .bulk_filter import BulkFilter
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class BulkSchema(UniversalBaseModel):
    data_cutoff_timestamp: typing.Optional[dt.datetime] = None
    disable_data_cutoff: typing.Optional[bool] = None
    enabled: typing.Optional[bool] = None
    fields: typing.Optional[typing.List[BulkField]] = None
    filters: typing.Optional[typing.List[BulkFilter]] = None
    id: typing.Optional[str] = None
    output_name: typing.Optional[str] = None
    partition_key: typing.Optional[str] = None
    tracking_field: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
