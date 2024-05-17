"""
Role Permission Namespace

Description:
    - This module contains role permission namespace.

"""

from flask_restx import Namespace

ns_role_permission = Namespace(
    name="Role Permission",
    description="Role Permission operations",
    path="/role-permission",
)
