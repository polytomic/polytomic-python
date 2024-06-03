# This file was auto-generated from our API Definition.

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .policies.client import AsyncPoliciesClient, PoliciesClient
from .roles.client import AsyncRolesClient, RolesClient


class PermissionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.policies = PoliciesClient(client_wrapper=self._client_wrapper)
        self.roles = RolesClient(client_wrapper=self._client_wrapper)


class AsyncPermissionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.policies = AsyncPoliciesClient(client_wrapper=self._client_wrapper)
        self.roles = AsyncRolesClient(client_wrapper=self._client_wrapper)
