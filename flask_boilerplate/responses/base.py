"""
Base Response

Description:
    - This module contains shared responses used by all repositories.

"""

from typing import List
from http import HTTPStatus

from flask_boilerplate.constants.base import CONTENT_TYPE_JSON


class BaseResponse:
    """
    Base Response

    Description:
        - This is base response for all responses.

    """

    @staticmethod
    def create_response(data):
        """
        Create Response

        Description:
            - This is used to create response.

        Args:
            - `data (dict)`: Data object. **(Required)**

        Returns:
            - `response (tuple)`: Response tuple.

        """

        return (
            {"success": True, "data": data.to_dict()},
            HTTPStatus.CREATED,
            CONTENT_TYPE_JSON,
        )

    @staticmethod
    def read_response(data):
        """
        Read Response

        Description:
            - This is used to read response.

        Args:
            - `data (dict)`: Data object. **(Required)**

        Returns:
            - `response (tuple)`: Response tuple.

        """

        return (
            {"success": True, "data": data.to_dict()},
            HTTPStatus.OK,
            CONTENT_TYPE_JSON,
        )

    @staticmethod
    def read_all_response(data):
        """
        Read All Response

        Description:
            - This is used to read all response.

        Args:
            - `data (dict)`: Data object. **(Required)**

        Returns:
            - `response (tuple)`: Response tuple.

        """

        return (
            {"success": True, "data": [item.to_dict() for item in data]},
            HTTPStatus.OK,
            CONTENT_TYPE_JSON,
        )

    @staticmethod
    def update_response(data):
        """
        Update Response

        Description:
            - This is used to update response.

        Args:
            - `data (dict)`: Data object. **(Required)**

        Returns:
            - `response (tuple)`: Response tuple.

        """

        return (
            {"success": True, "data": data.to_dict()},
            HTTPStatus.ACCEPTED,
            CONTENT_TYPE_JSON,
        )

    @staticmethod
    def delete_response():
        """
        Delete Response

        Description:
            - This is used to delete response.

        Args:
            - `None`

        Returns:
            - `response (tuple)`: Response tuple.

        """

        return (
            {"success": True},
            HTTPStatus.NO_CONTENT,
            CONTENT_TYPE_JSON,
        )

    @staticmethod
    def not_found_response(data):
        """
        Not Found Response

        Description:
            - This is used to return not found response.

        Args:
            - `data (str)`: Model name. **(Required)**

        Returns:
            - `response (tuple)`: Response tuple.

        """

        return (
            {"success": False, "message": f"{data} not found"},
            HTTPStatus.NOT_FOUND,
            CONTENT_TYPE_JSON,
        )

    @staticmethod
    def success(data: List = [], total_rows: int = None):
        """
        Success Response

        Description:
            - This is used to return success response.

        Args:
            - `data (list)`:

        Returns:
            - `response (dict)`: Response dict.
        """
        response = {"success": True, "data": data}
        if total_rows is not None:
            response["total_rows"] = total_rows

        return response

    @staticmethod
    def failure(error):
        if not error:
            error = ["Something went wrong."]
        if isinstance(error, str):
            error = [error]
        return {"status": "nok", "errors": error}
