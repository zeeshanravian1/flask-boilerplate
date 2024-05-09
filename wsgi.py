"""
WSGI entry point for application.

Description:
    - This module contains WSGI entry point for application.
    - It initializes Flask application and creates database tables.

"""

from flask import Flask

from flask_boilerplate.apis.role import role_router
from flask_boilerplate.app import create_app
from flask_boilerplate.core.config import PROJECT_TITLE

# Create Flask application object
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
