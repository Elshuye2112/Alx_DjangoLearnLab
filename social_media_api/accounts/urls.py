from django.urls import path
from .views import FeedView, FollowUserView, ListFollowersView, ListFollowingView, RegisterView, LoginView, ProfileView, UnfollowUserView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow-user"),
    path("<int:user_id>/followers/", ListFollowersView.as_view(), name="list-followers"),
    path("<int:user_id>/following/", ListFollowingView.as_view(), name="list-following"),
    path('feed/', FeedView.as_view(), name='feed'),
]
