from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Follower, User

def follow_user(request, user_id):
    follower_id = request.POST.get('follower_id')

    follower = get_object_or_404(User, id=follower_id)
    following = get_object_or_404(User, id=user_id)

    if Follower.objects.filter(follower=follower, following=following).exists():
        return JsonResponse({'message': 'Você já está seguindo esse usuário'}, status=400)

    follower_relationship = Follower.objects.create(follower=follower, following=following)

    data = {
        'id': follower_relationship.id,
        'follower': follower_relationship.follower.id,
        'following': follower_relationship.following.id,
        'created_at': follower_relationship.created_at,
    }
    return JsonResponse(data, status=201)

def unfollow_user(request, user_id):
    follower_id = request.POST.get('follower_id')

    follower = get_object_or_404(User, id=follower_id)
    following = get_object_or_404(User, id=user_id)

    if not Follower.objects.filter(follower=follower, following=following).exists():
        return JsonResponse({'message': 'Você não está seguindo esse usuário'}, status=400)

    Follower.objects.filter(follower=follower, following=following).delete()

    return JsonResponse({'message': 'Você deixou de seguir o usuário'})

def get_followers(request, user_id):
    following = get_object_or_404(User, id=user_id)
    followers = Follower.objects.filter(following=following)

    data = []
    for follower in followers:
        follower_data = {
            'id': follower.id,
            'follower': follower.follower.id,
            'following': follower.following.id,
            'created_at': follower.created_at,
        }
        data.append(follower_data)

    return JsonResponse(data, safe=False)
