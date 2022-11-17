from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from book_api.models import Book
from book_api.serializer import BookSerializer

# Create your views here.
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()  # Complex Data
    serialzier = BookSerializer(books, many=True)
    return Response(serialzier.data)
    # books_python = list(books.values())  # Python DS
    # return JsonResponse({
    #     'books': books_python
    # })
