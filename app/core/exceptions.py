"""Custom domain exceptions for BridgeTrace."""

from typing import Optional

from fastapi import HTTPException, status


class BridgeTraceException(Exception):
    """Base exception for known application failures."""

    def __init__(self, message: str, code: Optional[str] = None, details: Optional[dict] = None):
        self.message = message
        self.code = code or self.__class__.__name__
        self.details = details or {}
        super().__init__(self.message)


class ValidationError(BridgeTraceException):
    """Raised when request/domain validation fails."""


class NotFoundError(BridgeTraceException):
    """Raised when expected resources are not found."""


class AuthenticationError(BridgeTraceException):
    """Raised for authentication failures."""


class GraphTraversalError(BridgeTraceException):
    """Raised when graph traversal cannot be completed safely."""


def exception_to_http(exc: BridgeTraceException) -> HTTPException:
    """Map domain exceptions to HTTP-friendly errors."""

    status_map = {
        ValidationError: status.HTTP_400_BAD_REQUEST,
        NotFoundError: status.HTTP_404_NOT_FOUND,
        AuthenticationError: status.HTTP_401_UNAUTHORIZED,
        GraphTraversalError: status.HTTP_422_UNPROCESSABLE_ENTITY,
    }
    code = status_map.get(type(exc), status.HTTP_500_INTERNAL_SERVER_ERROR)
    return HTTPException(
        status_code=code,
        detail={"message": exc.message, "code": exc.code, "details": exc.details},
    )
