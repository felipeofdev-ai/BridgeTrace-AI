"""Custom exceptions."""
from typing import Any, Optional
from fastapi import HTTPException, status

class BridgeTraceException(Exception):
    def __init__(self, message: str, code: Optional[str] = None, details: Optional[dict] = None):
        self.message = message
        self.code = code or self.__class__.__name__
        self.details = details or {}
        super().__init__(self.message)

class ValidationError(BridgeTraceException):
    pass

class NotFoundError(BridgeTraceException):
    pass

class AuthenticationError(BridgeTraceException):
    pass

def exception_to_http(exc: BridgeTraceException) -> HTTPException:
    status_map = {
        ValidationError: status.HTTP_400_BAD_REQUEST,
        NotFoundError: status.HTTP_404_NOT_FOUND,
        AuthenticationError: status.HTTP_401_UNAUTHORIZED,
    }
    code = status_map.get(type(exc), status.HTTP_500_INTERNAL_SERVER_ERROR)
    return HTTPException(status_code=code, detail={"message": exc.message, "code": exc.code})
