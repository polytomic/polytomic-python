# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
from .v_2_ordered_map_string_github_com_invopop_jsonschema_schema import (
    V2OrderedMapStringGithubComInvopopJsonschemaSchema,
)
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ..core.pydantic_utilities import update_forward_refs


class JsonschemaSchema(UniversalBaseModel):
    anchor: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="$anchor")] = None
    comment: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="$comment")] = None
    defs: typing_extensions.Annotated[typing.Optional["JsonschemaDefinitions"], FieldMetadata(alias="$defs")] = None
    dynamic_ref: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="$dynamicRef")] = None
    id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="$id")] = None
    ref: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="$ref")] = None
    schema_: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="$schema")] = None
    additional_properties: typing_extensions.Annotated[
        typing.Optional["JsonschemaSchema"], FieldMetadata(alias="additionalProperties")
    ] = None
    all_of: typing_extensions.Annotated[
        typing.Optional[typing.List["JsonschemaSchema"]], FieldMetadata(alias="allOf")
    ] = None
    any_of: typing_extensions.Annotated[
        typing.Optional[typing.List["JsonschemaSchema"]], FieldMetadata(alias="anyOf")
    ] = None
    const: typing.Optional[typing.Optional[typing.Any]] = None
    contains: typing.Optional["JsonschemaSchema"] = None
    content_encoding: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="contentEncoding")] = None
    content_media_type: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="contentMediaType")] = (
        None
    )
    content_schema: typing_extensions.Annotated[
        typing.Optional["JsonschemaSchema"], FieldMetadata(alias="contentSchema")
    ] = None
    default: typing.Optional[typing.Optional[typing.Any]] = None
    dependent_required: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.List[str]]], FieldMetadata(alias="dependentRequired")
    ] = None
    dependent_schemas: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, "JsonschemaSchema"]], FieldMetadata(alias="dependentSchemas")
    ] = None
    deprecated: typing.Optional[bool] = None
    description: typing.Optional[str] = None
    else_: typing_extensions.Annotated[typing.Optional["JsonschemaSchema"], FieldMetadata(alias="else")] = None
    enum: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    examples: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    exclusive_maximum: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="exclusiveMaximum")] = None
    exclusive_minimum: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="exclusiveMinimum")] = None
    format: typing.Optional[str] = None
    if_: typing_extensions.Annotated[typing.Optional["JsonschemaSchema"], FieldMetadata(alias="if")] = None
    items: typing.Optional["JsonschemaSchema"] = None
    max_contains: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="maxContains")] = None
    max_items: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="maxItems")] = None
    max_length: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="maxLength")] = None
    max_properties: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="maxProperties")] = None
    maximum: typing.Optional[str] = None
    min_contains: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="minContains")] = None
    min_items: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="minItems")] = None
    min_length: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="minLength")] = None
    min_properties: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="minProperties")] = None
    minimum: typing.Optional[str] = None
    multiple_of: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="multipleOf")] = None
    not_: typing_extensions.Annotated[typing.Optional["JsonschemaSchema"], FieldMetadata(alias="not")] = None
    one_of: typing_extensions.Annotated[
        typing.Optional[typing.List["JsonschemaSchema"]], FieldMetadata(alias="oneOf")
    ] = None
    pattern: typing.Optional[str] = None
    pattern_properties: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, "JsonschemaSchema"]], FieldMetadata(alias="patternProperties")
    ] = None
    prefix_items: typing_extensions.Annotated[
        typing.Optional[typing.List["JsonschemaSchema"]], FieldMetadata(alias="prefixItems")
    ] = None
    properties: typing.Optional[V2OrderedMapStringGithubComInvopopJsonschemaSchema] = None
    property_names: typing_extensions.Annotated[
        typing.Optional["JsonschemaSchema"], FieldMetadata(alias="propertyNames")
    ] = None
    read_only: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="readOnly")] = None
    required: typing.Optional[typing.List[str]] = None
    then: typing.Optional["JsonschemaSchema"] = None
    title: typing.Optional[str] = None
    type: typing.Optional[str] = None
    unique_items: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="uniqueItems")] = None
    write_only: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="writeOnly")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .jsonschema_definitions import JsonschemaDefinitions  # noqa: E402

update_forward_refs(JsonschemaSchema)
