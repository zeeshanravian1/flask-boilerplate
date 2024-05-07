# -*- coding: utf-8 -*-
"""
Main Module

Description:
    - This module is the main entry point for the application.
    - It creates a Flask application and adds resources to it.

"""

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    """
    HelloWorld Resource

    Description:
        - This resource returns a simple JSON response.

    """

    def get(self) -> dict[str, str]:
        """
        GET Method

        Description:
            - This method returns a simple JSON response.

        Args:
            - `None`

        Returns:
            - `dict[str, str]`: A simple JSON response

        Raises:
            - `None`

        """

        return {"hello": "world"}


api.add_resource(HelloWorld, "/")

if __name__ == "__main__":
    app.run(debug=True)
