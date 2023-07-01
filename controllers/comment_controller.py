from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Comment, Post, User

def create_comment(request, post_id):
    user_id = request.POST.get('user_id')
    content = request.POST.get('content')

    user = get_object_or_404(User, id=user_id)
    post = get_object_or_404(Post, id=post_id)

    comment = Comment.objects.create(user=user, post=post, content=content)

    data = {
        'id': comment.id,
        'user': comment.user.id,
        'post': comment.post.id,
        'content': comment.content,
        'created_at': comment.created_at,
    }
    return JsonResponse(data, status=201)

def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    comment.content = request.POST.get('content')

    comment.save()

    data = {
        'id': comment.id,
        'user': comment.user.id,
        'post': comment.post.id,
        'content': comment.content,
        'created_at': comment.created_at,
    }
    return JsonResponse(data)

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return JsonResponse({'message': 'Comment deleted'})
