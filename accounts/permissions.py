from rest_framework.permissions import BasePermission


class HasRole(BasePermission):

    def __init__(self, role_name):
        self.role_name = role_name

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role and
            request.user.role.name == self.role_name
        )

           

