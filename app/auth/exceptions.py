class AuthenticationException(Exception):
    """Base exception for authentication errors."""
    pass

class InvalidCredentialsException(AuthenticationException):
    """Raised when username or password is invalid."""
    pass

class InactiveUserException(AuthenticationException):
    """Raised when user account is inactive."""
    pass

class UnauthorizedException(AuthenticationException):
    """Raised when authentication is required."""
    pass

class ForbiddenException(AuthenticationException):
    """Raised when user lacks permission."""
    pass

class UserAlreadyExistsException(AuthenticationException):
    """Raised when username/email already exists."""
    pass