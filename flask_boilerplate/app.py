# -*- coding: utf-8 -*-
"""
Application Factory Module

Description:
    - This module defines the Flask application factory and the basic
    configuration of the application.
    - The application factory is a function that returns a Flask application
    instance.

"""

from flask import Flask
from flask_cors import CORS

from .core.config import (
    CORS_ALLOW_CREDENTIALS,
    CORS_ALLOW_HEADERS,
    CORS_ALLOW_METHODS,
    CORS_ALLOW_ORIGINS,
    DATABASE_URL,
)
from .database.base import db


def create_app() -> Flask:
    """
    Create a Flask application instance with the SQLAlchemy database instance
    and CORS enabled.

    Description:
        - Create a Flask application instance.
        - Configure the application with the SQLAlchemy database instance.
        - Enable CORS for the application.

    Args:
        - `None`

    Returns:
        - `app`: Flask application instance

    """
    app = Flask(__name__)

    # Configure the application with the database URL
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

    # Disable the SQLAlchemy track modifications
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize the app with the SQLAlchemy database
    db.init_app(app)

    # Enable CORS
    CORS(
        app=app,
        supports_credentials=CORS_ALLOW_CREDENTIALS,
        origins=CORS_ALLOW_ORIGINS.split(","),
        methods=CORS_ALLOW_METHODS.split(","),
        headers=CORS_ALLOW_HEADERS.split(","),
    )

    return app
