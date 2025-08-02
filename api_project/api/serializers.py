from rest_framework import serializers
from .models import Book

class BooKSerializer(serializers.ModelSerializer):
    class meta:
        model=Book
        fields='_all_'
