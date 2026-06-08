from django.shortcuts import render, redirect, get_object_or_404
from .models import Despesa, Categoria, FormaDePagamento, Renda
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core.paginator import Paginator
from django.db import transaction
from datetime import datetime

# API REST Imports
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CategoriaSerializer, FormaDePagamentoSerializer, DespesaSerializer, RendaSerializer

# Cache Imports
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

# =====================================================================
# VIEWS DO FRONTEND (Site HTML)
# =====================================================================

def home(request):
    return render(request, 'despesas/home.html')

def listar_despesas(request):
    mes_atual = request.GET.get('mes', datetime.now().month)
    ano_atual = request.GET.get('ano', datetime.now().year)
    usuario_atual = request.user if request.user.is_authenticated else User.objects.first()

    query_base = Despesa.objects.filter(
        usuario=usuario_atual,
        data__month=mes_atual,
        data__year=ano_atual
    ).order_by('-data')
    
    total_mes = query_base.aggregate(Sum('valor'))['valor__sum'] or 0
    paginator = Paginator(query_base, 5)
    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'despesas': page_obj,
        'total_mes': total_mes,
        'mes_selecionado': int(mes_atual),
        'ano_selecionado': int(ano_atual)
    }
    return render(request, 'despesas/listar.html', context)

def adicionar_despesa(request):
    if request.method == 'POST':
        with transaction.atomic(): # Garantia de Rollback
            Despesa.objects.create(
                valor=request.POST.get('valor'),
                descricao=request.POST.get('descricao'),
                categoria_id=request.POST.get('categoria'),
                forma_pagamento_id=request.POST.get('forma_pagamento'),
                usuario=request.user
            )
        return redirect('listar')
    
    context = {
        'categorias': Categoria.objects.all(),
        'formas_pagamento': FormaDePagamento.objects.all()
    }
    return render(request, 'despesas/adicionar.html', context)

@transaction.atomic # Garantia de Rollback
def editar_despesa(request, id):
    despesa = get_object_or_404(Despesa, id=id)
    if request.method == 'POST':
        despesa.valor = request.POST.get('valor')
        despesa.descricao = request.POST.get('descricao')
        despesa.categoria_id = request.POST.get('categoria')
        despesa.forma_pagamento_id = request.POST.get('forma_pagamento')
        despesa.save()
        return redirect('listar')

    context = {
        'despesa': despesa,
        'categorias': Categoria.objects.all(),
        'formas_pagamento': FormaDePagamento.objects.all()
    }
    return render(request, 'despesas/editar.html', context)

@transaction.atomic # Garantia de Rollback
def excluir_despesa(request, id):
    despesa = get_object_or_404(Despesa, id=id)
    despesa.delete()
    return redirect('listar')

# =====================================================================
# API VIEWSETS (REST)
# =====================================================================

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

class FormaDePagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaDePagamento.objects.all()
    serializer_class = FormaDePagamentoSerializer
    permission_classes = [IsAuthenticated]

class DespesaViewSet(viewsets.ModelViewSet):
    serializer_class = DespesaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Despesa.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    @method_decorator(cache_page(60 * 5))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class RendaViewSet(viewsets.ModelViewSet):
    serializer_class = RendaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Renda.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)