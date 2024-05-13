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

from flask import Flask, jsonify
from psycopg2.errors import (
    ForeignKeyViolation,  # pylint: disable=E0611
    NotNullViolation,
    UniqueViolation,
)
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import HTTPException


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
            - `Any`: The JSON response with the error message and status code.

        """

        status_code: int | None = HTTPStatus.INTERNAL_SERVER_ERROR
        success: bool = False
        err_message: str | None = "Internal Server Error"

        # Handle specific exceptions
        if isinstance(err, IntegrityError):
            status_code = HTTPStatus.CONFLICT
            if isinstance(err.orig, NotNullViolation):
                match: re.Match[str] | None = re.search(
                    pattern=r'"([^"]+)"', string=str(err.orig)
                )
                if match:
                    err_message = f"{match.group(1)} can't be null"

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

            else:
                err_message = "Integrity Error"

        if isinstance(err, HTTPException):
            status_code = err.code
            err_message = err.description

        response: dict[str, str | bool | None] = {
            "success": success,
            "message": err_message,
        }

        return jsonify(response), status_code
