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

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == "DELETE":
        book.delete()
        return Response({
            'delete': True
        })