# This file was auto-generated from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BulkSelectiveMode(str, enum.Enum):
    NONE = "none"
    INCREMENTAL_FIELDS = "incrementalFields"
    NONINCREMENTAL_FIELDS = "nonincrementalFields"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        incremental_fields: typing.Callable[[], T_Result],
        nonincremental_fields: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BulkSelectiveMode.NONE:
            return none()
        if self is BulkSelectiveMode.INCREMENTAL_FIELDS:
            return incremental_fields()
        if self is BulkSelectiveMode.NONINCREMENTAL_FIELDS:
            return nonincremental_fields()
