from django.urls import path

from library import views

urlpatterns = [
    path('createbook/', views.create_book, name='createbook'),
    path('createAuthor/', views.create_author, name='createauthor'),
    path('createlocation/', views.create_location, name='createlocation'),
    path('getbooks/', views.get_book, name='getbooks')
]






# TODO: GET BOOK BY ID and return json response..
# TODO: GET AUTHOR BY ID and return json response..