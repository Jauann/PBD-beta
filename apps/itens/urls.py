from django.urls import path
from .views import ItemListView, ItemCreateView, ItemUpdateView, ItemDeleteView

app_name = 'itens'

urlpatterns = [
    path('', ItemListView.as_view(), name='item-list'),
    path('novo/', ItemCreateView.as_view(), name='item-create'),
    path('<int:pk>/editar/', ItemUpdateView.as_view(), name='item-update'),
    path('<int:pk>/excluir/', ItemDeleteView.as_view(), name='item-delete'),
]