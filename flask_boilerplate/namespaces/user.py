"""
User Namespace

Description:
    - This module contains user namespace.

"""

from flask_restx import Namespace

ns_user = Namespace(name="User", description="User Operations", path="/user")
