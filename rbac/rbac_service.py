from .models import UserRole

def check_permission(user, resource, action):
    try:
        role = UserRole.objects.get(user=user)
        if role.permissions.filter(resource=resource, action=action).exists():
            return True
    except UserRole.DoesNotExist:
        pass
    return False
