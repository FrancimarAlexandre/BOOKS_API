from django.shortcuts import render
from rest_framework import generics
from BOOKS import models
from BOOKS import serializers
# Create your views here.

class BooksList(generics.ListCreateAPIView):
    serializer_class = serializers.BooksSerializers
    queryset = models.Books.objects.all()

      
class BooksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Books.objects.all()
    serializer_class = serializers.BooksSerializers

