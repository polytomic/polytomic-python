# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .model_field import ModelField
from .v_2_enricher_configuration import V2EnricherConfiguration
from .v_2_enricher_mapping import V2EnricherMapping

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Enrichment(pydantic.BaseModel):
    configuration: typing.Optional[V2EnricherConfiguration] = None
    connection_id: typing.Optional[str] = None
    enricher_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Must be provided to update an existing enrichment
    """

    fields: typing.Optional[typing.List[ModelField]] = pydantic.Field(default=None)
    """
    If not provided, all fields will be enabled.
    """

    mappings: typing.Optional[V2EnricherMapping] = None

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
