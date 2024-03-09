from django.urls import path,include
from .views import *


urlpatterns = [
    path('books/', BooksList.as_view()),
    path('books/<int:pk>/', BooksDetail.as_view()),

]