from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item
from .forms import ItemForm

class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'itens/item_list.html'
    context_object_name = 'itens'

    def get_queryset(self):
        # Filtra os itens para mostrar apenas os do usuário logado
        return Item.objects.filter(proprietario=self.request.user)

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'itens/item_form.html'
    success_url = reverse_lazy('itens:item-list')

    def form_valid(self, form):
        # Associa o item ao usuário logado
        form.instance.proprietario = self.request.user
        return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'itens/item_form.html'
    success_url = reverse_lazy('itens:item-list')

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = 'itens/item_confirm_delete.html'
    success_url = reverse_lazy('itens:item-list')