# This file was auto-generated from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BulkExecutionStatus(str, enum.Enum):
    CREATED = "created"
    SCHEDULED = "scheduled"
    RUNNING = "running"
    EXPORTING = "exporting"
    CANCELING = "canceling"
    CANCELED = "canceled"
    COMPLETED = "completed"
    FAILED = "failed"
    PROCESSING = "processing"
    ERRORS = "errors"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        exporting: typing.Callable[[], T_Result],
        canceling: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        errors: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BulkExecutionStatus.CREATED:
            return created()
        if self is BulkExecutionStatus.SCHEDULED:
            return scheduled()
        if self is BulkExecutionStatus.RUNNING:
            return running()
        if self is BulkExecutionStatus.EXPORTING:
            return exporting()
        if self is BulkExecutionStatus.CANCELING:
            return canceling()
        if self is BulkExecutionStatus.CANCELED:
            return canceled()
        if self is BulkExecutionStatus.COMPLETED:
            return completed()
        if self is BulkExecutionStatus.FAILED:
            return failed()
        if self is BulkExecutionStatus.PROCESSING:
            return processing()
        if self is BulkExecutionStatus.ERRORS:
            return errors()
