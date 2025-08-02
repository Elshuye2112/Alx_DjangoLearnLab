from django.urls import path
from .view import BookList

urlpatterns=[
    path('books/',BookList.as_view(),name='book-list')
]