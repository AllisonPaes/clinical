from django.db import models

class Sala(models.Model):
    numero = models.CharField(max_length=5, unique=True)
    descricao = models.TextField()

    def __str__(self):
        return self.numero


# Create your models here.
