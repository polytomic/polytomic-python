# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .enrichment import Enrichment
from .model_model_field_request import ModelModelFieldRequest
from .model_relation import ModelRelation

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CreateModelRequest(pydantic.BaseModel):
    additional_fields: typing.Optional[typing.List[ModelModelFieldRequest]] = None
    configuration: typing.Optional[typing.Dict[str, typing.Any]] = None
    connection_id: str
    enricher: typing.Optional[Enrichment] = None
    fields: typing.Optional[typing.List[str]] = None
    identifier: typing.Optional[str] = None
    labels: typing.Optional[typing.List[str]] = None
    name: str
    organization_id: typing.Optional[str] = None
    policies: typing.Optional[typing.List[str]] = None
    relations: typing.Optional[typing.List[ModelRelation]] = None
    tracking_columns: typing.Optional[typing.List[str]] = None

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
