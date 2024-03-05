from rest_framework import viewsets
from books import models
from books.API import serializers

class BooksViewSet(viewsets.ModelViewSet):
    queryset = models.Books.objects.all()
    serializer_class = serializers.BooksSerializers