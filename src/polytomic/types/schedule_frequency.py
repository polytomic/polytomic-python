# This file was auto-generated from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ScheduleFrequency(str, enum.Enum):
    MANUAL = "manual"
    CONTINUOUS = "continuous"
    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    CUSTOM = "custom"
    BUILDER = "builder"
    RUNAFTER = "runafter"
    MULTI = "multi"
    DBTCLOUD = "dbtcloud"

    def visit(
        self,
        manual: typing.Callable[[], T_Result],
        continuous: typing.Callable[[], T_Result],
        hourly: typing.Callable[[], T_Result],
        daily: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
        builder: typing.Callable[[], T_Result],
        runafter: typing.Callable[[], T_Result],
        multi: typing.Callable[[], T_Result],
        dbtcloud: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ScheduleFrequency.MANUAL:
            return manual()
        if self is ScheduleFrequency.CONTINUOUS:
            return continuous()
        if self is ScheduleFrequency.HOURLY:
            return hourly()
        if self is ScheduleFrequency.DAILY:
            return daily()
        if self is ScheduleFrequency.WEEKLY:
            return weekly()
        if self is ScheduleFrequency.CUSTOM:
            return custom()
        if self is ScheduleFrequency.BUILDER:
            return builder()
        if self is ScheduleFrequency.RUNAFTER:
            return runafter()
        if self is ScheduleFrequency.MULTI:
            return multi()
        if self is ScheduleFrequency.DBTCLOUD:
            return dbtcloud()
