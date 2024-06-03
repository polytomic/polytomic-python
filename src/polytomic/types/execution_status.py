# This file was auto-generated from our API Definition.

import typing

ExecutionStatus = typing.Union[
    typing.Literal[
        "created",
        "scheduled",
        "queued",
        "waiting",
        "running",
        "processing",
        "canceling",
        "canceled",
        "completed",
        "failed",
        "interrupted",
    ],
    typing.Any,
]
