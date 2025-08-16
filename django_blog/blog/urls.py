# blog/urls.py
from django.urls import path
from .views import CommentCreateView, CommentDeleteView, CommentUpdateView, PostByTagListView, PostCreateView, PostDeleteView, PostDetailView, PostListView, PostSearchView, PostUpdateView,register_view, login_view, logout_view, profile_view

urlpatterns = [
    # Authentication URLs
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),

    # Blog post URLs
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
        # Comment URLs (updated to match system check)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
    # Tag filtering URL
    path('posts/tag/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
    path('search/', PostSearchView.as_view(), name='post-search'),
    path('tags/<slug:tag_slug>/', PostListView.as_view(), name='posts-by-tag'),
]
