class ApiException(Exception):
    # base class for all exceptions on api

    def __init__(self, msg, status_code):
        super().__init__(msg)
        self.msg = msg
        self.status_code = status_code


class ValidationError(ApiException):
    # exception for server validations errors

    def __init__(self, msg="Validation failed", status_code=400):
        super().__init__(msg, status_code)


class NotFoundError(ApiException):
    # exception for not found document/data in server

    def __init__(self, msg="Data not found", status_code=404):
        super().__init__(msg, status_code)


class ConflictError(ApiException):
    # exception for resource with association to another resource

    def __init__(self, msg="Conflict error with resources", status_code=409):
        super().__init__(msg, status_code)


class AuthorizationError(ApiException):
    # exception for not authorized users

    def __init__(self, msg="Unauthorized access", status_code=401):
        super().__init__(msg, status_code)
