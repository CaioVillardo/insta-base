from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Post

def get_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    data = {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author': post.author.username,
        'created_at': post.created_at,
        'updated_at': post.updated_at,
    }
    return JsonResponse(data)

def create_post(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    author_id = request.POST.get('author_id')

    post = Post.objects.create(title=title, content=content, author_id=author_id)

    data = {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author': post.author.username,
        'created_at': post.created_at,
        'updated_at': post.updated_at,
    }
    return JsonResponse(data, status=201)

def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    post.title = request.POST.get('title')
    post.content = request.POST.get('content')

    post.save()

    data = {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author': post.author.username,
        'created_at': post.created_at,
        'updated_at': post.updated_at,
    }
    return JsonResponse(data)

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return JsonResponse({'message': 'Post deleted'})
