from typing import Dict

import jwt
from flask import g, request
from werkzeug.exceptions import Unauthorized
from ..services.user import UserService
from flask_boilerplate.core.config import PUBLIC_KEY


def decode_jwt_token(token: str) -> Dict:
    """
    Decode jwt token

    Args:
        token: Token to decode

    Returns:
        Decoded dictionary
    """
    try:
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
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None


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

    def wraps(f):
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
            else:
                return Unauthorized("Invalid Token")

            return f(*args, **kwargs)

        return wrapper_function

    # If @auth is used instead of @auth(PERMISSION), value will
    # contain the child function instead of being empty due to
    # how decorators work, we handle that
    if hasattr(value, "__call__"):
        f = value
        value = None
        return wraps(f)

    return wraps
