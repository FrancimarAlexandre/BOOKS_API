from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated  # Importe IsAuthenticated
from BOOKS import models
from BOOKS import serializers

class BooksList(generics.ListCreateAPIView):
    serializer_class = serializers.BooksSerializers
    queryset = models.Books.objects.all()
    permission_classes = [IsAuthenticated]  # Adicione a permissão aqui

class BooksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Books.objects.all()
    serializer_class = serializers.BooksSerializers
    permission_classes = [IsAuthenticated]  # Adicione a permissão aqui
