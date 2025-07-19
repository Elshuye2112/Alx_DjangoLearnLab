from django.urls import path
from .views import add_book, edit_book, delete_book, list_books

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('books/add/', add_book, name='add_book'),                # Protected by 'can_add_book'
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),    # Protected by 'can_change_book'
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),  # Protected by 'can_delete_book'
]
