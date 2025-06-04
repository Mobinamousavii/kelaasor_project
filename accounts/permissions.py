from rest_framework.permissions import BasePermission


def HasRole(role_name):
    """
    Returns a custom permission class that grants access only to authenticated users
    with a specific role.

    This is a dynamic permission generator that allows you to enforce role-based access control
    without writing a separate permission class for each role (e.g., support, admin, teacher, etc.).

    """
    class RolePermission(BasePermission):
        def has_permission(self, request, view):
            return request.user.is_authenticated and request.user.role and request.user.role.name == role_name
    return RolePermission
           


