from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """ Права для владельца объекта """

    def has_object_permission(self, request, view, obj):

        if request.user == obj.user:
            return True

        return False
