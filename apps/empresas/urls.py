from django.urls import path
from .views import EmpresaListView, EmpresaCreateView, EmpresaUpdateView, EmpresaDeleteView

app_name = 'empresas'

urlpatterns = [
    path('', EmpresaListView.as_view(), name='empresa-list'),
    path('nova/', EmpresaCreateView.as_view(), name='empresa-create'),
    path('<int:pk>/editar/', EmpresaUpdateView.as_view(), name='empresa-update'),
    path('<int:pk>/excluir/', EmpresaDeleteView.as_view(), name='empresa-delete'),
]