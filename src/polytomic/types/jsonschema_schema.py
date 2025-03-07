# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .v_2_ordered_map_string_github_com_invopop_jsonschema_schema import (
    V2OrderedMapStringGithubComInvopopJsonschemaSchema,
)


class JsonschemaSchema(pydantic_v1.BaseModel):
    anchor: typing.Optional[str] = pydantic_v1.Field(alias="$anchor", default=None)
    comment: typing.Optional[str] = pydantic_v1.Field(alias="$comment", default=None)
    defs: typing.Optional[JsonschemaDefinitions] = pydantic_v1.Field(alias="$defs", default=None)
    dynamic_ref: typing.Optional[str] = pydantic_v1.Field(alias="$dynamicRef", default=None)
    id: typing.Optional[str] = pydantic_v1.Field(alias="$id", default=None)
    ref: typing.Optional[str] = pydantic_v1.Field(alias="$ref", default=None)
    schema_: typing.Optional[str] = pydantic_v1.Field(alias="$schema", default=None)
    additional_properties: typing.Optional[JsonschemaSchema] = pydantic_v1.Field(
        alias="additionalProperties", default=None
    )
    all_of: typing.Optional[typing.List[JsonschemaSchema]] = pydantic_v1.Field(alias="allOf", default=None)
    any_of: typing.Optional[typing.List[JsonschemaSchema]] = pydantic_v1.Field(alias="anyOf", default=None)
    const: typing.Optional[typing.Any] = None
    contains: typing.Optional[JsonschemaSchema] = None
    content_encoding: typing.Optional[str] = pydantic_v1.Field(alias="contentEncoding", default=None)
    content_media_type: typing.Optional[str] = pydantic_v1.Field(alias="contentMediaType", default=None)
    content_schema: typing.Optional[JsonschemaSchema] = pydantic_v1.Field(alias="contentSchema", default=None)
    default: typing.Optional[typing.Any] = None
    dependent_required: typing.Optional[typing.Dict[str, typing.List[str]]] = pydantic_v1.Field(
        alias="dependentRequired", default=None
    )
    dependent_schemas: typing.Optional[typing.Dict[str, JsonschemaSchema]] = pydantic_v1.Field(
        alias="dependentSchemas", default=None
    )
    deprecated: typing.Optional[bool] = None
    description: typing.Optional[str] = None
    else_: typing.Optional[JsonschemaSchema] = pydantic_v1.Field(alias="else", default=None)
    enum: typing.Optional[typing.List[typing.Any]] = None
    examples: typing.Optional[typing.List[typing.Any]] = None
    exclusive_maximum: typing.Optional[str] = pydantic_v1.Field(alias="exclusiveMaximum", default=None)
    exclusive_minimum: typing.Optional[str] = pydantic_v1.Field(alias="exclusiveMinimum", default=None)
    format: typing.Optional[str] = None
    if_: typing.Optional[JsonschemaSchema] = pydantic_v1.Field(alias="if", default=None)
    items: typing.Optional[JsonschemaSchema] = None
    max_contains: typing.Optional[int] = pydantic_v1.Field(alias="maxContains", default=None)
    max_items: typing.Optional[int] = pydantic_v1.Field(alias="maxItems", default=None)
    max_length: typing.Optional[int] = pydantic_v1.Field(alias="maxLength", default=None)
    max_properties: typing.Optional[int] = pydantic_v1.Field(alias="maxProperties", default=None)
    maximum: typing.Optional[str] = None
    min_contains: typing.Optional[int] = pydantic_v1.Field(alias="minContains", default=None)
    min_items: typing.Optional[int] = pydantic_v1.Field(alias="minItems", default=None)
    min_length: typing.Optional[int] = pydantic_v1.Field(alias="minLength", default=None)
    min_properties: typing.Optional[int] = pydantic_v1.Field(alias="minProperties", default=None)
    minimum: typing.Optional[str] = None
    multiple_of: typing.Optional[str] = pydantic_v1.Field(alias="multipleOf", default=None)
    not_: typing.Optional[JsonschemaSchema] = pydantic_v1.Field(alias="not", default=None)
    one_of: typing.Optional[typing.List[JsonschemaSchema]] = pydantic_v1.Field(alias="oneOf", default=None)
    pattern: typing.Optional[str] = None
    pattern_properties: typing.Optional[typing.Dict[str, JsonschemaSchema]] = pydantic_v1.Field(
        alias="patternProperties", default=None
    )
    prefix_items: typing.Optional[typing.List[JsonschemaSchema]] = pydantic_v1.Field(alias="prefixItems", default=None)
    properties: typing.Optional[V2OrderedMapStringGithubComInvopopJsonschemaSchema] = None
    property_names: typing.Optional[JsonschemaSchema] = pydantic_v1.Field(alias="propertyNames", default=None)
    read_only: typing.Optional[bool] = pydantic_v1.Field(alias="readOnly", default=None)
    required: typing.Optional[typing.List[str]] = None
    then: typing.Optional[JsonschemaSchema] = None
    title: typing.Optional[str] = None
    type: typing.Optional[str] = None
    unique_items: typing.Optional[bool] = pydantic_v1.Field(alias="uniqueItems", default=None)
    write_only: typing.Optional[bool] = pydantic_v1.Field(alias="writeOnly", default=None)

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


from .jsonschema_definitions import JsonschemaDefinitions  # noqa: E402

JsonschemaSchema.update_forward_refs()
