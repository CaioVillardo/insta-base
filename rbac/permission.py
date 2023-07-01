from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    """
    Permissão que permite apenas ao proprietário ou ao administrador acessar o objeto.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return obj.owner == request.user
