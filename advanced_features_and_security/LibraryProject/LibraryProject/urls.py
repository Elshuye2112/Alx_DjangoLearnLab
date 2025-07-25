from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import path
from bookshelf import views as bookshelf_views
from django.views.generic import RedirectView

urlpatterns = [
    path('', lambda request: redirect('admin/')),
    path('admin/', admin.site.urls),
    path('relationship_app/', include('relationship_app.urls')),  # This is key
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Use bookshelf_views here:
    path('', bookshelf_views.book_list, name='book_list'),
    path('create/', bookshelf_views.book_create, name='book_create'),
    path('edit/<int:pk>/', bookshelf_views.book_edit, name='book_edit'),
    path('delete/<int:pk>/', bookshelf_views.book_delete, name='book_delete'),

    path('', RedirectView.as_view(url='/relationship_app/books/', permanent=False)),
]
