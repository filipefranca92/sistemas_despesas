from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# 1. Modelo: Forma de Pagamento
class FormaDePagamento(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nome

# 2. Modelo: Categoria
class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nome

# 3. Modelo: Despesa
class Despesa(models.Model):
    # max_digits=10 e decimal_places=2 permitem valores até 99.999.999,99
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    data = models.DateField(auto_now_add=True, db_index=True)
    
    # Relações com os modelos acima
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='despesas'
    )
    forma_pagamento = models.ForeignKey(
        FormaDePagamento, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='despesas'
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        nome_categoria = self.categoria.nome if self.categoria else "Sem Categoria"
        return f"{nome_categoria} - R$ {self.valor}"

# 4. Modelo: Renda (Adicionado para completar sua API conforme a Atividade 1)
class Renda(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=100)
    data = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Renda: R$ {self.valor}"