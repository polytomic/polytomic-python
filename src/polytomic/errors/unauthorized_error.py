# This file was auto-generated from our API Definition.

from ..core.api_error import ApiError
from ..types.rest_err_response import RestErrResponse


class UnauthorizedError(ApiError):
    def __init__(self, body: RestErrResponse):
        super().__init__(status_code=401, body=body)
