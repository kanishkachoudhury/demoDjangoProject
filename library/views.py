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


#get all books
@api_view(['GET'])
def get_book(request):
    test = {'message': 'This is a GET response'}
    booklist = Book.objects.all()
    book_serializer = BookSerializer(data=booklist, many=True)
    

    if book_serializer.is_valid():
        print(book_serializer.data)
        return Response(book_serializer.data, status=status.HTTP_200_OK)
    
        #return Response(test,status=status.HTTP_200_OK)
        #json_data = JSONRenderer().render(book_serializer.data)
        #return Response(json_data, status=status.HTTP_200_OK)
        #return Response(test)