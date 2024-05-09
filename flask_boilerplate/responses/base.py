"""
Base Response

Description:
    - This module contains shared responses used by all repositories.

"""

import json
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
            json.dumps({"success": True, "data": data}),
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
            json.dumps({"success": True, "data": data}),
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
            json.dumps({"success": True, "data": data}),
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
            json.dumps({"success": True, "data": data}),
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
            json.dumps({"success": True}),
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
            - `data (dict)`: Data object. **(Required)**

        Returns:
            - `response (tuple)`: Response tuple.

        """

        return (
            json.dumps({"success": False, "message": f"{data} not found"}),
            HTTPStatus.NOT_FOUND,
            CONTENT_TYPE_JSON,
        )
