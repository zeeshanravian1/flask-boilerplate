"""
Middleware Module

Description:
    - This module contains the middleware classes that can be used to handle
    exceptions, logging, etc.
    - The CustomExceptionHandler class is used to handle exceptions and return
    a JSON response with the error message and status code.

"""

import re
from http import HTTPStatus
from logging import Logger

from flask import Flask, jsonify
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from psycopg2.errors import (  # pylint: disable=E0611
    ForeignKeyViolation,
    NotNullViolation,
    UniqueViolation,
)
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import HTTPException

from flask_boilerplate.constants.base import ERROR_MESSAGES
from flask_boilerplate.core.logger import AppLogger

logger: Logger = AppLogger().get_logger()


class ExceptionHandler:
    """
    Custom Exception Handler

    Description:
        - This class is used to handle exceptions and return a JSON response
        with the error message and status code.

    """

    def __init__(self, app) -> None:
        """
        Constructor

        Description:
            - This method initializes the ExceptionHandler class.
            - It registers the exception handler with the Flask application.

        Args:
            - `app (Flask)`: The Flask application instance.

        Returns:
            - `None`

        """

        self.app: Flask = app
        self.app.register_error_handler(Exception, self.handle_exception)

    def log_exception(self, err) -> None:
        """
        Log Exception

        Description:
            - This method logs the exceptions.

        Args:
            - `err (Exception)`: The exception object.

        Returns:
            - `None`
        """

        logger.error(err, exc_info=True)
        logger.info("********************************************************")

    def handle_exception(
        self, err
    ) -> tuple[dict[str, str | bool | None], int | None]:
        """
        Handle Exception

        Description:
            - This method handles the exceptions and returns a JSON response
            with the error message and status code.

        Args:
            - `err (Exception)`: The exception object.

        Returns:
            - `response (tuple)`: The JSON response with the error message and
            status code

        """

        # Default values
        status_code: int | None = HTTPStatus.INTERNAL_SERVER_ERROR
        success: bool = False
        err_message: str | None = ERROR_MESSAGES.get(
            str(HTTPStatus.INTERNAL_SERVER_ERROR)
        )

        # Handle Unauthorize Exception
        if isinstance(err, (ExpiredSignatureError, InvalidTokenError)):
            status_code = HTTPStatus.UNAUTHORIZED
            err_message = ERROR_MESSAGES.get(str(HTTPStatus.UNAUTHORIZED))

            self.log_exception(err)

        # Handle Integrity Exception
        elif isinstance(err, IntegrityError):
            status_code = HTTPStatus.CONFLICT

            # Hanlde NotNullViolation Exception
            if isinstance(err.orig, NotNullViolation):
                match: re.Match[str] | None = re.search(
                    pattern=r'"([^"]+)"', string=str(err.orig)
                )
                if match:
                    err_message = f"{match.group(1)} can't be null"

            # Handle ForeignKeyViolation and UniqueViolation Exception
            elif isinstance(err.orig, (ForeignKeyViolation, UniqueViolation)):
                err_message = (
                    str(err.orig)
                    .split("DETAIL:")[1]
                    .replace("Key", "")
                    .replace("(", "")
                    .replace(")", "")
                    .strip()
                )
                err_message = re.sub(
                    pattern=r"in table.*", repl="", string=err_message
                ).strip()

            # Handle other IntegrityError Exception
            else:
                err_message = ERROR_MESSAGES.get(str(HTTPStatus.CONFLICT))

        # Handle HTTPException
        elif isinstance(err, HTTPException):
            status_code = err.code
            err_message = err.description

            self.log_exception(err)

        # Handle other Exceptions
        else:
            self.log_exception(err)

        # Return JSON response
        return (
            jsonify(
                {
                    "success": success,
                    "message": err_message,
                }
            ),
            status_code,
        )
