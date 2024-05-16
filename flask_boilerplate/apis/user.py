"""
User APIs

Description:
    - This module is used to handle all user routes.

"""

import jwt
from datetime import datetime, timedelta
from http import HTTPStatus

from flask import request
from flask_restx import Resource

from flask_boilerplate.constants.user import USER, USER_DELETE_SUCCESS
from flask_boilerplate.namespaces.user import ns_user
from flask_boilerplate.responses.user import UserResponse
from flask_boilerplate.schemas.user import (
    user_create_schema,
    user_read_all_schema,
    user_read_schema,
    user_update_schema,
    user_login_schema,
    user_login_response,
)
from flask_boilerplate.services.user import UserService
from flask_boilerplate.core.config import PRIVATE_KEY
from flask_boilerplate.decorator.authorization import auth
from flask_boilerplate.constants.base import TOKEN_EXPIRY_TIME


# Resource to handle listing and adding users
@ns_user.route("/")
class UserListResource(Resource):
    """
    User List Resource

    Description:
        - This class is used to handle listing and adding users.

    """

    @ns_user.expect(user_create_schema, validate=True)
    @ns_user.marshal_with(fields=user_read_schema, code=HTTPStatus.CREATED)
    def post(self):
        """
        Add User

        Description:
            - This function is used to add a new user.

        Args:
        User details to be created with following fields:
            - `first_name (str)`: First name of user. **(Required)**
            - `last_name (str)`: Last name of user. **(Required)**
            - `contact (str)`: Contact of user. **(Optional)**
            - `username (str)`: Username of user. **(Required)**
            - `email (str)`: Email of user. **(Required)**
            - `password (str)`: Password of user. **(Required)**
            - `address (str)`: Address of user. **(Optional)**
            - `city (str)`: City of user. **(Optional)**
            - `state (str)`: State of user. **(Optional)**
            - `country (str)`: Country of user. **(Optional)**
            - `postal_code (str)`: Postal code of user. **(Optional)**

        Returns:
        User details along with following information:
            - `id (int)`: ID of user.
            - `first_name (str)`: First name of user.
            - `last_name (str)`: Last name of user.
            - `contact (str)`: Contact of user.
            - `username (str)`: Username of user.
            - `email (str)`: Email of user.
            - `address (str)`: Address of user.
            - `city (str)`: City of user.
            - `state (str)`: State of user.
            - `country (str)`: Country of user.
            - `postal_code (str)`: Postal code of user.
            - `created_at (str)`: Datetime of user creation.
            - `updated_at (str)`: Datetime of user updation.

        """

        user = UserService().create(entity=request.get_json())

        return UserResponse.create_response(data=user)

    @auth()
    @ns_user.marshal_with(fields=user_read_all_schema, code=HTTPStatus.OK)
    def get(self):
        """
        Get all Users

        Description:
            - This function is used to get all users.

        Args:
            - `None`

        Returns:
        Get all users with following information:
            - `id (int)`: ID of user.
            - `first_name (str)`: First name of user.
            - `last_name (str)`: Last name of user.
            - `contact (str)`: Contact of user.
            - `username (str)`: Username of user.
            - `email (str)`: Email of user.
            - `address (str)`: Address of user.
            - `city (str)`: City of user.
            - `state (str)`: State of user.
            - `country (str)`: Country of user.
            - `postal_code (str)`: Postal code of user.
            - `created_at (str)`: Datetime of user creation.
            - `updated_at (str)`: Datetime of user updation.

        """

        # Get all users
        users = UserService().read_all()

        return UserResponse.read_all_response(data=users)


# Resource to handle get, update, delete single user
@ns_user.route("/<int:user_id>")
class UserResource(Resource):
    """
    User Resource

    Description:
        - This class is used to handle get, update, delete single user.

    """

    @ns_user.marshal_with(fields=user_read_schema, code=HTTPStatus.OK)
    def get(self, user_id):
        """
        Get User

        Description:
            - This function is used to get a single user by providing user ID.

        Args:
            - `user_id (int)`: ID of user. **(Required)**

        Returns:
        Single User details along with following information:
            - `id (int)`: ID of user.
            - `first_name (str)`: First name of user.
            - `last_name (str)`: Last name of user.
            - `contact (str)`: Contact of user.
            - `username (str)`: Username of user.
            - `email (str)`: Email of user.
            - `address (str)`: Address of user.
            - `city (str)`: City of user.
            - `state (str)`: State of user.
            - `country (str)`: Country of user.
            - `postal_code (str)`: Postal code of user.
            - `created_at (str)`: Datetime of user creation.
            - `updated_at (str)`: Datetime of user updation.

        """

        user = UserService().read_by_id(entity_id=user_id)

        if not user:
            return UserResponse.not_found_response(data=USER)

        return UserResponse.read_response(data=user)

    @ns_user.expect(user_update_schema, validate=True)
    @ns_user.marshal_with(fields=user_read_schema, code=HTTPStatus.ACCEPTED)
    def put(self, user_id):
        """
        Update User

        Description:
            - This function is used to update a single user by providing user
            ID.

        Args:
            - `user_id (int)`: ID of user. **(Required)**
            User details to be updated with following fields:
            - `first_name (str)`: First name of user. **(Required)**
            - `last_name (str)`: Last name of user. **(Required)**
            - `contact (str)`: Contact of user. **(Optional)**
            - `username (str)`: Username of user. **(Required)**
            - `email (str)`: Email of user. **(Required)**
            - `address (str)`: Address of user. **(Optional)**
            - `city (str)`: City of user. **(Optional)**
            - `state (str)`: State of user. **(Optional)**
            - `country (str)`: Country of user. **(Optional)**
            - `postal_code (str)`: Postal code of user. **(Optional)**

        Returns:
        Updated User details along with following information:
            - `id (int)`: ID of user.
            - `first_name (str)`: First name of user.
            - `last_name (str)`: Last name of user.
            - `contact (str)`: Contact of user.
            - `username (str)`: Username of user.
            - `email (str)`: Email of user.
            - `address (str)`: Address of user.
            - `city (str)`: City of user.
            - `state (str)`: State of user.
            - `country (str)`: Country of user.
            - `postal_code (str)`: Postal code of user.
            - `created_at (str)`: Datetime of user creation.
            - `updated_at (str)`: Datetime of user updation.

        """

        user = UserService().update(
            entity_id=user_id, entity=request.get_json()
        )

        if not user:
            return UserResponse.not_found_response(data=USER)

        return UserResponse.update_response(data=user)

    @ns_user.response(
        code=HTTPStatus.NO_CONTENT, description=USER_DELETE_SUCCESS
    )
    def delete(self, user_id):
        """
        Delete User

        Description:
            - This function is used to delete a user.

        Args:
            - `user_id (int)`: ID of user. **(Required)**

        Returns:
            - `None`

        """

        user = UserService().delete(entity_id=user_id)

        if not user:
            return UserResponse.not_found_response(data=USER)

        return UserResponse.delete_response()


@ns_user.route("/login")
class UserLogin(Resource):
    """
    User Login

    Description:
        - This class is used to handle user login

    """

    @ns_user.expect(user_login_schema, validate=True)
    @ns_user.marshal_with(fields=user_login_response, code=HTTPStatus.OK)
    def post(self):
        """
        Login User

        Description:
            - This function is used to login a user.

        Args:
            - `email (str)`: Email of user. **(Required)**
            - `password (str)`: Password of user. **(Required)**

        Returns:
            - `token (str)`: Access token.

        """
        user_email = ns_user.payload["email"]
        user_password = ns_user.payload["password"]

        user_services = UserService()
        user = user_services.get_by_validate_user(user_email, user_password)
        if user:
            token = jwt.encode(
                {
                    "sub": user.id,
                    "exp": datetime.utcnow()
                    + timedelta(seconds=TOKEN_EXPIRY_TIME),
                    "role": user.role_id,
                },
                PRIVATE_KEY,
                algorithm="RS256",
            )
            user.token = token
            return UserResponse.success(data=user)
        else:
            return UserResponse.failure("User not found")
