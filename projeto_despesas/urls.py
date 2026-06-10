from django.contrib import admin
from django.urls import path, include
from despesas import views # Importamos as views para mapear o registo

urlpatterns = [
    path('admin/', admin.site.urls),
    # Dizemos ao Django para enviar as URLs da raiz para o nosso app
    path('', include('despesas.urls')), 
    
    # ATIVA ROTAS NATIVAS (login, logout) E A ROTA DE REGISTO
    path('contas/registrar/', views.registrar, name='registrar'),
    path('contas/', include('django.contrib.auth.urls')), 
]