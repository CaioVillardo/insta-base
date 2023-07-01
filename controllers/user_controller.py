from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import User

def get_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
    }
    return JsonResponse(data)

def create_user(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.create(username=username, email=email, password=password)

    data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
    }
    return JsonResponse(data, status=201)

def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    user.username = request.POST.get('username')
    user.email = request.POST.get('email')
    user.password = request.POST.get('password')

    user.save()

    data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
    }
    return JsonResponse(data)

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return JsonResponse({'message': 'User deleted'})
