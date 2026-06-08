from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Inicializa o roteador automático do Django REST Framework
router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet, basename='api-categoria')
router.register(r'formas-pagamento', views.FormaDePagamentoViewSet, basename='api-forma-pagamento')
router.register(r'despesas', views.DespesaViewSet, basename='api-despesa')
router.register(r'rendas', views.RendaViewSet, basename='api-renda')

urlpatterns = [
    # --- Rotas Originais do Front-end (Seu site HTML) ---
    path('', views.home, name='home'),
    path('historico/', views.listar_despesas, name='listar'),
    path('adicionar/', views.adicionar_despesa, name='adicionar'),
    path('editar/<int:id>/', views.editar_despesa, name='editar'),
    path('excluir/<int:id>/', views.excluir_despesa, name='excluir'),

    # --- Rotas da API RESTful (Geradas dinamicamente pelo Router) ---
    path('api/', include(router.urls)),
]