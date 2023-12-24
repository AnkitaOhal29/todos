# auth/permissions.py
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or user.role != 'Admin':
            raise PermissionDenied("Custom Permission Denied Message")
        return True
