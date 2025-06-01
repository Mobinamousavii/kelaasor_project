from rest_framework.permissions import BasePermission


def HasRole(role_name):
    class RolePermission(BasePermission):
        def has_permission(self, request, view):
            return request.user.is_authenticated and request.user.role and request.user.role.name == role_name
    return RolePermission
           


