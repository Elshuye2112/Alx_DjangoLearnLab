from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrReadOnly(BasePermission):
    """
    Read for everyone; write only for the object's author.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # obj has .author in both Post and Comment
        return getattr(obj, 'author_id', None) == getattr(request.user, 'id', None)
