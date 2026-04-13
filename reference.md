# Reference
## BulkSync
<details><summary><code>client.bulk_sync.<a href="src/polytomic/bulk_sync/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists bulk syncs in the caller's organization.

Results are returned as a single `data` array. This version of the endpoint
supports the `active` filter but does not support cursor pagination, `limit`,
or `page_token` query parameters.

If you need a cursor-paginated bulk sync list, use API version `2025-09-18` or
later.

> 📘 To retrieve a specific sync, use
> [`GET /api/bulk/syncs/{id}`](../../../api-reference/bulk-sync/get)
> instead of filtering the list client-side.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.list(
    active=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Filter to only active (true) or only paused (false) syncs. Omit to return both.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.<a href="src/polytomic/bulk_sync/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new bulk sync from a source connection to a destination connection.

Bulk syncs are used for the ELT pattern (Extract, Load, and Transform), where you want to sync un-transformed data to your data warehouses, databases, or cloud storage buckets like S3.

All of the functionality described in [the product
documentation](https://docs.polytomic.com/docs/bulk-syncs) is configurable via
the API.

Sample code examples:

- [Bulk sync (ELT) from Salesforce to S3](../../../guides/code-examples/bulk-sync-elt-from-salesforce-to-s-3)
- [Bulk sync (ELT) from Salesforce to Snowflake](../../../guides/code-examples/bulk-sync-elt-from-salesforce-to-snowflake)
- [Bulk sync (ELT) from HubSpot to PostgreSQL](../../../guides/code-examples/bulk-sync-elt-from-hub-spot-to-postgre-sql)

## Connection specific configuration

The `destination_configuration` is integration-specific configuration for the
selected bulk sync destination. This includes settings such as the output schema
and is required when creating a new sync.

The `source_configuration` is optional. It allows configuration for how
Polytomic reads data from the source connection. This will not be available for
integrations that do not support additional configuration.

Consult the [connection configurations](../../../guides/configuring-your-connections/overview)
to see configurations for particular integrations (for example, [here](../../../guides/configuring-your-connections/connections/postgre-sql#source-1) is the available source configuration for the PostgreSQL bulk sync source).

## Defaults and selection behavior

If `schemas` is omitted, the sync is created with all available source schemas
selected. Pass `schemas` explicitly if you want the initial sync to include
only a subset of tables or objects.

Schedule times are interpreted in UTC.

When omitted, automatic discovery defaults are conservative:

- `automatically_add_new_objects` defaults to not enabling newly discovered
  source objects automatically.
- `automatically_add_new_fields` defaults to enabling newly discovered fields
  on already selected objects.
- `normalize_names` defaults to enabled.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import BulkSchedule, Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.create(
    destination_configuration={"schema": "my_schema"},
    destination_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    name="My Bulk Sync",
    schedule=BulkSchedule(
        frequency="manual",
    ),
    source_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**destination_configuration:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**destination_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `BulkSchedule` 
    
</dd>
</dl>

<dl>
<dd>

**source_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**automatically_add_new_fields:** `typing.Optional[BulkDiscover]` 
    
</dd>
</dl>

<dl>
<dd>

**automatically_add_new_objects:** `typing.Optional[BulkDiscover]` 
    
</dd>
</dl>

<dl>
<dd>

**concurrency_limit:** `typing.Optional[int]` — Override the default concurrency limit for this sync.
    
</dd>
</dl>

<dl>
<dd>

**data_cutoff_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**disable_record_timestamps:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**discover:** `typing.Optional[bool]` — DEPRECATED: Use automatically_add_new_objects/automatically_add_new_fields instead
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[BulkSyncMode]` 
    
</dd>
</dl>

<dl>
<dd>

**normalize_names:** `typing.Optional[BulkNormalizeNames]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**policies:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**resync_concurrency_limit:** `typing.Optional[int]` — Override the default resync concurrency limit for this sync.
    
</dd>
</dl>

<dl>
<dd>

**schemas:** `typing.Optional[typing.Sequence[V2CreateBulkSyncRequestSchemasItem]]` — List of schemas to sync; if omitted, all schemas will be selected for syncing.
    
</dd>
</dl>

<dl>
<dd>

**source_configuration:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.<a href="src/polytomic/bulk_sync/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single bulk sync by ID.

The response includes the sync's top-level configuration — source, destination,
schedules, and discovery settings.

- To check whether the sync is running and see the most-recent execution result,
  use [`GET /api/bulk/syncs/{id}/status`](../../../../api-reference/bulk-sync/get-status).
- To inspect which schemas are selected and how they are configured, use
  [`GET /api/bulk/syncs/{id}/schemas`](../../../../api-reference/bulk-sync/schemas/list).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.get(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    refresh_schemas=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**refresh_schemas:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.<a href="src/polytomic/bulk_sync/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing bulk sync's top-level configuration.

Updating a bulk sync is a **full replacement** of the sync's top-level
configuration. Every field in the request body is written to the sync; any
field you omit is cleared or reset to its default value.

To make a partial change — for example, toggling `active` or swapping a
schedule — fetch the current sync with
[`GET /api/bulk/syncs/{id}`](./get),
modify the fields you want to change, and send the complete object back in
the update request.

Updates to `active`, `schedules`, and `policies` take effect immediately.
Changes to source or destination configuration take effect on the sync's
next execution.

Because omitted fields are reset to their defaults, the discovery and
naming options behave the same as on create when left out:

- `automatically_add_new_objects` resets to not enabling newly discovered
  source objects automatically.
- `automatically_add_new_fields` resets to enabling newly discovered
  fields on already selected objects.
- `normalize_names` resets to enabled.

Send the existing values explicitly if you want to preserve a non-default or
non-empty setting, including schema and field selections.

> 📘 Updating schemas
>
> Schema updates are not performed through this endpoint. Use the
> [Update Bulk Sync Schemas](./schemas/patch)
> endpoint to change a subset of schemas, or
> [Update Bulk Sync Schema](./schemas/%7Bschema_id%7D/put)
> to replace a single schema's configuration.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import BulkSchedule, Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.update(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    destination_configuration={"schema": "my_schema"},
    destination_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    name="My Bulk Sync",
    schedule=BulkSchedule(
        frequency="manual",
    ),
    source_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**destination_configuration:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**destination_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `BulkSchedule` 
    
</dd>
</dl>

<dl>
<dd>

**source_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**automatically_add_new_fields:** `typing.Optional[BulkDiscover]` 
    
</dd>
</dl>

<dl>
<dd>

**automatically_add_new_objects:** `typing.Optional[BulkDiscover]` 
    
</dd>
</dl>

<dl>
<dd>

**concurrency_limit:** `typing.Optional[int]` — Override the default concurrency limit for this sync.
    
</dd>
</dl>

<dl>
<dd>

**data_cutoff_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**disable_record_timestamps:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**discover:** `typing.Optional[bool]` — DEPRECATED: Use automatically_add_new_objects/automatically_add_new_fields instead
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[BulkSyncMode]` 
    
</dd>
</dl>

<dl>
<dd>

**normalize_names:** `typing.Optional[BulkNormalizeNames]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**policies:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**resync_concurrency_limit:** `typing.Optional[int]` — Override the default resync concurrency limit for this sync.
    
</dd>
</dl>

<dl>
<dd>

**schemas:** `typing.Optional[typing.Sequence[V2UpdateBulkSyncRequestSchemasItem]]` — List of schemas to sync; if omitted, all schemas will be selected for syncing.
    
</dd>
</dl>

<dl>
<dd>

**source_configuration:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.<a href="src/polytomic/bulk_sync/client.py">remove</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a bulk sync, cancelling any running executions.

Any execution that is currently running is cancelled before the sync record is
removed.

> 🚧 All associated schedules, schema configurations, and execution history are
> deleted along with the sync.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.remove(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    refresh_schemas=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**refresh_schemas:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.<a href="src/polytomic/bulk_sync/client.py">activate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets whether a bulk sync is active.

Only active syncs are eligible to execute on their configured schedule.
Deactivating a sync prevents future scheduled runs and requests cancellation of
any execution that is currently in progress.

> 📘 To start or stop a running execution directly, use
> [`POST /api/bulk/syncs/{id}/executions`](../../../../../api-reference/bulk-sync/start)
> or
> [`POST /api/bulk/syncs/{id}/cancel`](../../../../../api-reference/bulk-sync/cancel).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.activate(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    active=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.<a href="src/polytomic/bulk_sync/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requests cancellation of any running executions on a bulk sync.

Cancellation is asynchronous. A successful response means the cancellation
signal has been queued; the running execution continues until the signal is
processed. Poll `GET /api/bulk/syncs/{id}/status` until the current execution
reaches a terminal state (`completed`, `canceled`, or `failed`) to confirm
cancellation has taken effect.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.cancel(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The active execution of this bulk sync ID will be cancelled.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.<a href="src/polytomic/bulk_sync/client.py">start</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts a new execution of a bulk sync.

This endpoint returns the execution record immediately after the run is queued
or started. Use the execution ID with the bulk-sync execution endpoints if you
need to monitor progress in detail.

## Execution modes

- Set `test=true` to validate the sync without writing to the destination.
- Use `resync_mode` for destructive or full-refresh style reruns.
- `test` and `resync_mode` are mutually exclusive.

The legacy `resync` boolean is no longer accepted on this v5 endpoint. Send
`resync_mode` instead.

If another execution is already running, the endpoint returns `409 Conflict`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.start(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the bulk sync.
    
</dd>
</dl>

<dl>
<dd>

**fetch_mode:** `typing.Optional[BulkFetchMode]` 
    
</dd>
</dl>

<dl>
<dd>

**resync:** `typing.Optional[bool]` — Deprecated: use resync_mode instead. Equivalent to resync_mode=rebuild.
    
</dd>
</dl>

<dl>
<dd>

**resync_mode:** `typing.Optional[BulkResyncMode]` 
    
</dd>
</dl>

<dl>
<dd>

**schemas:** `typing.Optional[typing.Sequence[str]]` — Optional list of schema IDs to include in this execution. If empty, all enabled schemas are included.
    
</dd>
</dl>

<dl>
<dd>

**test:** `typing.Optional[bool]` — When true, runs a test execution that validates the configuration without writing to the destination. Mutually exclusive with resync and resync_mode.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.<a href="src/polytomic/bulk_sync/client.py">get_status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current status of a bulk sync.

The response includes the sync's current active/inactive state together with
information about the most recent execution — its status, start time, and any
errors — making this endpoint well-suited for health checks and monitoring
dashboards.

For the complete execution history, use
[`GET /api/bulk/syncs/{id}/executions`](../../../../../api-reference/bulk-sync/executions/list).
For the full details of a specific run, including per-schema breakdowns, use
[`GET /api/bulk/syncs/{id}/executions/{exec_id}`](../../../../../api-reference/bulk-sync/executions/get).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.get_status(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the bulk sync.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.<a href="src/polytomic/bulk_sync/client.py">get_source</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the schemas (tables or objects) available on a connection for use as a bulk sync source, optionally including per-schema field details.

The response reflects what the
connection currently has cached; if the upstream source has changed, trigger
a refresh first with
[`POST /api/connections/{id}/schemas/refresh`](../../../../../api-reference/schemas/refresh).

These are the schemas available for selection, not the schemas already
configured on any particular sync. To inspect schemas on a running sync, use
[`GET /api/bulk/syncs/{id}/schemas`](../../../../../api-reference/bulk-sync/schemas/list).

Pass `include_fields=true` to receive per-schema field details in a single call.
Omit it when you only need the schema list, as field enumeration can be slow for
large sources.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.get_source(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    include_fields=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the connection.
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` — When true, include per-schema field lists in the response. Set to false for a smaller payload when field details are not needed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.<a href="src/polytomic/bulk_sync/client.py">get_destination</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Describes the destination configuration schema a connection accepts when used as a bulk sync destination.

The response is a JSON Schema object describing the shape of the
`destination_configuration` field you must supply when
[creating](../../../../../api-reference/bulk-sync/create) or
[updating](../../../../../api-reference/bulk-sync/update) a bulk sync that uses this
connection as its destination. Required fields vary by connection type.

> 📘 Fetch this endpoint once per connection type rather than once per sync.
> The configuration schema is the same for all syncs sharing the same
> destination connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.get_destination(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Connections
<details><summary><code>client.connections.<a href="src/polytomic/connections/client.py">get_types</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all connection types supported by this deployment.

Each entry includes per-type metadata:

- The available operations the connection type supports.
- Its category.
- Whether the connection type is enabled for the caller's organization.
- Which modes (source, destination, enrichment) it can act as.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.connections.get_types()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/polytomic/connections/client.py">get_connection_type_schema</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the JSON schema for a connection type.

This schema is intended for building forms or validating configuration payloads
client-side. It describes the structure Polytomic expects when you create or
update a connection of the given type.

The response is metadata about the shape of the configuration, not a live
connection instance and not a set of current credential values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.connections.get_connection_type_schema(
    id="postgresql",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Connection type identifier (e.g. postgresql, salesforce, hubspot).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/polytomic/connections/client.py">get_type_parameter_values</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns completion values for parameter fields on a connection type.

This endpoint is useful during connection setup, before a connection exists or
before you want to persist it. The supplied `parameters` are applied to a
temporary in-memory connection shape and used to resolve dependent options.

When an endpoint requires upstream authorization before it can return values,
Polytomic returns an error instead of guessing. In that case, complete the
authorization flow first and call the endpoint again.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.connections.get_type_parameter_values(
    type="type",
    field="field",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**field:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/polytomic/connections/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists every connection in the caller's organization, with sensitive fields redacted.

Sensitive configuration values — passwords, API tokens, private keys — are
redacted from all responses. To understand which fields a connection type
exposes, consult the parameter schema returned by
[`GET /api/connection_types`](../../api-reference/connections/get-types).

To inspect the data objects available on a specific connection, use
[`POST /api/connections/{id}/schemas/refresh`](../../api-reference/schemas/refresh)
followed by [`GET /api/connections/{id}/schemas/status`](../../api-reference/schemas/get-status).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.connections.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/polytomic/connections/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new connection of the specified type.

Use [`GET /api/connection_types`](../../api-reference/connections/get-types) to retrieve the
list of available types and their parameter schemas. The `configuration`
object is type-specific; consult the [integration
guides](../../guides/configuring-your-connections/overview)
for the required and optional fields for each type.

> 📘 Polytomic validates the connection against the upstream service
> immediately on creation. The request will fail if the credentials or
> endpoint cannot be reached.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.connections.create(
    configuration={
        "database": "example",
        "hostname": "postgres.example.com",
        "password": "********",
        "port": 5432,
        "username": "user",
    },
    name="My Postgres Connection",
    type="postgresql",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**configuration:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**healthcheck_interval:** `typing.Optional[str]` — Override interval for connection health checking.
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**policies:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` — URL to redirect to after completing OAuth flow.
    
</dd>
</dl>

<dl>
<dd>

**validate:** `typing.Optional[bool]` — Validate connection configuration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/polytomic/connections/client.py">connect</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a Polytomic Connect session and returns a redirect URL that embeds the Connect modal.

See also:

- [Embedding authentication](../../../guides/embedding-authentication), a guide to using Polytomic Connect.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.connections.connect(
    name="Salesforce Connection",
    redirect_url="redirect_url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the new connection. Must be unique per organization.
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `str` — URL to redirect to after connection is created.
    
</dd>
</dl>

<dl>
<dd>

**connection:** `typing.Optional[str]` — The id of an existing connection to update.
    
</dd>
</dl>

<dl>
<dd>

**dark:** `typing.Optional[bool]` — Whether to use the dark theme for the Connect modal.
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — Connection type to create.
    
</dd>
</dl>

<dl>
<dd>

**whitelist:** `typing.Optional[typing.Sequence[str]]` — List of connection types which are allowed to be created. Ignored if type is set.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/polytomic/connections/client.py">test_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Tests a connection configuration.

This endpoint is useful for setup flows that want to verify credentials before
persisting them.

If you provide `connection_id`, Polytomic starts from the saved configuration
for that connection and then applies the request's `configuration` values on
top. This lets callers test a partial change without resending every existing
field.

The request does not persist any configuration changes even when validation
succeeds.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.connections.test_connection(
    configuration={
        "database": "example",
        "hostname": "postgres.example.com",
        "password": "password",
        "port": 5432,
        "username": "user",
    },
    type="postgresql",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**configuration:** `typing.Dict[str, typing.Optional[typing.Any]]` — Connection configuration to test.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — The type of connection to test.
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `typing.Optional[str]` — Optional existing connection ID to use as a base for testing. The provided configuration will be merged over the stored configuration for this connection before testing.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/polytomic/connections/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single connection by ID, with sensitive fields redacted.

To inspect the schemas available on this connection, trigger a refresh with
[`POST /api/connections/{id}/schemas/refresh`](./schemas/refresh/post) and
track progress via
[`GET /api/connections/{id}/schemas/status`](./schemas/status/get).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.connections.get(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/polytomic/connections/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a connection's configuration.

Updating a connection is a **full replacement** of its configuration. Any
`configuration` field you omit is cleared. To make a partial change, fetch
the current connection with
[`GET /api/connections/{id}`](./get), apply your edits, and send the
complete object back.

> 📘 The connection is re-validated against the upstream service after every
> update. The request will fail if the new credentials or endpoint cannot be
> reached.

Syncs that are already running when the update is submitted are not
interrupted; the updated configuration takes effect on their next execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.connections.update(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    configuration={
        "database": "example",
        "hostname": "postgres.example.com",
        "password": "********",
        "port": 5432,
        "username": "user",
    },
    name="My Postgres Connection",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**healthcheck_interval:** `typing.Optional[str]` — Override interval for connection health checking.
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**policies:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**reconnect:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**validate:** `typing.Optional[bool]` — Validate connection configuration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/polytomic/connections/client.py">remove</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a connection.

> 🚧 Deleting a connection that is referenced by fieldsets, syncs, bulk
> syncs, or schedules returns `422 connection in use` unless you pass
> `force=true`. With `force=true`, the API deletes those dependent
> resources before removing the connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.connections.remove(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    force=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/polytomic/connections/client.py">get_parameter_values</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns completion values for parameter fields on a persisted connection.

Use this endpoint when the available options for one parameter depend on the
connection's saved credentials or previously selected settings. For example,
after a connection is authorized, the upstream service may be able to return
lists of databases, schemas, or similar selectable values.

For new setup flows, prefer
[`POST /api/connection_types/{type}/parameter_values`](./get-type-parameter-values),
which lets you resolve completions before the connection has been created.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.connections.get_parameter_values(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/polytomic/connections/client.py">create_shared_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Shares a connection with another organization in the caller's partner account.

> 🚧 Requires partner key
>
> Shared connections can only be created by using [partner keys](../../../../guides/obtaining-api-keys#partner-keys).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.connections.create_shared_connection(
    parent_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    child_organization_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**parent_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**child_organization_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.connections.<a href="src/polytomic/connections/client.py">list_shared_connections</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists shared copies of a connection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.connections.list_shared_connections(
    parent_connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**parent_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## QueryRunner
<details><summary><code>client.query_runner.<a href="src/polytomic/query_runner/client.py">run_query</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits a query for asynchronous execution against the connection.

This endpoint returns immediately with a query task ID. It does not wait for
the query to finish. Poll [`GET /api/queries/{id}`](./get-query) until `status`
reaches `done` or `failed`.

Only the user who created the query can fetch its results later. Query results
are stored temporarily and may expire; use the `expires` field from the result
endpoint to understand how long they will remain available.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.query_runner.run_query(
    connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    query="SELECT * FROM table",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `str` — Unique identifier of the connection to run the query against.
    
</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[str]` — The query to execute against the connection.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.query_runner.<a href="src/polytomic/query_runner/client.py">get_query</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetches the latest status for a submitted query and, once complete, returns fields and paginated results.

This endpoint is the second step of the query-runner flow. First call
[`POST /api/connections/{connection_id}/query`](./run-query),
then poll this endpoint with the returned ID.

Results may be paginated across multiple blobs. When that happens, use the
opaque `links.next` and `links.previous` URLs exactly as returned. Do not try to
construct the `page` token yourself.

If the query is still running, the response may include only status metadata.
If the task is complete but the caller is not the same user that created it,
the endpoint returns `404`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.query_runner.get_query(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the query task, as returned by POST /api/connections/{connection_id}/query.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` — Opaque pagination token returned in the links.next or links.previous URL of the previous response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Schemas
<details><summary><code>client.schemas.<a href="src/polytomic/schemas/client.py">upsert_field</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates user-defined fields on a schema, matched by field_id.

Fields are matched by `field_id`. Reusing an existing `field_id` updates that
field; using a new `field_id` creates a new user-defined field.

This makes the endpoint safe to retry when you are intentionally upserting the
same field definitions. It is not a patch-by-position operation.

If some fields succeed and others fail, the endpoint can return a partial
success response. Validate the response status and message rather than assuming
the whole batch was applied uniformly.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.schemas.upsert_field(
    connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    schema_id="public.users",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `str` — Unique identifier of the connection.
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` — Identifier of the schema the fields belong to.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Sequence[V4UserFieldRequest]]` — Fields to create or update on the schema. Existing user-defined fields with the same field_id are replaced.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schemas.<a href="src/polytomic/schemas/client.py">delete_field</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a user-defined field from a schema.

Only user-defined fields — those created via
[`POST /api/connections/{connection_id}/schemas/{schema_id}/fields`](../../../../../../../api-reference/schemas/upsert-field)
— can be removed through this endpoint. Fields detected automatically from
the source cannot be deleted here; they are managed through schema refresh.

> 🚧 Deleting a field that is referenced in an active sync mapping may cause
> that sync to error on its next execution. Remove or update any dependent
> mappings before deleting the field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.schemas.delete_field(
    connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    schema_id="public.users",
    field_id="first_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `str` — Unique identifier of the connection.
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` — Identifier of the schema the field belongs to.
    
</dd>
</dl>

<dl>
<dd>

**field_id:** `str` — Identifier of the user-defined field to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schemas.<a href="src/polytomic/schemas/client.py">set_primary_keys</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Overrides the primary key detected on a schema.

This is a full replacement: the keys you supply become the complete override
set, replacing any previously configured overrides. Omitting a key that was
previously set removes it.

Primary key overrides are useful when the source does not expose a primary
key or when the source-detected key is not the correct deduplication
identifier for your use case.

> 📘 To revert to the source-detected primary keys and remove all overrides,
> use [`DELETE /api/connections/{connection_id}/schemas/{schema_id}/primary_keys`](./delete).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.schemas.set_primary_keys(
    connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    schema_id="public.users",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `str` — Unique identifier of the connection.
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` — Identifier of the schema whose primary keys are being overridden.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Sequence[SchemaPrimaryKeyOverrideInput]]` — Ordered list of source fields that together form the primary key. Replaces any existing override; supply an empty list to clear.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schemas.<a href="src/polytomic/schemas/client.py">reset_primary_keys</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes all primary key overrides for a schema, reverting to the primary keys detected from the source.

To replace the overrides with a new set rather than clearing them entirely,
use [`PUT /api/connections/{connection_id}/schemas/{schema_id}/primary_keys`](./put)
instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.schemas.reset_primary_keys(
    connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    schema_id="public.users",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `str` — Unique identifier of the connection.
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` — Identifier of the schema whose primary key override should be cleared.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schemas.<a href="src/polytomic/schemas/client.py">refresh</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Refreshes a connection's cached schemas.

Call this when the upstream source has added, removed, or changed tables,
objects, or fields and you need Polytomic to re-inspect the connection before
creating or updating sync configuration.

This endpoint does not return the refreshed schemas directly. Follow the
`Location` header or poll [`GET /api/connections/{id}/schemas/status`](./get-status)
until the refresh completes, then fetch the schemas you need.

> 📘 Schema refresh is asynchronous
>
> This endpoint kicks off a background refresh of the connection's cached
> schemas and returns a `Location` header pointing at
> [`GET /api/connections/{id}/schemas/status`](../../../../../api-reference/schemas/get-status).
> Poll that endpoint until `cache_status` transitions from `refreshing` to
> `fresh` (or until `last_refresh_finished` advances past
> `last_refresh_started`) to observe completion.
>
> Only connections whose current health status is healthy may be refreshed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.schemas.refresh(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the connection whose schema cache should be refreshed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schemas.<a href="src/polytomic/schemas/client.py">get_status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current schema inspection status for a connection.

Poll this endpoint after calling
[`POST /api/connections/{id}/schemas/refresh`](../../../../../api-reference/schemas/refresh) to track
progress. When `status` transitions to `completed`, the refreshed schemas
are available for use in sync configuration.

> 📘 Schema refresh is asynchronous
>
> This endpoint kicks off a background refresh of the connection's cached
> schemas and returns a `Location` header pointing at
> [`GET /api/connections/{id}/schemas/status`](../../../../../api-reference/schemas/get-status).
> Poll that endpoint until `cache_status` transitions from `refreshing` to
> `fresh` (or until `last_refresh_finished` advances past
> `last_refresh_started`) to observe completion.
>
> Only connections whose current health status is healthy may be refreshed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.schemas.get_status(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the connection whose schema cache status should be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schemas.<a href="src/polytomic/schemas/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single schema on a connection.

The schema is returned from the connection's cached schema set. If the
upstream source has changed since the last inspection, the result may be
stale.

> 📘 Trigger [`POST /api/connections/{id}/schemas/refresh`](../../../../../api-reference/schemas/refresh)
> and wait for it to complete before fetching this endpoint if you need
> up-to-date field definitions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.schemas.get(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    schema_id="public.users",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the connection.
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` — Identifier of the schema within the connection. Format depends on the connection type (e.g. schema.table for databases, object name for SaaS backends).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.schemas.<a href="src/polytomic/schemas/client.py">get_records</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a sample of records from a schema on a connection.

The sample is intended for previewing the shape and values of data before
committing to a sync configuration, not for full data export.

> 🚧 The sample is not guaranteed to be representative of the full dataset.
> Row selection is implementation-defined and may differ across connection
> types.

> 📘 If the schema's field definitions are stale, refresh them first with
> [`POST /api/connections/{id}/schemas/refresh`](../../../../../../api-reference/schemas/refresh) to ensure
> the sample aligns with the current schema structure.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.schemas.get_records(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    schema_id="public.users",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the connection.
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` — Identifier of the schema within the connection.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Models
<details><summary><code>client.models.<a href="src/polytomic/models/client.py">get_enrichment_source</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Describes the enrichment source configuration available on a connection.

Not all connections support enrichment. Call this endpoint to determine
whether a connection can serve as an enrichment source in a model sync and,
if so, what configuration it accepts.

> ⚠️ If the connection does not support enrichment, this endpoint returns
> `404`. Check for that status before attempting to configure an enrichment
> source on a sync.

When a connection does support enrichment, the response describes the
configuration fields required to set it up. Pass those values in the
`enrichment` block when creating or updating a model sync.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.models.get_enrichment_source(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the connection.
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Sequence[str]]]]` — Query parameters used to incrementally refine a dependent source configuration. Keys correspond to configuration fields returned by previous calls to this endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/polytomic/models/client.py">post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the valid input field sets for an enrichment configuration on a connection.

When configuring an enrichment source in a model sync, use this endpoint to
discover which input fields the enrichment connection requires. Pass the
proposed enrichment configuration in the request body; the response lists the
valid input field sets that map your model's fields to the enrichment service's
expected inputs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.models.post(
    connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[V2EnricherConfiguration]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/polytomic/models/client.py">preview</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits a job that previews the fields a model would expose without persisting it.

The response contains a job ID that resolves to the list of fields the model
would expose. Poll the job until it completes to retrieve the field list. The
model is not persisted — this endpoint is useful for validating a query or
configuration before calling [`POST /api/models`](../../api-reference/models/create) to save it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.models.preview(
    configuration={"table": "public.users"},
    connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    name="Users",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**configuration:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**additional_fields:** `typing.Optional[typing.Sequence[ModelModelFieldRequest]]` 
    
</dd>
</dl>

<dl>
<dd>

**enricher:** `typing.Optional[Enrichment]` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**policies:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**relations:** `typing.Optional[typing.Sequence[ModelRelation]]` 
    
</dd>
</dl>

<dl>
<dd>

**tracking_columns:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/polytomic/models/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all models in the caller's organization.

Results are ordered by `updated_at` descending, with `id` used as a tiebreaker.
If more results are available, the response includes `pagination.next_page_token`.
Pass that token back unchanged to continue from the last item you received.

The token is opaque. Do not construct or edit it yourself.

The `limit` is capped at 50. Values above that cap are reduced to 50, and
non-positive values fall back to the same default.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.models.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/polytomic/models/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new model.

A model defines a query or view over a connection's data — for example, a SQL
query, a filtered object, or a joined dataset. Models are used as sources when
creating model syncs.

The connection referenced by `connection_id` must have source capabilities. Use
[`GET /api/connection_types/{id}`](../../api-reference/connections/get-connection-type-schema) to check
whether a connection type supports use as a source.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.models.create(
    configuration={"table": "public.users"},
    connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    name="Users",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**configuration:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**additional_fields:** `typing.Optional[typing.Sequence[ModelModelFieldRequest]]` 
    
</dd>
</dl>

<dl>
<dd>

**enricher:** `typing.Optional[Enrichment]` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**policies:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**relations:** `typing.Optional[typing.Sequence[ModelRelation]]` 
    
</dd>
</dl>

<dl>
<dd>

**tracking_columns:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/polytomic/models/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single model by ID, including its source fields, identity, and filters.

The response includes the model's source fields, identity column, and any
configured filters. To preview the data a model would return without saving
changes, use [`GET /api/models/{id}/sample`](./sample/get).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.models.get(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/polytomic/models/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a model's configuration.

Updating a model is a **full replacement** of its configuration. Every field in
the request body is written to the model; any field you omit is cleared or reset
to its default value.

To make a partial change, fetch the current model with
[`GET /api/models/{id}`](./get), modify the fields you want to change, and send
the complete object back in the update request.

Changes to source fields, filters, or the identity column take effect on the
next sync execution that uses this model.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.models.update(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    async_=False,
    configuration={"table": "public.users"},
    connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    name="Users",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**additional_fields:** `typing.Optional[typing.Sequence[ModelModelFieldRequest]]` 
    
</dd>
</dl>

<dl>
<dd>

**enricher:** `typing.Optional[Enrichment]` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**labels:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**policies:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**refresh:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**relations:** `typing.Optional[typing.Sequence[ModelRelation]]` 
    
</dd>
</dl>

<dl>
<dd>

**tracking_columns:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/polytomic/models/client.py">remove</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a model.

> 🚧 Deleting a model used by one or more syncs will break those syncs. Remove
> or reconfigure any syncs that reference this model before deleting it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.models.remove(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/polytomic/models/client.py">sample</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a sample of records from a model.

Synchronous requests must complete within 10 seconds. If the source query or
enrichment step can exceed that budget, use the asynchronous option so the
work runs as a background job.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.models.sample(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ModelSync
<details><summary><code>client.model_sync.<a href="src/polytomic/model_sync/client.py">get_source</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Describes the source configuration available on a connection for use as a model sync source.

Use this endpoint before creating a model to understand what configuration is
available. Once you have a configuration, resolve the fields available for
sync mapping with
[`GET /api/connections/{id}/modelsync/source/fields`](./fields/get).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.get_source(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the connection.
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Sequence[str]]]]` — Query parameters used to incrementally refine a dependent source configuration. Keys correspond to configuration fields returned by previous calls to this endpoint.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.<a href="src/polytomic/model_sync/client.py">get_source_fields</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the source fields available on a connection for a given source configuration.

Pass the model's source configuration as query parameters to resolve the
fields that the connection will expose for that specific configuration. The
returned fields are what can be referenced in sync field mappings.

> 📘 Results depend on the source configuration you supply. A different
> table or query in the configuration may return a completely different field
> list.

The available source configuration parameters are described by
[`GET /api/connections/{id}/modelsync/source`](../../../../../../api-reference/model-sync/get-source).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.get_source_fields(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the connection.
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Sequence[str]]]]` — Source configuration, matching the params used with GET /api/connections/{id}/modelsync/source, that selects the specific source to return fields for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.<a href="src/polytomic/model_sync/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all model syncs in the caller's organization.

Results are ordered by `updated_at` descending, with `id` used as a tiebreaker.
If more results are available, the response includes `pagination.next_page_token`.
Pass that token back unchanged to continue from the last item you received.

The token is opaque. Do not construct or edit it yourself.

The `limit` is capped at 50. Values above that cap are reduced to 50, and
non-positive values fall back to the same default.

This endpoint returns syncs visible to the current caller's organization scope.
To inspect a specific sync in more detail, follow up with
[`GET /api/syncs/{id}`](./get).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.list(
    active=True,
    target_connection_id="0b155265-c537-44c9-9359-a3ceb468a4da",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ModelSyncMode]` 
    
</dd>
</dl>

<dl>
<dd>

**target_connection_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.<a href="src/polytomic/model_sync/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new model sync.

Create a new sync from one or more models to a destination.

All of the functionality described in [the product
documentation](https://docs.polytomic.com/docs/sync-destinations) is
configurable via the API.

Guides:

- [Model sync (Reverse ETL) from Snowflake query to Salesforce](../../guides/code-examples/model-sync-reverse-etl-from-snowflake-query-to-salesforce)
- [Joined model sync from Postgres, Airtable, and Stripe to Hubspot](../../guides/code-examples/joined-model-sync-from-postgres-airtable-and-stripe-to-hubspot)

## Targets (Destinations)

Polytomic refers to a model sync's destination as the "target object", or
target. Target objects are identified by a connection ID and an object ID. You
can retrieve a list of all target objects for a connection using the [Get Target
Objects](./targets/list) endpoint.

The `target` object in the request specifies information about the sync destination.

```json
"target": {
    "connection_id": "248df4b7-aa70-47b8-a036-33ac447e668d",
    "object": "Users",
},
```

Some connections support additional configuration for targets. For example,
[Salesforce
connections](../../guides/configuring-your-connections/connections/salesforce#target)
support optionally specifying the ingestion API to use. The target specific
options are passed as `configuration`; consult the [integration
guides](../../guides/configuring-your-connections/overview)
for details about specific connection configurations.

### Creating a new target

Some integrations support creating a new target when creating a model sync. For
example, an ad audience or database table.

When creating a new target, `object` is omitted and `create` is specified
instead. The `create` property is an object containing integration specific
configuration for the new target.

```json
"target": {
    "connection_id": "248df4b7-aa70-47b8-a036-33ac447e668d",
    "create": {
        "name": "New audience",
        "type": "user_audience"
    }
},
```

The [Get Target List](./targets/list) endpoint returns information about whether
a connection supports target creation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import ModelSyncField, Polytomic, Schedule, Target

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.create(
    fields=[
        ModelSyncField(
            target="name",
        )
    ],
    mode="create",
    name="Users Sync",
    schedule=Schedule(),
    target=Target(
        connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Sequence[ModelSyncField]` — Fields to sync from source to destination.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `ModelSyncMode` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `Schedule` 
    
</dd>
</dl>

<dl>
<dd>

**target:** `Target` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Whether the sync is enabled and scheduled.
    
</dd>
</dl>

<dl>
<dd>

**encryption_passphrase:** `typing.Optional[str]` — Passphrase for encrypting the sync data.
    
</dd>
</dl>

<dl>
<dd>

**filter_logic:** `typing.Optional[str]` — Logical expression to combine filters.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Sequence[Filter]]` — Filters to apply to the source data.
    
</dd>
</dl>

<dl>
<dd>

**identity:** `typing.Optional[Identity]` 
    
</dd>
</dl>

<dl>
<dd>

**only_enrich_updates:** `typing.Optional[bool]` — Whether to use enrichment models as a source of possible changes to sync. If true, only changes to the base models will cause a record to sync.
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — Organization ID for the sync; read-only with a partner key.
    
</dd>
</dl>

<dl>
<dd>

**override_fields:** `typing.Optional[typing.Sequence[ModelSyncField]]` — Values to set in the target unconditionally.
    
</dd>
</dl>

<dl>
<dd>

**overrides:** `typing.Optional[typing.Sequence[Override]]` — Conditional value replacement for fields.
    
</dd>
</dl>

<dl>
<dd>

**policies:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**skip_initial_backfill:** `typing.Optional[bool]` — Whether to skip the initial backfill of records; if true only records seen after the sync is enabled will be synced.
    
</dd>
</dl>

<dl>
<dd>

**sync_all_records:** `typing.Optional[bool]` — Whether to sync all records from the source, regardless of whether they've changed since the previous execution.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.<a href="src/polytomic/model_sync/client.py">get_schedule_options</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the schedule types available when creating or updating a model sync.

Use the `type` identifiers returned by this endpoint in the `schedule` field
when creating or updating a sync via
[`POST /api/syncs`](../../../api-reference/model-sync/create) or [`PUT /api/syncs/{id}`](../../../api-reference/model-sync/update).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.get_schedule_options()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.<a href="src/polytomic/model_sync/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single model sync by ID.

To check whether a sync is currently running or has recently completed, use
[`GET /api/syncs/{id}/status`](./status/get). For the full history of
executions, use [`GET /api/syncs/{id}/executions`](./executions/get).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.get(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.<a href="src/polytomic/model_sync/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a model sync's configuration.

Updating a model sync is a **full replacement** of the sync's configuration.
Every field in the request body is written to the sync; any field you omit is
cleared or reset to its default value.

To make a partial change — for example, toggling `active` or adjusting a
single field mapping — fetch the current sync with
[`GET /api/syncs/{id}`](../../../api-reference/model-sync/get),
modify the fields you want to change, and send the complete object back in
the update request.

Updates to `active`, `schedule`, and `policies` take effect immediately.
Changes to source fields, target configuration, filters, or field mappings
take effect on the sync's next execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import ModelSyncField, Polytomic, Schedule, Target

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.update(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    fields=[
        ModelSyncField(
            target="name",
        )
    ],
    mode="create",
    name="Users Sync",
    schedule=Schedule(),
    target=Target(
        connection_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Sequence[ModelSyncField]` — Fields to sync from source to destination.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `ModelSyncMode` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `Schedule` 
    
</dd>
</dl>

<dl>
<dd>

**target:** `Target` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Whether the sync is enabled and scheduled.
    
</dd>
</dl>

<dl>
<dd>

**encryption_passphrase:** `typing.Optional[str]` — Passphrase for encrypting the sync data.
    
</dd>
</dl>

<dl>
<dd>

**filter_logic:** `typing.Optional[str]` — Logical expression to combine filters.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Sequence[Filter]]` — Filters to apply to the source data.
    
</dd>
</dl>

<dl>
<dd>

**identity:** `typing.Optional[Identity]` 
    
</dd>
</dl>

<dl>
<dd>

**only_enrich_updates:** `typing.Optional[bool]` — Whether to use enrichment models as a source of possible changes to sync. If true, only changes to the base models will cause a record to sync.
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — Organization ID for the sync; read-only with a partner key.
    
</dd>
</dl>

<dl>
<dd>

**override_fields:** `typing.Optional[typing.Sequence[ModelSyncField]]` — Values to set in the target unconditionally.
    
</dd>
</dl>

<dl>
<dd>

**overrides:** `typing.Optional[typing.Sequence[Override]]` — Conditional value replacement for fields.
    
</dd>
</dl>

<dl>
<dd>

**policies:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**skip_initial_backfill:** `typing.Optional[bool]` — Whether to skip the initial backfill of records; if true only records seen after the sync is enabled will be synced.
    
</dd>
</dl>

<dl>
<dd>

**sync_all_records:** `typing.Optional[bool]` — Whether to sync all records from the source, regardless of whether they've changed since the previous execution.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.<a href="src/polytomic/model_sync/client.py">remove</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a model sync, cancelling any running executions.

Deletion is permanent. Any running execution is cancelled before the sync
record is removed. Deleted syncs cannot be recovered; recreate them using
[`POST /api/syncs`](../../../api-reference/model-sync/create) if needed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.remove(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.<a href="src/polytomic/model_sync/client.py">activate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets whether a model sync is active.

Only active syncs execute on schedule or in response to a manual trigger. Set
`active` to `false` to pause a sync without deleting it.

> 📘 Deactivating a sync does not cancel an execution that is already in
> progress. Use [`POST /api/syncs/{id}/cancel`](../../../../api-reference/model-sync/cancel) to stop a
> running execution.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.activate(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    active=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.<a href="src/polytomic/model_sync/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requests cancellation of any running executions on a model sync.

Cancellation is asynchronous. A successful response means the cancellation
signal has been queued; the running execution continues until the signal is
processed. Poll `GET /api/syncs/{id}/status` until the current execution
reaches a terminal state (`completed`, `canceled`, or `failed`) to confirm
cancellation has taken effect.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.cancel(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The active execution of this sync ID will be cancelled.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.<a href="src/polytomic/model_sync/client.py">start</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts a new execution of a model sync.

> 🚧 Force full resync
>
> Use caution when setting the `resync` parameter to `true`. This will force a full resync of the data from the source system. This can be a time-consuming operation and may impact the performance of the source system. It is recommended to only use this option when necessary.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.start(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**identities:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**resync:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**test:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.<a href="src/polytomic/model_sync/client.py">get_status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current status of a model sync.

The response includes a summary of the most recent execution, including its
start time, completion time, and record counts. For the complete execution
history, use [`GET /api/syncs/{id}/executions`](../../../../api-reference/model-sync/executions/list).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.get_status(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Events
<details><summary><code>client.events.<a href="src/polytomic/events/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists audit events for the caller's organization.

Results are paginated. If more events are available, the response includes
`pagination.next_page_token`; pass that token back unchanged to continue from
the last item you received.

Filter by event type using the `event_type` query parameter. Pass one of the
identifiers returned by [`GET /api/events_types`](../../api-reference/events/get-types) to
narrow results to a specific category of activity.

> 📘 Events reflect audit activity scoped to the caller's organization.
> The log captures both user-initiated and API-initiated actions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.events.list(
    organization_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    starting_after=datetime.datetime.fromisoformat(
        "2020-01-01 00:00:00+00:00",
    ),
    ending_before=datetime.datetime.fromisoformat(
        "2020-01-01 00:00:00+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` — Organization to list events for. Only used by system callers; normal and partner callers are always scoped to their own organization.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — Filter to a single event type. Use GET /api/events_types to list valid values.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[dt.datetime]` — Return events created strictly after this timestamp.
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[dt.datetime]` — Return events created strictly before this timestamp.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of events to return. Default 10, maximum 100.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/polytomic/events/client.py">get_types</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the set of event type identifiers supported by GET /api/events.

Use the identifiers returned here as the `event_type` filter value when calling
[`GET /api/events`](../../api-reference/events/list).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.events.get_types()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Jobs
<details><summary><code>client.jobs.<a href="src/polytomic/jobs/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current state of an asynchronous job.

This endpoint is used as a polling target by other asynchronous workflows such
as model preview and log export. The caller must know the job `type` and `id`
that were returned when the job was created.

If the job is still running, the response returns `status: running` and may not
include a `result` yet. Once complete, `status` becomes `done` or `failed`.

Only specific job types are supported by this endpoint. Passing an unknown
`type` returns `400`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.jobs.get(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    type="createmodel",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the job (usually returned by whichever endpoint started the job).
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — Job type. One of: createmodel, updatemodel, previewmodel, samplemodel, exportlogs.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Identity
<details><summary><code>client.identity.<a href="src/polytomic/identity/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about the authenticated caller and, if applicable, the organization they are scoped to.

Use this endpoint to confirm which kind of credential is being used before
calling endpoints with stricter authorization rules.

For user-scoped credentials, the response includes the resolved user and
organization details. For non-user keys, the response identifies the key class
with the corresponding boolean flags instead of impersonating a user.

This endpoint is especially useful when debugging why a request is being
accepted or rejected by endpoints that are limited to particular caller types.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.identity.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Notifications
<details><summary><code>client.notifications.<a href="src/polytomic/notifications/client.py">get_global_error_subscribers</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of email addresses subscribed to global sync error notifications for the caller's organization.

To update the subscriber list, use
[`PUT /api/notifications/global-error-subscribers`](./put).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.notifications.get_global_error_subscribers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.notifications.<a href="src/polytomic/notifications/client.py">set_global_error_subscribers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces the list of email addresses subscribed to global sync error notifications for the caller's organization.

This is a **full replacement** — the request body becomes the complete
subscriber list. To add or remove a single address without affecting others,
fetch the current list with
[`GET /api/notifications/global-error-subscribers`](./get), apply your change,
and send the modified list back.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.notifications.set_global_error_subscribers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**emails:** `typing.Optional[typing.Sequence[str]]` — Email addresses to subscribe to global sync error notifications. Replaces the current subscriber list; pass an empty list to unsubscribe everyone.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Organization
<details><summary><code>client.organization.<a href="src/polytomic/organization/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists organizations accessible to the caller.

> 🚧 Requires partner key
>
> This endpoint is only accessible using [partner keys](../../guides/obtaining-api-keys#partner-keys).

The result depends on the caller type:

- User-scoped callers receive their current organization.
- Partner callers receive the organizations available within their partner
  scope.
- Deployment-level callers may receive a broader organization list, depending
  on deployment configuration.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.organization.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.<a href="src/polytomic/organization/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new organization under the calling partner account, optionally configuring SSO or OIDC at creation time.

> 🚧 Requires partner key
>
> This endpoint is only accessible using [partner keys](../../guides/obtaining-api-keys#partner-keys).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.organization.create(
    name="My Organization",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Human-readable name of the organization. Must be unique across the partner account.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — OIDC client ID issued by the identity provider.
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `typing.Optional[str]` — OIDC client secret issued by the identity provider. Write-only; never returned in responses.
    
</dd>
</dl>

<dl>
<dd>

**issuer:** `typing.Optional[str]` — OIDC issuer URL for organizations using OpenID Connect single sign-on.
    
</dd>
</dl>

<dl>
<dd>

**sso_domain:** `typing.Optional[str]` — Email domain used to match users to this organization during SSO sign-in.
    
</dd>
</dl>

<dl>
<dd>

**sso_org_id:** `typing.Optional[str]` — WorkOS organization identifier linking this organization to its SAML/SSO configuration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.<a href="src/polytomic/organization/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single organization by ID.

> 🚧 Requires partner key
>
> This endpoint is only accessible using [partner keys](../../../guides/obtaining-api-keys#partner-keys).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.organization.get(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the organization.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.<a href="src/polytomic/organization/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an organization's configuration.

> 🚧 Requires partner key
>
> This endpoint is only accessible using [partner keys](../../../guides/obtaining-api-keys#partner-keys).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.organization.update(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    name="My Organization",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the organization to update.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable name of the organization. Must be unique across the partner account.
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — OIDC client ID issued by the identity provider.
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `typing.Optional[str]` — OIDC client secret issued by the identity provider. Write-only; never returned in responses.
    
</dd>
</dl>

<dl>
<dd>

**issuer:** `typing.Optional[str]` — OIDC issuer URL for organizations using OpenID Connect single sign-on.
    
</dd>
</dl>

<dl>
<dd>

**sso_domain:** `typing.Optional[str]` — Email domain used to match users to this organization during SSO sign-in.
    
</dd>
</dl>

<dl>
<dd>

**sso_org_id:** `typing.Optional[str]` — WorkOS organization identifier linking this organization to its SAML/SSO configuration.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.organization.<a href="src/polytomic/organization/client.py">remove</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an organization.

> 🚧 Requires partner key
>
> This endpoint is only accessible using [partner keys](../../../guides/obtaining-api-keys#partner-keys).

Partner callers cannot delete their own owner organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.organization.remove(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the organization.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/polytomic/users/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all users in the specified organization.

> 🚧 Requires partner key
>
> User endpoints are only accessible using [partner keys](../../../../guides/obtaining-api-keys#partner-keys).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.users.list(
    org_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique identifier of the organization whose users should be listed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/polytomic/users/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new user in the specified organization and assigns the requested permissions roles.

> 🚧 Requires partner key
>
> User endpoints are only accessible using [partner keys](../../../../guides/obtaining-api-keys#partner-keys).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.users.create(
    org_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    email="mail@example.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique identifier of the organization the user belongs to.
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Email address used to sign the user in and receive notifications.
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` — Deprecated legacy role name. Use role_ids instead; setting both role and role_ids in the same request is rejected.
    
</dd>
</dl>

<dl>
<dd>

**role_ids:** `typing.Optional[typing.Sequence[str]]` — Identifiers of the permissions roles to assign to the user. Must contain at least one entry when provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/polytomic/users/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single user in the specified organization.

> 🚧 Requires partner key
>
> User endpoints are only accessible using [partner keys](../../../../../guides/obtaining-api-keys#partner-keys).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.users.get(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    org_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `str` — Unique identifier of the organization the user belongs to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/polytomic/users/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a user's assigned permissions roles.

> 🚧 Requires partner key
>
> User endpoints are only accessible using [partner keys](../../../../../guides/obtaining-api-keys#partner-keys).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.users.update(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    org_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    email="mail@example.com",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the user to update.
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `str` — Unique identifier of the organization the user belongs to.
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Email address used to sign the user in and receive notifications.
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` — Deprecated legacy role name. Use role_ids instead; setting both role and role_ids in the same request is rejected.
    
</dd>
</dl>

<dl>
<dd>

**role_ids:** `typing.Optional[typing.Sequence[str]]` — Identifiers of the permissions roles to assign to the user. Must contain at least one entry when provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/polytomic/users/client.py">remove</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a user from the specified organization.

> 🚧 Requires partner key
>
> User endpoints are only accessible using [partner keys](../../../../../guides/obtaining-api-keys#partner-keys).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.users.remove(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    org_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the user.
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `str` — Unique identifier of the organization the user belongs to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/polytomic/users/client.py">create_api_key</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Issues a new API key for the specified user.

> 🚧 Requires partner key
>
> User endpoints are only accessible using [partner keys](../../../../../../guides/obtaining-api-keys#partner-keys).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.users.create_api_key(
    org_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    force=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `str` — Unique identifier of the organization the user belongs to.
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — Unique identifier of the user the key will be issued for.
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[bool]` — If true, revoke any existing API key for the user before creating a new one.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhooks
<details><summary><code>client.webhooks.<a href="src/polytomic/webhooks/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the webhooks for the caller's organization.

> 📘 One webhook per organization
>
> An organization can register a single webhook, which receives every event
> produced in that organization. See the
> [Events documentation](../../guides/events) for the
> list of event types and payload shapes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.webhooks.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/polytomic/webhooks/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates the organization's webhook.

> 📘 One webhook per organization
>
> An organization can register a single webhook, which receives every event
> produced in that organization. See the
> [Events documentation](../../guides/events) for the
> list of event types and payload shapes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.webhooks.create(
    endpoint="https://example.com/webhook",
    secret="secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**endpoint:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/polytomic/webhooks/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single webhook by ID.

> 📘 One webhook per organization
>
> An organization can register a single webhook, which receives every event
> produced in that organization. See the
> [Events documentation](../../../guides/events) for the
> list of event types and payload shapes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.webhooks.get(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/polytomic/webhooks/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing webhook.

> 📘 One webhook per organization
>
> An organization can register a single webhook, which receives every event
> produced in that organization. See the
> [Events documentation](../../../guides/events) for the
> list of event types and payload shapes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.webhooks.update(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    endpoint="https://example.com/webhook",
    secret="secret",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**endpoint:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**secret:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/polytomic/webhooks/client.py">remove</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a webhook.

> 📘 One webhook per organization
>
> An organization can register a single webhook, which receives every event
> produced in that organization. See the
> [Events documentation](../../../guides/events) for the
> list of event types and payload shapes.

Deletion is permanent. To stop delivery without losing the webhook
configuration, use
[`POST /api/webhooks/{id}/disable`](./disable/post) instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.webhooks.remove(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/polytomic/webhooks/client.py">disable</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disables a webhook without deleting it.

> 📘 One webhook per organization
>
> An organization can register a single webhook, which receives every event
> produced in that organization. See the
> [Events documentation](../../../../guides/events) for the
> list of event types and payload shapes.

Events are not queued while the webhook is disabled — any activity that occurs
during the disabled period is not delivered retroactively. To resume
delivery, re-enable the webhook using
[`POST /api/webhooks/{id}/enable`](../../../../api-reference/webhooks/enable).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.webhooks.disable(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/polytomic/webhooks/client.py">enable</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Re-enables a previously disabled webhook.

> 📘 One webhook per organization
>
> An organization can register a single webhook, which receives every event
> produced in that organization. See the
> [Events documentation](../../../../guides/events) for the
> list of event types and payload shapes.

Delivery resumes from the next event generated after this call. Events that
occurred while the webhook was disabled are not replayed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.webhooks.enable(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## BulkSync Executions
<details><summary><code>client.bulk_sync.executions.<a href="src/polytomic/bulk_sync/executions/client.py">list_status</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a concise per-schema status for one or more bulk syncs.

This endpoint is a summary view, not an execution-history view. Each schema is
represented at most once with its most recent execution status, and running
executions are preferred over older terminal ones.

Use this endpoint when you want a dashboard-style answer to "what is each sync
doing now?" If you need the full execution history or a single execution's
details, use [`GET /api/bulk/syncs/{id}/executions`](./list) or
[`GET /api/bulk/syncs/{id}/executions/{exec_id}`](./get) instead.

Setting `all=true` or `active=true` ignores any explicit `sync_id` filters and
expands the request to the caller's organization scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.executions.list_status(
    all_=True,
    active=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**all_:** `typing.Optional[bool]` — When true, return status for every sync in the caller's organization. Overrides any sync_id values.
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — When true, return status only for active syncs in the caller's organization. Overrides any sync_id values.
    
</dd>
</dl>

<dl>
<dd>

**sync_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return status for the specified bulk sync. Repeat the parameter to target multiple syncs. Ignored if all or active is true.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.executions.<a href="src/polytomic/bulk_sync/executions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists executions for a bulk sync.

Results are ordered by start time descending by default. When more results are
available, the response includes an opaque `pagination.next_page_token`; pass it
back as the `page_token` query parameter to retrieve the next page. The `limit`
parameter is optional, and the maximum page size is 100 executions.

Use `only_terminal=true` to return only finished executions. In that mode,
executions are ordered by `updated_at` so recently completed runs appear first.

Use `ascending=true` to walk forward from the oldest execution instead of
starting with the newest execution.

For the full details of a single run — including per-schema execution status —
use [`GET /api/bulk/syncs/{id}/executions/{exec_id}`](../../../../../api-reference/bulk-sync/executions/get).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.executions.list(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    page_token="AmkYh8v0jR5B3kls2Qcc9y8MjrPmvR4CvaK7H0F4rEwqvg76K==",
    only_terminal=True,
    ascending=True,
    limit=100,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the bulk sync.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` — Pagination cursor returned in the previous response. Omit on the first request.
    
</dd>
</dl>

<dl>
<dd>

**only_terminal:** `typing.Optional[bool]` — When true, only return executions that have finished. Terminal executions are ordered by updated_at.
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` — When true, return executions from oldest to newest. Default is newest first.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of executions to return. Capped at 100.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.executions.<a href="src/polytomic/bulk_sync/executions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single bulk sync execution, including per-schema execution status.

The response includes a breakdown of each schema (table or object) that
participated in the execution, with its individual status, row counts, and any
error details. This makes it suitable for diagnosing partial failures where
some schemas succeeded while others did not.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.executions.get(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    exec_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the bulk sync.
    
</dd>
</dl>

<dl>
<dd>

**exec_id:** `str` — Unique identifier of the execution.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.executions.<a href="src/polytomic/bulk_sync/executions/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requests cancellation of a specific bulk sync execution.

Cancellation is asynchronous. A successful response means the cancellation
signal has been queued; the execution continues to run until the signal is
processed. Poll `GET /api/bulk/syncs/{id}/executions/{exec_id}` until the
execution reaches a terminal state (`completed`, `canceled`, or `failed`) to
confirm cancellation has taken effect.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.executions.cancel(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    exec_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The bulk sync ID.
    
</dd>
</dl>

<dl>
<dd>

**exec_id:** `str` — The execution ID to cancel.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.executions.<a href="src/polytomic/bulk_sync/executions/client.py">get_logs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns signed URLs for the log files produced by a single bulk sync execution.

Each URL in the response is pre-signed and grants temporary read access to the
corresponding log file. URLs expire after a short period; if you need to access
a file after the URL has expired, call this endpoint again to obtain a fresh set
of signed URLs.

> 📘 To export logs asynchronously to a destination of your choice, use
> [`POST /api/bulk/syncs/{sync_id}/executions/{execution_id}/logs/export`](../../../../../../../api-reference/bulk-sync/executions/export-logs)
> instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.executions.get_logs(
    sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    execution_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sync_id:** `str` — Unique identifier of the bulk sync.
    
</dd>
</dl>

<dl>
<dd>

**execution_id:** `str` — Unique identifier of the execution whose log files should be listed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.executions.<a href="src/polytomic/bulk_sync/executions/client.py">export_logs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts an asynchronous job that packages the log files for a single bulk sync execution into a downloadable archive.

> 📘 Log export is asynchronous
>
> This endpoint starts a background job that packages an execution's log
> files into a downloadable archive. The first call typically returns a
> `job` descriptor instead of a completed result. Poll
> [`GET /api/jobs/exportlogs/{id}`](../../../../../../../../api-reference/jobs/get)
> with the returned `job_id` until `status` is `done`; the final response
> contains a signed `url` that can be used to download the archive.
>
> Set `notify=true` to also email the requesting user when the archive is
> ready.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.executions.export_logs(
    sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    execution_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sync_id:** `str` — Unique identifier of the bulk sync.
    
</dd>
</dl>

<dl>
<dd>

**execution_id:** `str` — Unique identifier of the execution whose logs should be exported.
    
</dd>
</dl>

<dl>
<dd>

**notify:** `typing.Optional[bool]` — Send a notification to the user when the logs are ready for download.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## BulkSync Schemas
<details><summary><code>client.bulk_sync.schemas.<a href="src/polytomic/bulk_sync/schemas/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the schemas configured on a bulk sync.

This endpoint returns the schemas that have been added to and configured on this
specific bulk sync — not the full set of schemas available from the source
connection. To discover what the source connection exposes, use the source
schemas endpoint for the relevant connection type.

Each schema in the response includes its sync mode, field selections, and any
custom configuration applied via
[`PATCH /api/bulk/syncs/{id}/schemas`](../../../../../api-reference/bulk-sync/schemas/patch)
or
[`PUT /api/bulk/syncs/{id}/schemas/{schema_id}`](../../../../../api-reference/bulk-sync/schemas/update).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.schemas.list(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the bulk sync.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Optional filters applied to the returned schemas. Supports enabled=true to return only enabled schemas and enabled=false to return only disabled schemas.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.schemas.<a href="src/polytomic/bulk_sync/schemas/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches one or more schemas on a bulk sync at once.

Only schemas explicitly included in the request body are modified; schemas
omitted from the request are left unchanged. This makes PATCH the right choice
when you want to update a subset of tables without affecting the rest of the
sync's schema configuration.

Within each provided schema, omitting `fields` enables all available fields on
that schema. To control which fields are enabled, include the `fields` array
with explicit `enabled` values for each field.

> 📘 To replace a single schema's configuration in full (clearing any fields you
> omit), use
> [`PUT /api/bulk/syncs/{id}/schemas/{schema_id}`](../../../../../api-reference/bulk-sync/schemas/update)
> instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.schemas.patch(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the bulk sync.
    
</dd>
</dl>

<dl>
<dd>

**schemas:** `typing.Optional[typing.Sequence[BulkSchema]]` — Schemas to patch. Schemas are matched by id; only schemas present in this list are updated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.schemas.<a href="src/polytomic/bulk_sync/schemas/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the configuration of a single schema on a bulk sync.

Returns the sync mode, field selections, and any other configuration applied to
this schema on the bulk sync.

To modify the configuration, use
[`PATCH /api/bulk/syncs/{id}/schemas`](../../../../../../api-reference/bulk-sync/schemas/patch)
for a partial update across multiple schemas, or
[`PUT /api/bulk/syncs/{id}/schemas/{schema_id}`](../../../../../../api-reference/bulk-sync/schemas/update)
to fully replace this schema's configuration.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.schemas.get(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    schema_id="Contact",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the bulk sync.
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` — Source-side schema identifier.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.schemas.<a href="src/polytomic/bulk_sync/schemas/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces the configuration of a single schema on a bulk sync.

This is a full replacement: every field in the request body is written to the
schema, and any field you omit is cleared or reset to its default. Fetch the
current configuration with
[`GET /api/bulk/syncs/{id}/schemas/{schema_id}`](../../../../../../api-reference/bulk-sync/schemas/get)
first if you want to preserve existing settings while changing only a subset.

Omitting `fields` enables all available fields on the schema. To control which
fields are enabled, include the `fields` array with explicit `enabled` values.

> 📘 To update multiple schemas in a single request without affecting others,
> use the partial-update endpoint
> [`PATCH /api/bulk/syncs/{id}/schemas`](../../../../../../api-reference/bulk-sync/schemas/patch)
> instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.schemas.update(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    schema_id="contact",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the bulk sync.
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` — Source-side schema identifier.
    
</dd>
</dl>

<dl>
<dd>

**data_cutoff_timestamp:** `typing.Optional[dt.datetime]` — Per-schema cutoff. Records older than this timestamp are excluded from sync runs.
    
</dd>
</dl>

<dl>
<dd>

**disable_data_cutoff:** `typing.Optional[bool]` — When true, the sync ignores any configured data_cutoff_timestamp for this schema.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Whether this schema is included in sync runs.
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Sequence[UpdateBulkField]]` — Field-level configuration. Supplying an empty list enables every field discovered on the source.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Sequence[BulkFilter]]` — Row-level filters applied when reading from the source.
    
</dd>
</dl>

<dl>
<dd>

**partition_key:** `typing.Optional[str]` — Source field used to partition rows when writing to the destination.
    
</dd>
</dl>

<dl>
<dd>

**tracking_field:** `typing.Optional[str]` — Source field used to detect changes between incremental sync runs.
    
</dd>
</dl>

<dl>
<dd>

**user_output_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.schemas.<a href="src/polytomic/bulk_sync/schemas/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requests cancellation of any running executions for a specific schema on a bulk sync.

Cancellation is asynchronous. A successful response means the cancellation
signal for this schema has been queued; the schema's in-flight work continues
until the signal is processed. Poll
`GET /api/bulk/syncs/{id}/schemas/{schema_id}` and the parent execution via
`GET /api/bulk/syncs/{id}/status` to confirm the schema has reached a terminal
state.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.schemas.cancel(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    schema_id="schema_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The bulk sync ID.
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` — The schema ID to cancel for the bulk sync.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## BulkSync Schedules
<details><summary><code>client.bulk_sync.schedules.<a href="src/polytomic/bulk_sync/schedules/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all schedules configured for a bulk sync.

A bulk sync can have multiple schedules attached; this endpoint returns all
of them. Schedule times are returned in UTC.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.schedules.list(
    sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sync_id:** `str` — Unique identifier of the bulk sync whose schedules should be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.schedules.<a href="src/polytomic/bulk_sync/schedules/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new schedule to a bulk sync.

A bulk sync can have multiple schedules attached; adding one here does not
replace existing schedules. Schedule times are interpreted in UTC.

Creating a schedule only affects future automatic executions. To run the
sync immediately, call
[`POST /api/bulk/syncs/{id}/executions`](../../../../../api-reference/bulk-sync/start).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic, V4BulkSyncScheduleApi

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.schedules.create(
    sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    schedule=V4BulkSyncScheduleApi(
        frequency="manual",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sync_id:** `str` — Unique identifier of the bulk sync to add a schedule to.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `V4BulkSyncScheduleApi` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.schedules.<a href="src/polytomic/bulk_sync/schedules/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single schedule configured on a bulk sync.

Schedule times are returned in UTC.

To see all schedules on this sync, use
[`GET /api/bulk/syncs/{sync_id}/schedules`](../../../../../../api-reference/bulk-sync/schedules/list).
To update the schedule, use
[`PUT /api/bulk/syncs/{sync_id}/schedules/{schedule_id}`](../../../../../../api-reference/bulk-sync/schedules/update).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.schedules.get(
    sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    schedule_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sync_id:** `str` — Unique identifier of the bulk sync.
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `str` — Unique identifier of the schedule.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.schedules.<a href="src/polytomic/bulk_sync/schedules/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing schedule on a bulk sync.

Updates replace the stored schedule. Send the full schedule definition
rather than only the field you want to change. Schedule times are
interpreted in UTC.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic, V4BulkSyncScheduleApi

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.schedules.update(
    sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    schedule_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    schedule=V4BulkSyncScheduleApi(
        frequency="manual",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sync_id:** `str` — Unique identifier of the bulk sync.
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `str` — Unique identifier of the schedule to update.
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `V4BulkSyncScheduleApi` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.bulk_sync.schedules.<a href="src/polytomic/bulk_sync/schedules/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a schedule from a bulk sync.

Deleting a schedule only stops future automatic executions. It does not
cancel an execution that is already running.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.bulk_sync.schedules.delete(
    sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    schedule_id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sync_id:** `str` — Unique identifier of the bulk sync.
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `str` — Unique identifier of the schedule to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ModelSync Targets
<details><summary><code>client.model_sync.targets.<a href="src/polytomic/model_sync/targets/client.py">get_target</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns target metadata for a connection.

> 🚧 Deprecated
>
> Use `GET /api/connections/{id}/modelsync/targetobjects` instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.targets.get_target(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the connection.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — Target object type to query (e.g. schema name). When supplied, the response is narrowed to objects matching this type.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Substring filter applied to target object names. Combine with type to browse large schemas.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.targets.<a href="src/polytomic/model_sync/targets/client.py">get_target_fields</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the fields of a specific target object on a connection.

Pass the target object identifier to retrieve the fields available for
mapping on that object. These are the destination fields you can reference
when configuring field mappings in a model sync.

> 📘 To list available target objects and their identifiers, use
> [`GET /api/connections/{id}/modelsync/targetobjects`](../../../../../../api-reference/model-sync/targets/list).

Fields returned here reflect the connection's current cached state. If the
upstream object schema has changed, trigger a schema refresh with
[`POST /api/connections/{id}/schemas/refresh`](../../../../../../api-reference/schemas/refresh)
before calling this endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.targets.get_target_fields(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    target="database.table",
    refresh=False,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Unique identifier of the connection.
    
</dd>
</dl>

<dl>
<dd>

**target:** `str` — Identifier of the target object (e.g. schema.table for a database destination, object name for a SaaS destination).
    
</dd>
</dl>

<dl>
<dd>

**refresh:** `typing.Optional[bool]` — When true, force a cache refresh of the target's schema before returning its fields.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.targets.<a href="src/polytomic/model_sync/targets/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the target objects available on a connection for use as a model sync destination.

If the connection supports creating new destinations, the `target_creation`
object will contain information on what properties are required to create the
target.

Target creation properties are all string values; the `enum` flag indicates if
the property has a fixed set of valid values. When `enum` is `true`, the [Target
Creation Property
Values](../../../../../api-reference/model-sync/targets/get-create-property)
endpoint can be used to retrieve the valid values.

## Sync modes

The sync mode determines which records are written to the destination for a
model sync. The `modes` array for a target object defines the `id` along with
what operations the mode supports.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.targets.list(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.targets.<a href="src/polytomic/model_sync/targets/client.py">get_create_property</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the valid values for a target-creation property on a connection that supports creating new target objects.

Connections which support creating new sync target objects (destinations) will
return `target_creation` with their [target object list](./list). This endpoint
will return possible values for properties where `enum` is `true`.

If the connection does not support creating new target objects, an HTTP 404 will
be returned.

The `values` array lists the valid options (and labels) for the property. Each
member of the `values` array has a `label` and `value`. For exaample,

```json
{
  "data": [
    {
      "id": "account",
      "title": "Account ID",
      "enum": true,
      "values": [
        {
          "value": "1234567::urn:li:organization:987654",
          "label": "Polytomic Inc. (1234567)"
        }
      ]
    }
  ]
}
```

The `value` for the selected option should be passed when [creating a
sync](../../../../../../../api-reference/model-sync/create).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.targets.get_create_property(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    property="property",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**property:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ModelSync Executions
<details><summary><code>client.model_sync.executions.<a href="src/polytomic/model_sync/executions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists executions for a model sync.

Results are ordered by start time descending. If more results are available, the
response includes `pagination.next_page_token`; pass that token back unchanged
to continue paging.

The token is opaque. Do not construct or edit it yourself.

For full details about a specific execution — including record counts and error
summaries — use
[`GET /api/syncs/{sync_id}/executions/{id}`](./{id}/get).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.executions.list(
    sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    page_token="AmkYh8v0jR5B3kls2Qcc9y8MjrPmvR4CvaK7H0F4rEwqvg76K==",
    only_completed=True,
    ascending=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sync_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**only_completed:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.executions.<a href="src/polytomic/model_sync/executions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single model sync execution.

For the log files produced by this execution, use
[`GET /api/syncs/{sync_id}/executions/{id}/{type}`](../../../../../api-reference/model-sync/executions/get-log-urls) to retrieve
signed URLs grouped by log category.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.executions.get(
    sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sync_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.executions.<a href="src/polytomic/model_sync/executions/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a model sync execution's state, used to retry or resolve stalled executions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.executions.update(
    sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    status="created",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sync_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — The ID of the execution to update.
    
</dd>
</dl>

<dl>
<dd>

**status:** `ExecutionStatus` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.executions.<a href="src/polytomic/model_sync/executions/client.py">get_log_urls</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns signed URLs for every log file of a given type on a model sync execution.

`{type}` identifies the log category, such as `errors` or `warnings`. The
response contains a signed URL for each log file in that category.

> 🚧 Signed URLs expire after a short period. If a URL has expired, re-request
> it from this endpoint. To fetch a single file's URL directly, use
> [`GET /api/syncs/{sync_id}/executions/{id}/{type}/{filename}`](../../../../../../api-reference/model-sync/executions/get-logs).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.executions.get_log_urls(
    sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    type="records",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sync_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `V2ExecutionLogType` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_sync.executions.<a href="src/polytomic/model_sync/executions/client.py">get_logs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a signed URL for a specific log file produced by a model sync execution.

The URL is signed and expires after a short period. If it has expired before
you download the file, call this endpoint again to obtain a fresh URL.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.model_sync.executions.get_logs(
    sync_id="248df4b7-aa70-47b8-a036-33ac447e668d",
    id="0ecd09c1-b901-4d27-9053-f0367c427254",
    type="records",
    filename="path/to/file.json",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sync_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `V2ExecutionLogType` 
    
</dd>
</dl>

<dl>
<dd>

**filename:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Permissions Policies
<details><summary><code>client.permissions.policies.<a href="src/polytomic/permissions/policies/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all policies in the caller's organization.

Each policy binds one or more roles to a set of resources, controlling what
actions members with those roles can perform on those resources.

To inspect a specific policy in detail, use
[`GET /api/permissions/policies/{id}`](./%7Bid%7D/get).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.permissions.policies.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.permissions.policies.<a href="src/polytomic/permissions/policies/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new policy.

A policy binds one or more roles to a set of resources, granting members who
hold those roles the actions defined by them. Roles must already exist before
they are referenced in a policy; create roles using
[`POST /api/permissions/roles`](../../../api-reference/permissions/roles/create).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.permissions.policies.create(
    name="Custom",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**policy_actions:** `typing.Optional[typing.Sequence[PolicyAction]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.permissions.policies.<a href="src/polytomic/permissions/policies/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single policy by ID, including all action/role bindings it defines.

Returns the full set of action/role bindings defined by the policy, including
the resources it applies to.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.permissions.policies.get(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.permissions.policies.<a href="src/polytomic/permissions/policies/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing policy.

The update is a **full replacement** of the policy's bindings. Any role or
resource binding not included in the request body is removed. To make a
partial change, fetch the current policy with
[`GET /api/permissions/policies/{id}`](./get), modify the relevant bindings,
and send the complete object back.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.permissions.policies.update(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    name="Custom",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**policy_actions:** `typing.Optional[typing.Sequence[PolicyAction]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.permissions.policies.<a href="src/polytomic/permissions/policies/client.py">remove</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a policy.

Deletion is permanent. Any access that was granted solely through this policy
is revoked immediately for all users who depended on it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.permissions.policies.remove(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Permissions Roles
<details><summary><code>client.permissions.roles.<a href="src/polytomic/permissions/roles/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all permissions roles available in the caller's organization, including built-in system roles.

System roles such as Admin and Member are always present in every organization
and cannot be modified or deleted. Custom roles appear alongside them and can
be created, updated, or removed as needed.

To inspect or modify a specific role, use
[`GET /api/permissions/roles/{id}`](./%7Bid%7D/get).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.permissions.roles.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.permissions.roles.<a href="src/polytomic/permissions/roles/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new permissions role.

Provide a `name` for the new role. The role is immediately available for use
in permission policies.

To attach the role to resources, create or update a policy using
[`POST /api/permissions/policies`](../../../api-reference/permissions/policies/create).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.permissions.roles.create(
    name="Custom",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.permissions.roles.<a href="src/polytomic/permissions/roles/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single permissions role by ID.

Returns the role's name, action set, and whether it is a built-in system role.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.permissions.roles.get(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.permissions.roles.<a href="src/polytomic/permissions/roles/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing permissions role's name and action set.

The update is a **full replacement** of the role definition.

> 🚧 Built-in system roles (such as Admin and Member) cannot be updated.
> Attempting to modify a system role returns an error.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.permissions.roles.update(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
    name="Custom",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.permissions.roles.<a href="src/polytomic/permissions/roles/client.py">remove</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a permissions role.

> 🚧 Built-in system roles (such as Admin and Member) cannot be deleted.
> Attempting to delete a system role returns an error.

Deleting a role does not automatically remove it from any policies that
reference it. Update those policies separately using
[`PUT /api/permissions/policies/{id}`](../../../../api-reference/permissions/policies/update) to avoid
leaving stale role references.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from polytomic import Polytomic

client = Polytomic(
    version="YOUR_VERSION",
    token="YOUR_TOKEN",
)
client.permissions.roles.remove(
    id="248df4b7-aa70-47b8-a036-33ac447e668d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

