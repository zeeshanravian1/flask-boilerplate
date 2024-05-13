"""
Role Namespace

Description:
    - This module contains role namespace.

"""

from flask_restx import Namespace

ns_role = Namespace(name="Role", description="Role operations", path="/role")
