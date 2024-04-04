# This file was auto-generated from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BulkSchemaExecutionStatus(str, enum.Enum):
    CREATED = "created"
    SCHEDULED = "scheduled"
    RUNNING = "running"
    EXPORTING = "exporting"
    CANCELED = "canceled"
    COMPLETED = "completed"
    FAILED = "failed"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        exporting: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BulkSchemaExecutionStatus.CREATED:
            return created()
        if self is BulkSchemaExecutionStatus.SCHEDULED:
            return scheduled()
        if self is BulkSchemaExecutionStatus.RUNNING:
            return running()
        if self is BulkSchemaExecutionStatus.EXPORTING:
            return exporting()
        if self is BulkSchemaExecutionStatus.CANCELED:
            return canceled()
        if self is BulkSchemaExecutionStatus.COMPLETED:
            return completed()
        if self is BulkSchemaExecutionStatus.FAILED:
            return failed()
