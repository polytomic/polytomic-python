# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .connection_parameter_value import ConnectionParameterValue
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ConnectionParameterValuesResp(UniversalBaseModel):
    allows_creation: typing.Optional[bool] = None
    values: typing.Optional[typing.List[ConnectionParameterValue]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
