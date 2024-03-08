from rest_framework import viewsets
from . import serializers
from . import models

class BookViewset(viewsets.ModelViewSet):
    queryset = models.Books.objects.all()
    serializer_class = serializers.BooksSerializers
