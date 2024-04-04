# This file was auto-generated from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WorkTaskStatus(str, enum.Enum):
    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        done: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkTaskStatus.RUNNING:
            return running()
        if self is WorkTaskStatus.DONE:
            return done()
        if self is WorkTaskStatus.FAILED:
            return failed()
