# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .enrichment import Enrichment
from .label_label import LabelLabel
from .model_field import ModelField
from .relation import Relation

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ModelResponse(pydantic.BaseModel):
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
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
