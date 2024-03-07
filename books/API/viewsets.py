from rest_framework import viewsets
from books import models
from books.API import serializer

class BooksViewSet(viewsets.ModelViewSet):
    queryset = models.Books.objects.all()
    serializer_class = serializer.BooksSerializers