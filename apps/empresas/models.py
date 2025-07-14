from django.db import models
from django.conf import settings

class Empresa(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, unique=True) # Adicionado o campo CNPJ
    dono = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='empresas')

    def __str__(self):
        return self.nome