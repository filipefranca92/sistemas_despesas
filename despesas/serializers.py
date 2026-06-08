from rest_framework import serializers
from .models import Categoria, FormaDePagamento, Despesa, Renda

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class FormaDePagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaDePagamento
        fields = '__all__'

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'

class RendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renda
        fields = '__all__'