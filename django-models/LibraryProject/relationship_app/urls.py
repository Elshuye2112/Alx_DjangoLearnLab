from django.urls import path
from .views import list_books, add_book, edit_book, delete_book, LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('books/add/',add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),

    path('add_book/', add_book),       # for test script
    path('edit_book/<int:pk>/', edit_book),  # for test script

    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='views.register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
