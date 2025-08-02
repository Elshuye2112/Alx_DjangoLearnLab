from rest_framework import generics
from .models import Book
from .serializers import BooKSerializer

class BookList(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=BooKSerializer