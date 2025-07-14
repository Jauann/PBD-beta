# apps/dashboard/urls.py

from django.urls import path
from . import views # Importa as views do app

app_name = 'dashboard' # Define um namespace para as URLs

urlpatterns = [
    path('', views.dashboard, name='dashboard-home'), # A rota '' corresponde a /dashboard/
]