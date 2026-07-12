from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from backend.auth.exceptions import ForbiddenException, InactiveUserException, InvalidCredentialsException, UnauthorizedException, UserAlreadyExistsException


async def invalid_credentials_exception_handler(
    request: Request,
    exc: InvalidCredentialsException,
):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "success": False,
            "message": "Invalid username or password.",
        },
    )


async def inactive_user_exception_handler(
    request: Request,
    exc: InactiveUserException,
):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            "success": False,
            "message": "Your account has been deactivated.",
        },
    )


async def unauthorized_exception_handler(
    request: Request,
    exc: UnauthorizedException,
):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "success": False,
            "message": "Authentication required.",
        },
    )


async def forbidden_exception_handler(
    request: Request,
    exc: ForbiddenException,
):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            "success": False,
            "message": "You do not have permission to perform this action.",
        },
    )

async def user_already_exists_exception_handler(
    request: Request,
    exc: UserAlreadyExistsException,
):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "success": False,
            "message": "User already exists.",
        },
    )

def register_exception_handlers(app: FastAPI) -> None:
    """
    Register all global exception handlers.
    """

    app.add_exception_handler(
        InvalidCredentialsException,
        invalid_credentials_exception_handler,
    )

    app.add_exception_handler(
        InactiveUserException,
        inactive_user_exception_handler,
    )

    app.add_exception_handler(
        UnauthorizedException,
        unauthorized_exception_handler,
    )

    app.add_exception_handler(
        ForbiddenException,
        forbidden_exception_handler,
    )

    app.add_exception_handler(
        UserAlreadyExistsException,
        user_already_exists_exception_handler,
    )