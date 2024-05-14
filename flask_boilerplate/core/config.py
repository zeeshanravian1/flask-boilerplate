"""
Core Configuration Module

Description:
    - This module is responsible for core configuration and read values from
    environment file.

"""

import environs

# Creating env object
env = environs.Env()

# Reading environment file
env.read_env()

# Database
DATABASE: str = env.str("DATABASE")
DB_HOST: str = env.str("DB_HOST")
DB_PORT: int = env.int("DB_PORT")
DB_USER: str = env.str("DB_USER")
DB_PASSWORD: str = env.str("DB_PASSWORD")
DB_NAME: str = env.str("DB_NAME")
DB_SCHEMA: str = env.str("DB_SCHEMA")

DATABASE_URL: str = (
    f"{DATABASE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


# CORS
CORS_ALLOW_ORIGINS: str = env.str("CORS_ALLOW_ORIGINS")
CORS_ALLOW_METHODS: str = env.str("CORS_ALLOW_METHODS")
CORS_ALLOW_HEADERS: str = env.str("CORS_ALLOW_HEADERS")
CORS_ALLOW_CREDENTIALS: bool = env.bool("CORS_ALLOW_CREDENTIALS")


# Project
PROJECT_TITLE: str = "Flask BoilerPlate"
PROJECT_DESCRIPTION: str = "Flask BoilerPlate Documentation"

PROJECT_VERSION: str = "0.1.0"
API_PREFIX: str = "/api/v1"
DOCS_URL: str = "/docs"

SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
SWAGGER_UI_DOC_EXPANSION: str = "list"
