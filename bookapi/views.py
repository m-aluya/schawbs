from django.shortcuts import render
from bookapi.models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from bookapi.serializer import BookSerializer


# Create your views here.
@api_view(['GET'])
def books(request):
    get_books = Book.objects.all()
    books = BookSerializer(get_books, many=True)
    return Response(books.data, status=200)

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else: 
        return Response(serializer.errors, status=400)
    


