# blog/urls.py
from django.urls import path
from .views import CommentCreateView, CommentDeleteView, CommentUpdateView, PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, add_comment, delete_comment, edit_comment, register_view, login_view, logout_view, profile_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:post_id>/comments/new/', add_comment, name='add-comment'),
    path('comments/<int:comment_id>/edit/', edit_comment, name='edit-comment'),
    path('comments/<int:comment_id>/delete/', delete_comment, name='delete-comment'),
    path('posts/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='edit-comment'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
]
