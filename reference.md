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

**data_cutoff_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**destination_configuration:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
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

**mode:** `typing.Optional[SyncMode]` 
    
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

**data_cutoff_timestamp:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**destination_configuration:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
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

**mode:** `typing.Optional[SyncMode]` 
    
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
        "password": "password",
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

**name:** `str` — Name of the new connection.
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `str` — URL to redirect to after connection is created.
    
</dd>
</dl>

<dl>
<dd>

**connection:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**dark:** `typing.Optional[bool]` 
    
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
        "password": "password",
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

<details><summary><code>client.model_sync.<a href="src/polytomic/model_sync/client.py">get_target</a>(...)</code></summary>
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
client.model_sync.get_target(
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

<details><summary><code>client.model_sync.<a href="src/polytomic/model_sync/client.py">get_target_fields</a>(...)</code></summary>
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
client.model_sync.get_target_fields(
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

<details><summary><code>client.model_sync.<a href="src/polytomic/model_sync/client.py">get_target_objects</a>(...)</code></summary>
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
client.model_sync.get_target_objects(
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

**mode:** `typing.Optional[SyncMode]` 
    
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
        object="Users",
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

**fields:** `typing.Sequence[ModelSyncField]` — Fields to sync from source to target.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `str` 
    
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

**active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**enricher:** `typing.Optional[Enrichment]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_logic:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Sequence[Filter]]` 
    
</dd>
</dl>

<dl>
<dd>

**identity:** `typing.Optional[Identity]` 
    
</dd>
</dl>

<dl>
<dd>

**only_enrich_updates:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
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

**skip_initial_backfill:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**sync_all_records:** `typing.Optional[bool]` 
    
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
        object="Users",
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

**fields:** `typing.Sequence[ModelSyncField]` — Fields to sync from source to target.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `str` 
    
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

**active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**enricher:** `typing.Optional[Enrichment]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_logic:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Sequence[Filter]]` 
    
</dd>
</dl>

<dl>
<dd>

**identity:** `typing.Optional[Identity]` 
    
</dd>
</dl>

<dl>
<dd>

**only_enrich_updates:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**organization_id:** `typing.Optional[str]` 
    
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

**skip_initial_backfill:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**sync_all_records:** `typing.Optional[bool]` 
    
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

## Schemas
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

Consult the [Events documentation](https://apidocs.polytomic.com/getting-started/events) for more information.
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

Consult the [Events documentation](https://apidocs.polytomic.com/getting-started/events) for more information.
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

Consult the [Events documentation](https://apidocs.polytomic.com/getting-started/events) for more information.
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

Consult the [Events documentation](https://apidocs.polytomic.com/getting-started/events) for more information.
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

**fields:** `typing.Optional[typing.Sequence[BulkField]]` 
    
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

