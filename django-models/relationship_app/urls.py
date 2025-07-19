from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('admin-role/', views.admin_view, name='admin_view'),
    path('librarian-role/', views.librarian_view, name='librarian_view'),
    path('member-role/', views.member_view, name='member_view'),
=======
    # Your existing URLs for books and libraries here
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
>>>>>>> f4cc49a (authentication added)
]
