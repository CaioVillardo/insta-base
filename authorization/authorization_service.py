def has_permission(user, resource_id, resource_type):
    user_permissions = user.get_all_permissions()

    if resource_type == "post":
        if user.is_superuser or user.has_perm("posts.view_post"):
            return True
        else:
            return False
    elif resource_type == "comment":
        if user.is_superuser or (user.has_perm("comments.view_comment") and user.has_perm("comments.view_comment", resource_id)):
            return True
        else:
            return False

    return False
