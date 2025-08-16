# blog/urls.py
from django.urls import path
from .views import CommentCreateView, CommentDeleteView, CommentUpdateView, PostCreateView, PostDeleteView, PostDetailView, PostListView, PostSearchView, PostUpdateView,register_view, login_view, logout_view, profile_view

urlpatterns = [
    # Authentication URLs
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),

    # Blog post URLs
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
        # Comment URLs (updated to match system check)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),

    path('search/', PostSearchView.as_view(), name='post-search'),
    path('tags/<slug:tag_slug>/', PostListView.as_view(), name='posts-by-tag'),
]
