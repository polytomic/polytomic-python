# This file was auto-generated from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import PolytomicEnvironment
from .resources.bulk_sync.client import AsyncBulkSyncClient, BulkSyncClient
from .resources.connections.client import AsyncConnectionsClient, ConnectionsClient
from .resources.events.client import AsyncEventsClient, EventsClient
from .resources.identity.client import AsyncIdentityClient, IdentityClient
from .resources.jobs.client import AsyncJobsClient, JobsClient
from .resources.model_sync.client import AsyncModelSyncClient, ModelSyncClient
from .resources.models.client import AsyncModelsClient, ModelsClient
from .resources.organization.client import AsyncOrganizationClient, OrganizationClient
from .resources.permissions.client import AsyncPermissionsClient, PermissionsClient
from .resources.schemas.client import AsyncSchemasClient, SchemasClient
from .resources.users.client import AsyncUsersClient, UsersClient
from .resources.webhooks.client import AsyncWebhooksClient, WebhooksClient


class Polytomic:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - base_url: typing.Optional[str]. The base url to use for requests from the client.

        - environment: PolytomicEnvironment. The environment to use for requests from the client. from .environment import PolytomicEnvironment

                                             Defaults to PolytomicEnvironment.DEFAULT

        - token: typing.Union[str, typing.Callable[[], str]].

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

        - httpx_client: typing.Optional[httpx.Client]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.
    ---
    from polytomic.client import Polytomic

    client = Polytomic(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: PolytomicEnvironment = PolytomicEnvironment.DEFAULT,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = None,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx.Client(timeout=_defaulted_timeout) if httpx_client is None else httpx_client,
            timeout=_defaulted_timeout,
        )
        self.bulk_sync = BulkSyncClient(client_wrapper=self._client_wrapper)
        self.connections = ConnectionsClient(client_wrapper=self._client_wrapper)
        self.model_sync = ModelSyncClient(client_wrapper=self._client_wrapper)
        self.schemas = SchemasClient(client_wrapper=self._client_wrapper)
        self.events = EventsClient(client_wrapper=self._client_wrapper)
        self.jobs = JobsClient(client_wrapper=self._client_wrapper)
        self.identity = IdentityClient(client_wrapper=self._client_wrapper)
        self.models = ModelsClient(client_wrapper=self._client_wrapper)
        self.organization = OrganizationClient(client_wrapper=self._client_wrapper)
        self.users = UsersClient(client_wrapper=self._client_wrapper)
        self.permissions = PermissionsClient(client_wrapper=self._client_wrapper)
        self.webhooks = WebhooksClient(client_wrapper=self._client_wrapper)


class AsyncPolytomic:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - base_url: typing.Optional[str]. The base url to use for requests from the client.

        - environment: PolytomicEnvironment. The environment to use for requests from the client. from .environment import PolytomicEnvironment

                                             Defaults to PolytomicEnvironment.DEFAULT

        - token: typing.Union[str, typing.Callable[[], str]].

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

        - httpx_client: typing.Optional[httpx.AsyncClient]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.
    ---
    from polytomic.client import AsyncPolytomic

    client = AsyncPolytomic(
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: PolytomicEnvironment = PolytomicEnvironment.DEFAULT,
        token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = None,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            token=token,
            httpx_client=httpx.AsyncClient(timeout=_defaulted_timeout) if httpx_client is None else httpx_client,
            timeout=_defaulted_timeout,
        )
        self.bulk_sync = AsyncBulkSyncClient(client_wrapper=self._client_wrapper)
        self.connections = AsyncConnectionsClient(client_wrapper=self._client_wrapper)
        self.model_sync = AsyncModelSyncClient(client_wrapper=self._client_wrapper)
        self.schemas = AsyncSchemasClient(client_wrapper=self._client_wrapper)
        self.events = AsyncEventsClient(client_wrapper=self._client_wrapper)
        self.jobs = AsyncJobsClient(client_wrapper=self._client_wrapper)
        self.identity = AsyncIdentityClient(client_wrapper=self._client_wrapper)
        self.models = AsyncModelsClient(client_wrapper=self._client_wrapper)
        self.organization = AsyncOrganizationClient(client_wrapper=self._client_wrapper)
        self.users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        self.permissions = AsyncPermissionsClient(client_wrapper=self._client_wrapper)
        self.webhooks = AsyncWebhooksClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: PolytomicEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
