# This file was auto-generated from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ExecutionStatus(str, enum.Enum):
    CREATED = "created"
    SCHEDULED = "scheduled"
    QUEUED = "queued"
    WAITING = "waiting"
    RUNNING = "running"
    PROCESSING = "processing"
    CANCELING = "canceling"
    CANCELED = "canceled"
    COMPLETED = "completed"
    FAILED = "failed"
    INTERRUPTED = "interrupted"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
        waiting: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        canceling: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        interrupted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExecutionStatus.CREATED:
            return created()
        if self is ExecutionStatus.SCHEDULED:
            return scheduled()
        if self is ExecutionStatus.QUEUED:
            return queued()
        if self is ExecutionStatus.WAITING:
            return waiting()
        if self is ExecutionStatus.RUNNING:
            return running()
        if self is ExecutionStatus.PROCESSING:
            return processing()
        if self is ExecutionStatus.CANCELING:
            return canceling()
        if self is ExecutionStatus.CANCELED:
            return canceled()
        if self is ExecutionStatus.COMPLETED:
            return completed()
        if self is ExecutionStatus.FAILED:
            return failed()
        if self is ExecutionStatus.INTERRUPTED:
            return interrupted()
