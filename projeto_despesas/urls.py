from django.contrib import admin
from django.urls import path, include # <-- Adicionamos o 'include' aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    # Dizemos ao Django para enviar as URLs da raiz para o nosso app
    path('', include('despesas.urls')), 
]