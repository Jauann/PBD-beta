from django.db import models
from django.conf import settings

class Tipo(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    nome = models.CharField(max_length=200)
    dono = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='empresas')

    def __str__(self):
        return self.nome

class Item(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco_diario = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    proprietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='itens')
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='itens')

    def __str__(self):
        return self.nome