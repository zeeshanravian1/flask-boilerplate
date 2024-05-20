from typing import Dict

import jwt
from flask import g, request
from werkzeug.exceptions import Unauthorized
from ..services.user import UserService
from flask_boilerplate.core.config import PUBLIC_KEY
from services.redis import redis
from functools import wraps as functools_wraps


def decode_jwt_token(token: str) -> Dict:
    """
    Decode jwt token

    Args:
        token: Token to decode

    Returns:
        Decoded dictionary
    """

    public_key = PUBLIC_KEY
    if public_key:
        decoded = jwt.decode(
            token,
            public_key,
            algorithms=["RS256"],
            options={
                "verify_aud": False,
            },
        )
        return decoded


def auth(*value):
    """
    Authorize user by decoding token

    Args:
        f: Function

    Raises:
        Unauthorized: Authorization Missing.
        Unauthorized: Invalid Token.
        Unauthorized: Unauthorized user.

    Returns:
        Decorated function
    """

    def decorator(f):
        @functools_wraps(f)
        def wrapper_function(*args, **kwargs):
            g.user = None
            g.permission = value
            authorization = request.headers.get("Authorization")
            if not authorization:
                raise Unauthorized("Authorization Missing.")

            token = authorization.split("Bearer ")
            if token and len(token) == 2:
                token = token[1]
            else:
                raise Unauthorized("Invalid Token")

            decoded = decode_jwt_token(token)
            if decoded and "sub" in decoded.keys():
                g.user = UserService().read_by_id(decoded["sub"])
                permissions = redis.get(g.user.role.role_name)
                if permissions:
                    if g.permission[0] in permissions:
                        return f(*args, **kwargs)
            else:
                raise Unauthorized("Invalid Token")

            raise Unauthorized("Invalid Token")

        return wrapper_function

    # Handle both cases where decorator might be used with or without arguments
    if value and hasattr(value[0], "__call__"):
        f = value[0]
        value = ()
        return decorator(f)

    return decorator
