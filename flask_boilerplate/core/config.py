"""
Core Configuration Module

Description:
    - This module is responsible for core configuration and read values from
    environment file.

"""

import environs

# Creating env object
env = environs.Env()
env.read_env()

ENVIRONMENT: str = env.str("ENV")
# Database
DATABASE: str = env.str("DATABASE")
DB_HOST: str = env.str("DB_HOST")
DB_PORT: int = env.int("DB_PORT")
DB_USER: str = env.str("DB_USER")
DB_PASSWORD: str = env.str("DB_PASSWORD")
DB_NAME: str = env.str("DB_NAME")

DATABASE_URL: str = (
    f"{DATABASE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


# CORS
CORS_ALLOW_ORIGINS: str = env.str("CORS_ALLOW_ORIGINS")
CORS_ALLOW_METHODS: str = env.str("CORS_ALLOW_METHODS")
CORS_ALLOW_HEADERS: str = env.str("CORS_ALLOW_HEADERS")
CORS_ALLOW_CREDENTIALS: bool = env.bool("CORS_ALLOW_CREDENTIALS")


# JWT
PRIVATE_KEY: str = env.str("PRIVATE_KEY").replace("\\n", "\n")
PUBLIC_KEY: str = env.str("PUBLIC_KEY").replace("\\n", "\n")
ACCESS_TOKEN_EXPIRY_TIME: int = 60 * 24  # 1 day
REFRESH_TOKEN_EXPIRY_TIME: int = 60 * 24 * 7  # 1 week


# Project
PROJECT_TITLE: str = "Flask BoilerPlate"
PROJECT_DESCRIPTION: str = "Flask BoilerPlate Documentation"

PROJECT_VERSION: str = "0.1.0"
API_PREFIX: str = "/api/v1"
DOCS_URL: str = "/docs"

SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

SWAGGER_UI_DOC_EXPANSION: str = "list"
SWAGGER_SECURITY: str = "Authorization"
SWAGGER_AUTHORIZATIONS: dict[str, dict[str, str]] = {
    "Authorization": {
        "description": "Inputs: Bearer \\<jwtToken\\>",
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
    }
}

REDIS_PORT: int = env.str("REDIS_PORT")
REDIS_HOST: str = env.str("REDIS_HOST")
