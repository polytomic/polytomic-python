# This file was auto-generated from our API Definition.

import typing

from .bulk_sync_canceled_event import BulkSyncCanceledEvent
from .bulk_sync_completed_event import BulkSyncCompletedEvent
from .bulk_sync_completed_with_error_event import BulkSyncCompletedWithErrorEvent
from .bulk_sync_failed_event import BulkSyncFailedEvent
from .bulk_sync_running_event import BulkSyncRunningEvent
from .sync_canceled_event import SyncCanceledEvent
from .sync_completed_event import SyncCompletedEvent
from .sync_completed_with_errors_event import SyncCompletedWithErrorsEvent
from .sync_failed_event import SyncFailedEvent
from .sync_running_event import SyncRunningEvent

EventBody = typing.Union[
    SyncRunningEvent,
    SyncCompletedEvent,
    SyncFailedEvent,
    SyncCanceledEvent,
    SyncCompletedWithErrorsEvent,
    BulkSyncRunningEvent,
    BulkSyncCompletedEvent,
    BulkSyncCanceledEvent,
    BulkSyncCompletedWithErrorEvent,
    BulkSyncFailedEvent,
]
