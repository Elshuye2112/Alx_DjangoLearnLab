from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('', lambda request: redirect('admin/')),
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),  # This is key
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('', views.book_list, name='book_list'),
    path('create/', views.book_create, name='book_create'),
    path('edit/<int:pk>/', views.book_edit, name='book_edit'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
]
