from django.urls import path
from . import views

urlpatterns = [
    # Your existing URLs for books and libraries here
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]
