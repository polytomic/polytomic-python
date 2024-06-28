# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .bulk_filter import BulkFilter
from .v_2_schema_configuration_fields_item import V2SchemaConfigurationFieldsItem


class SchemaConfiguration(pydantic_v1.BaseModel):
    enabled: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Whether the schema is enabled for syncing.
    """

    fields: typing.Optional[typing.List[V2SchemaConfigurationFieldsItem]] = None
    filters: typing.Optional[typing.List[BulkFilter]] = None
    id: typing.Optional[str] = None
    partition_key: typing.Optional[str] = pydantic_v1.Field(alias="partitionKey", default=None)
    tracking_field: typing.Optional[str] = pydantic_v1.Field(alias="trackingField", default=None)

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
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
