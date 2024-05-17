"""
Permission Namespace

Description:
    - This module contains permission namespace.

"""

from flask_restx import Namespace

ns_permission = Namespace(
    name="Permission", description="Permission operations", path="/permission"
)
