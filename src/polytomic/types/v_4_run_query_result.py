# This file was auto-generated from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .work_task_status import WorkTaskStatus


class V4RunQueryResult(pydantic_v1.BaseModel):
    count: typing.Optional[int] = pydantic_v1.Field(default=None)
    """
    The number of rows returned by the query. This will not be returned until the query completes.
    """

    error: typing.Optional[str] = None
    expires: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The time at which the query will expire and be deleted. This will not be returned until the query completes.
    """

    fields: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    The names of the fields returned by the query. This will not be returned until the query completes.
    """

    id: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The ID of the query task.
    """

    results: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic_v1.Field(default=None)
    """
    The query results, returned as an array of objects.
    """

    status: typing.Optional[WorkTaskStatus] = None

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
