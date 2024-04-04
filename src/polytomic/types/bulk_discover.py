# This file was auto-generated from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BulkDiscover(str, enum.Enum):
    ALL = "all"
    ONLY_INCREMENTAL = "onlyIncremental"
    ONLY_NON_INCREMENTAL = "onlyNonIncremental"
    NONE = "none"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        only_incremental: typing.Callable[[], T_Result],
        only_non_incremental: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BulkDiscover.ALL:
            return all_()
        if self is BulkDiscover.ONLY_INCREMENTAL:
            return only_incremental()
        if self is BulkDiscover.ONLY_NON_INCREMENTAL:
            return only_non_incremental()
        if self is BulkDiscover.NONE:
            return none()
