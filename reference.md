# Reference
## BulkSync
<details><summary><code>client.bulk_sync.<a href="src/polytomic/bulk_sync/client.py">list</a>(...)</code></summary>
<dl>
<dd>

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

**active:** `typing.Optional[bool]` 
    
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

Create a new Bulk Sync from a source to a destination (data warehouse, database, or cloud storage bucket like S3).

Bulk Syncs are used for the ELT pattern (Extract, Load, and Transform), where you want to sync un-transformed data to your data warehouses, databases, or cloud storage buckets like S3.

All of the functionality described in [the product
documentation](https://docs.polytomic.com/docs/bulk-syncs) is configurable via
the API.

Sample code examples:

- [Bulk sync (ELT) from Salesforce to S3](https://apidocs.polytomic.com/guides/code-examples/bulk-sync-elt-from-salesforce-to-s-3)
- [Bulk sync (ELT) from Salesforce to Snowflake](https://apidocs.polytomic.com/guides/code-examples/bulk-sync-elt-from-salesforce-to-snowflake)
- [Bulk sync (ELT) from HubSpot to PostgreSQL](https://apidocs.polytomic.com/guides/code-examples/bulk-sync-elt-from-hub-spot-to-postgre-sql)

## Connection specific configuration

The `destination_configuration` is integration-specific configuration for the
selected bulk sync destination. This includes settings such as the output schema
and is required when creating a new sync.

The `source_configuration` is optional. It allows configuration for how
Polytomic reads data from the source connection. This will not be available for
integrations that do not support additional configuration.

Consult the [connection configurations](https://apidocs.polytomic.com/2024-02-08/guides/configuring-your-connections/overview)
to see configurations for particular integrations (for example, [here](https://apidocs.polytomic.com/2024-02-08/guides/configuring-your-connections/connections/postgre-sql#source-1) is the available source configuration for the PostgreSQL bulk sync source).
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

> 📘 Updating schemas
>
> Schema updates can be performed using the [Update Bulk Sync Schemas](https://apidocs.polytomic.com/api-reference/bulk-sync/schemas/patch) endpoint.
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

<details><summary><code>client.bulk_sync.<a href="src/polytomic/bulk_sync/client.py">start</a>(...)</code></summary>
<dl>
<dd>

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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fetch_mode:** `typing.Optional[BulkFetchMode]` 
    
</dd>
</dl>

<dl>
<dd>

**resync:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**schemas:** `typing.Optional[typing.Sequence[str]]` 
    
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

<details><summary><code>client.bulk_sync.<a href="src/polytomic/bulk_sync/client.py">get_status</a>(...)</code></summary>
<dl>
<dd>

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

<details><summary><code>client.bulk_sync.<a href="src/polytomic/bulk_sync/client.py">get_source</a>(...)</code></summary>
<dl>
<dd>

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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**include_fields:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.connections.<a href="src/polytomic/connections/client.py">list</a>()</code></summary>
<dl>
<dd>

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

Creates a new request for [Polytomic Connect](https://www.polytomic.com/connect).

This endpoint configures a Polytomic Connect request and returns the URL to
redirect users to. This allows embedding Polytomic connection authorization in
other applications.

See also:

- [Embedding authentication](https://apidocs.polytomic.com/2024-02-08/guides/embedding-authentication), a guide to using Polytomic Connect.
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

## QueryRunner
<details><summary><code>client.query_runner.<a href="src/polytomic/query_runner/client.py">run_query</a>(...)</code></summary>
<dl>
<dd>

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

**connection_id:** `str` 
    
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[str]` 
    
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

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Sequence[V4UserFieldRequest]]` 
    
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

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**field_id:** `str` 
    
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

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Sequence[SchemaPrimaryKeyOverrideInput]]` 
    
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

Delete all primary key overrides for a schema. After this call the schema will use the primary keys detected from the source connection, if any.
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

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` 
    
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

<details><summary><code>client.schemas.<a href="src/polytomic/schemas/client.py">get_status</a>(...)</code></summary>
<dl>
<dd>

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

<details><summary><code>client.schemas.<a href="src/polytomic/schemas/client.py">get</a>(...)</code></summary>
<dl>
<dd>

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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` 
    
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` 
    
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Sequence[str]]]]` 
    
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

For a given connection and enrichment configuration, provides the valid sets of input fields.
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

Returns sample records from the model. The first ten records that the source provides will be returned after being enriched (if applicable). Synchronous requests must complete within 10s. If either querying or enrichment exceeds 10s, please use the async option.
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Sequence[str]]]]` 
    
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Sequence[str]]]]` 
    
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

Create a new sync from one or more models to a destination.

All of the functionality described in [the product
documentation](https://docs.polytomic.com/docs/sync-destinations) is
configurable via the API.

Guides:

- [Model sync (Reverse ETL) from Snowflake query to Salesforce](https://apidocs.polytomic.com/2024-02-08/guides/code-examples/model-sync-reverse-etl-from-snowflake-query-to-salesforce)
- [Joined model sync from Postgres, Airtable, and Stripe to Hubspot](https://apidocs.polytomic.com/2024-02-08/guides/code-examples/joined-model-sync-from-postgres-airtable-and-stripe-to-hubspot)

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
connections](https://apidocs.polytomic.com/2024-02-08/guides/configuring-your-connections/connections/salesforce#target)
support optionally specifying the ingestion API to use. The target specific
options are passed as `configuration`; consult the [integration
guides](https://apidocs.polytomic.com/2024-02-08/guides/configuring-your-connections/overview)
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

**organization_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**ending_before:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` 
    
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

Returns information about the caller's identity.
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

## Organization
<details><summary><code>client.organization.<a href="src/polytomic/organization/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

> 🚧 Requires partner key
>
> Organization endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).
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

> 🚧 Requires partner key
>
> Organization endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**issuer:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sso_domain:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sso_org_id:** `typing.Optional[str]` 
    
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

> 🚧 Requires partner key
>
> Organization endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).
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

<details><summary><code>client.organization.<a href="src/polytomic/organization/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

> 🚧 Requires partner key
>
> Organization endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).
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

**client_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**issuer:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sso_domain:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sso_org_id:** `typing.Optional[str]` 
    
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

> 🚧 Requires partner key
>
> Organization endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).
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

## Users
<details><summary><code>client.users.<a href="src/polytomic/users/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

> 🚧 Requires partner key
>
> User endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).
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

**org_id:** `str` 
    
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

> 🚧 Requires partner key
>
> User endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).
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

**org_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` 
    
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

> 🚧 Requires partner key
>
> User endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `str` 
    
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

> 🚧 Requires partner key
>
> User endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` 
    
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

> 🚧 Requires partner key
>
> User endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `str` 
    
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

> 🚧 Requires partner key
>
> User endpoints are only accessible using [partner keys](https://apidocs.polytomic.com/guides/obtaining-api-keys#partner-keys).
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

**org_id:** `str` 
    
</dd>
</dl>

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

## Webhooks
<details><summary><code>client.webhooks.<a href="src/polytomic/webhooks/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Webooks can be set up using the webhook API endpoints. Currently, only one
webhook may be created per organization. The webhook will be called for events
in that organization.

Consult the [Events documentation](https://apidocs.polytomic.com/guides/events) for more information.
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

Webooks can be set up using the webhook API endpoints. Currently, only one
webhook may be created per organization. The webhook will be called for events
in that organization.

Consult the [Events documentation](https://apidocs.polytomic.com/guides/events) for more information.
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

Webooks can be set up using the webhook API endpoints. Currently, only one
webhook may be created per organization. The webhook will be called for events
in that organization.

Consult the [Events documentation](https://apidocs.polytomic.com/guides/events) for more information.
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

Webooks can be set up using the webhook API endpoints. Currently, only one
webhook may be created per organization. The webhook will be called for events
in that organization.

Consult the [Events documentation](https://apidocs.polytomic.com/guides/events) for more information.
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

**all_:** `typing.Optional[bool]` — Return the execution status of all syncs in the organization
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Return the execution status of all active syncs in the organization
    
</dd>
</dl>

<dl>
<dd>

**sync_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return the execution status of the specified sync; this may be supplied multiple times.
    
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**only_terminal:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**exec_id:** `str` 
    
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

**sync_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**execution_id:** `str` 
    
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

**sync_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**execution_id:** `str` 
    
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schemas:** `typing.Optional[typing.Sequence[BulkSchema]]` 
    
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` 
    
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schema_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**data_cutoff_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**disable_data_cutoff:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Sequence[UpdateBulkField]]` 
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Sequence[BulkFilter]]` 
    
</dd>
</dl>

<dl>
<dd>

**partition_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tracking_field:** `typing.Optional[str]` 
    
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

## BulkSync Schedules
<details><summary><code>client.bulk_sync.schedules.<a href="src/polytomic/bulk_sync/schedules/client.py">list</a>(...)</code></summary>
<dl>
<dd>

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

**sync_id:** `str` 
    
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

**sync_id:** `str` 
    
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

**sync_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `str` 
    
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

**sync_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `str` 
    
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

**sync_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**schedule_id:** `str` 
    
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
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

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**target:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**refresh:** `typing.Optional[bool]` 
    
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

Returns available model sync destinations for a connection.

If the connection supports creating new destinations, the `target_creation`
object will contain information on what properties are required to create the
target.

Target creation properties are all string values; the `enum` flag indicates if
the property has a fixed set of valid values. When `enum` is `true`, the [Target
Creation Property
Values](https://apidocs.polytomic.com/2024-02-08/api-reference/model-sync/targets/get-create-property)
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
sync](https://apidocs.polytomic.com/2024-02-08/api-reference/model-sync/create).
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

