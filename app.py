"""
Application Factory Module

Description:
    - This module defines Flask application factory and basic configuration of
    application.
    - Application factory is a function that returns a Flask application
    instance.

"""

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restx import Api, Resource

from flask_boilerplate.apis.role import ns_role
from flask_boilerplate.apis.user import ns_user
from flask_boilerplate.apis.permission import ns_permission
from flask_boilerplate.apis.role_permission import ns_role_permission
from flask_boilerplate.core.config import (
    CORS_ALLOW_CREDENTIALS,
    CORS_ALLOW_HEADERS,
    CORS_ALLOW_METHODS,
    CORS_ALLOW_ORIGINS,
    DATABASE_URL,
    DOCS_URL,
    PROJECT_DESCRIPTION,
    PROJECT_TITLE,
    PROJECT_VERSION,
    SQLALCHEMY_TRACK_MODIFICATIONS,
    SWAGGER_AUTHORIZATIONS,
    SWAGGER_SECURITY,
    SWAGGER_UI_DOC_EXPANSION,
)
from flask_boilerplate.core.middlewares import ExceptionHandler
from flask_boilerplate.database.base import db
from flask_boilerplate.database.initialize_database import (
    add_permissions,
    add_roles,
    add_admin_permissions,
)

# Initialize Flask application instance
app = Flask(__name__)
app.app_context().push()

# Initialize ExceptionHandler instance
ExceptionHandler(app)

# Initialize RestX API instance
api = Api(
    app=app,
    doc=DOCS_URL,
    title=PROJECT_TITLE,
    description=PROJECT_DESCRIPTION,
    authorizations=SWAGGER_AUTHORIZATIONS,
    security=SWAGGER_SECURITY,
    version=PROJECT_VERSION,
)

# Configure application with database URL
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

# Disable SQLAlchemy track modifications
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

# Enable Swagger UI doc expansion
app.config["SWAGGER_UI_DOC_EXPANSION"] = SWAGGER_UI_DOC_EXPANSION

# Initialize app with SQLAlchemy database
db.init_app(app=app)

# Initialize Migrate instance
Migrate(app=app, db=db)

# Enable CORS
CORS(
    app=app,
    supports_credentials=CORS_ALLOW_CREDENTIALS,
    origins=CORS_ALLOW_ORIGINS.split(","),
    methods=CORS_ALLOW_METHODS.split(","),
    expose_headers=CORS_ALLOW_HEADERS.split(","),
)


# Home Resource
@api.route("/home")
class Home(Resource):
    """
    Home Resource

    Description:
        - This class is used to create home resource.

    """

    def get(self) -> dict[str, str | bool]:
        """
        Home Resource

        Description:
            - This function is used to create home route.

        Args:
            - `None`

        Returns:
            - `None`

        """

        return {"success": True, "data": f"Welcome to {PROJECT_TITLE}"}


# Register namespaces
api.add_namespace(ns_role)
api.add_namespace(ns_user)
api.add_namespace(ns_permission)
api.add_namespace(ns_role_permission)

add_permissions()
add_roles()
add_admin_permissions()
# Main function to run application
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
