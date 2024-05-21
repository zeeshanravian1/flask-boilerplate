"""
This file contains the functionality to update the redis on deletion of any role and permission
"""

from flask_boilerplate.services.redis import redis
from flask_boilerplate.services.role import RoleService


def remove_permission_from_roles(permission: str):
    roles = RoleService().read_all()
    for role in roles:
        redis_permission = redis.get(role.role_name)
        if redis_permission:
            if permission in redis_permission:
                redis_permission.remove(permission)
                redis.set(role.role_name, redis_permission)
