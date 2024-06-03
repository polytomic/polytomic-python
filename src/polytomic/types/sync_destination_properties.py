# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class SyncDestinationProperties(pydantic_v1.BaseModel):
    does_not_report_operation_counts: typing.Optional[bool] = None
    new_target_label: typing.Optional[str] = None
    optional_target_mappings: typing.Optional[bool] = None
    primary_metadata_object: typing.Optional[str] = None
    requires_configuration: typing.Optional[bool] = None
    supports_field_creation: typing.Optional[bool] = None
    supports_field_type_selection: typing.Optional[bool] = None
    supports_target_filters: typing.Optional[bool] = None
    target_creator: typing.Optional[bool] = None
    use_field_names_as_labels: typing.Optional[bool] = None

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
