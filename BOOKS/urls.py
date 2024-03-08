from django.urls import path,include
from . import viewset
from rest_framework import routers

# criando as rotas
router = routers.DefaultRouter()
router.register(r'books',viewset.BookViewset)
urlpatterns = [
    path('',include(router.urls)),
]
