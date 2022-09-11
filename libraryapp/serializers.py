
from rest_framework import serializers
from .models import BookData

class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100)
    authors = serializers.CharField(max_length=100)
    publisher = serializers.CharField(max_length=100)
    class Meta:
        model = BookData
        fields = ('__all__')