from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


from library.serializer import BookSerializer, AuthorSerializer, LocationSerializer
from .models import Book, Author


# Create your views here.

@api_view(['POST'])
def create_book(request):
    book_serializer = BookSerializer(data=request.data)

    if book_serializer.is_valid():
        book_serializer.save()
        return Response(book_serializer.data, status=status.HTTP_201_CREATED)

    return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_author(request):
    author_serializer = AuthorSerializer(data=request.data)

    if author_serializer.is_valid():
        author_serializer.save()

        return Response(author_serializer.data, status=status.HTTP_201_CREATED)

    return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_location(requests):
    location_serilizer = LocationSerializer(data=requests.data)

    if location_serilizer.is_valid():
        location_serilizer.save()
        return Response(location_serilizer.data, status=status.HTTP_201_CREATED)
    return Response(location_serilizer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_book(request):
    listBook = Book.objects.all()
    print(listBook)
    book_serializer = BookSerializer(listBook, many=True)
    return Response(data=book_serializer.data, status=status.HTTP_200_OK)