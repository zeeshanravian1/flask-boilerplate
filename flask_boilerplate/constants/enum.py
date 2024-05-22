from enum import Enum as PyEnum


class Enum(str, PyEnum):
    @classmethod
    def exists(cls, item):
        return item in [x.value for x in cls]

    @classmethod
    def list(cls):
        return [x.value for x in cls]


class Roles(Enum):
    ADMIN = "admin"
    CLIENT = "client"


class UserPermissions(Enum):
    GET_ALL_USERS = "Get All Users"
    GET_USER = "Get User"
    UPDATE_USER = "Update User"
    DELETE_USER = "Delete User"


class RolePermissions(Enum):
    Create_Role = "Create Role"
    GET_ALL_ROLE = "Get All Role"
    GET_ROLE = "Get Role"
    UPDATE_ROLE = "Update Role"
    DELETE_ROLE = "Delete Role"


class PermissionPermissions(Enum):
    CREATE_PERMISSION = "Create Permission"
    GET_ALL_PERMISSION = "Get All Permissions"
    GET_PERMISSION = "Get Permission"
    UPDATE_PERMISSION = "Update Permission"
    DELETE_PERMISSION = "Delete Permission"
