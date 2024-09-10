class ValidationError(Exception):
    # exception for server validations errors

    def __init__(self, msg, status_code=400):
        super().__init__(msg)
        self.status_code = status_code
        self.msg = msg


class NotFoundError(Exception):
    # exception for not found document/data in server

    def __init__(self, msg, status_code=404):
        super().__init__(msg)
        self.status_code = status_code
        self.msg = msg


class ConflictError(Exception):
    # exception for resource with association to another resource

    def __init__(self, msg, status_code=409):
        super().__init__(msg)
        self.status_code = status_code
        self.msg = msg
