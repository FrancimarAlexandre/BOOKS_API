from django.db import models

# Create your models here.

class Books(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    autor = models.CharField(max_length = 255)
    genero = models.CharField(max_length = 255)
    create_at = models.DateField(auto_now_add = True)
