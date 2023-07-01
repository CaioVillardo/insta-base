from django.urls import path, include
from .views import (
    UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    FollowerCreateView, FollowerDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView,
    password_reset, password_reset_confirm,
)

urlpatterns = [
    # User URLs
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),

    # Post URLs
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Follower URLs
    path('followers/create/', FollowerCreateView.as_view(), name='follower_create'),
    path('followers/<int:pk>/delete/', FollowerDeleteView.as_view(), name='follower_delete'),

    # Comment URLs
    path('comments/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),

    # Authentication URLs
    path('api/token/', authentication.obtain_token, name='token_obtain'),
    path('api/token/refresh/', authentication.refresh_token, name='token_refresh'),
    path('api/token/verify/', authentication.verify_token, name='token_verify'),

    # Password Recovery URLs
    path('password/reset/', password_reset, name='password_reset'),
    path('password/reset/confirm/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),

    # RBAC URLs
    path('roles/', include('rbac.urls')),
]
