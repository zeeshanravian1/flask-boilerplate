# -*- coding: utf-8 -*-
"""
WSGI entry point for the application.

Description:
    - This module contains the WSGI entry point for the application.
    - It initializes the Flask application and creates the database tables.

"""

from flask import Flask

from flask_boilerplate.apis.role import role_router
from flask_boilerplate.app import create_app
from flask_boilerplate.core.config import PROJECT_TITLE

# Create the Flask application object
app: Flask = create_app()


@app.route("/")
def index() -> dict[str, str]:
    """
    Root

    Description:
        - This function is used to create root route.

    Args:
        - `None`

    Returns:
        - `None`

    """

    return {"detail": f"Welcome to {PROJECT_TITLE}"}


# Register routers
app.register_blueprint(role_router)
