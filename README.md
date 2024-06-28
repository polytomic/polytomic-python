# Polytomic Python Library

[![pypi](https://img.shields.io/pypi/v/polytomic)](https://pypi.python.org/pypi/polytomic)

The Polytomic Python library provides convenient access to the Polytomic API from Python.

## Installation

```sh
pip install polytomic
```

## Usage

Instantiate and use the client with the following:

```python
from polytomic import BulkSchedule
from polytomic.client import Polytomic

client = Polytomic(
    token="YOUR_TOKEN",
)
client.bulk_sync.create(
    destination_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    mode="replicate",
    name="My Bulk Sync",
    schedule=BulkSchedule(
        frequency="manual",
    ),
    source_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
from polytomic import BulkSchedule
from polytomic.client import AsyncPolytomic

client = AsyncPolytomic(
    token="YOUR_TOKEN",
)
await client.bulk_sync.create(
    destination_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    mode="replicate",
    name="My Bulk Sync",
    schedule=BulkSchedule(
        frequency="manual",
    ),
    source_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
