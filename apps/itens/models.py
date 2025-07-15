# PBD beta/apps/itens/models.py

from django.db import models
from django.conf import settings

class Tipo(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, unique=True, null=True, blank=True)
    dono = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='empresas_dos_itens')

    def __str__(self):
        return self.nome

class Item(models.Model):
    # Opções para o campo status
    STATUS_CHOICES = (
        ('disponivel', 'Disponível'),
        ('alugado', 'Alugado'),
        ('manutencao', 'Em Manutenção'),
    )

    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    # Novo campo para a imagem
    imagem = models.ImageField(upload_to='itens_imagens/', blank=True, null=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True, blank=True)
    # Campo status com opções pré-definidas
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')
    # Novo campo para a quantidade
    quantidade = models.PositiveIntegerField(default=1)
    preco_diario = models.DecimalField(max_digits=10, decimal_places=2)
    proprietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='itens')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='itens')

    def __str__(self):
        return self.nome