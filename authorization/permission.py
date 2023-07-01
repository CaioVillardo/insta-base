from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

def create_custom_permission(codename, name, content_type):
    content_type = ContentType.objects.get(app_label='instagram', model=content_type)
    permission = Permission.objects.create(
        codename=codename,
        name=name,
        content_type=content_type
    )
    return permission
