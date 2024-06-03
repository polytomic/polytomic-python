# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .enrichment import Enrichment
from .label_label import LabelLabel
from .model_field import ModelField
from .relation import Relation


class ModelResponse(pydantic_v1.BaseModel):
    configuration: typing.Optional[typing.Dict[str, typing.Any]] = None
    connection_id: typing.Optional[str] = None
    enricher: typing.Optional[Enrichment] = None
    fields: typing.Optional[typing.List[ModelField]] = None
    id: typing.Optional[str] = None
    identifier: typing.Optional[str] = None
    labels: typing.Optional[typing.List[LabelLabel]] = None
    name: typing.Optional[str] = None
    organization_id: typing.Optional[str] = None
    policies: typing.Optional[typing.List[str]] = None
    relations: typing.Optional[typing.List[Relation]] = None
    tracking_columns: typing.Optional[typing.List[str]] = None
    type: typing.Optional[str] = None
    version: typing.Optional[int] = None

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
