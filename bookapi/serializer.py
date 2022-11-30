from rest_framework import serializers
from bookapi.models import Book
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    pages = serializers.IntegerField()
    publish_date = serializers.DateField()
    quantity = serializers.IntegerField()
    
    def create(self,data):
        return Book.objects.create(**data)
        
     

