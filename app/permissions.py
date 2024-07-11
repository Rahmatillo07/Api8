from rest_framework.permissions import BasePermission,SAFE_METHODS

class AdminRequiredPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        else:
            return request.method in SAFE_METHODS



    def has_object_permission(self, request, view, obj):

        if request.user.is_staff:
            return True
        else:
            return request.method in SAFE_METHODS

