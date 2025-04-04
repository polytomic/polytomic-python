# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .v_2_enricher_configuration import V2EnricherConfiguration
import pydantic
from .model_field import ModelField
from .v_2_enricher_mapping import V2EnricherMapping
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Enrichment(UniversalBaseModel):
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
