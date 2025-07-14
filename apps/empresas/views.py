from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Empresa
from .forms import EmpresaForm

class EmpresaListView(LoginRequiredMixin, ListView):
    model = Empresa
    template_name = 'empresas/empresa_list.html'
    context_object_name = 'empresas'

    def get_queryset(self):
        return Empresa.objects.filter(dono=self.request.user)

class EmpresaCreateView(LoginRequiredMixin, CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresas/empresa_form.html'
    success_url = reverse_lazy('empresas:empresa-list')

    def form_valid(self, form):
        form.instance.dono = self.request.user
        return super().form_valid(form)

class EmpresaUpdateView(LoginRequiredMixin, UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresas/empresa_form.html'
    success_url = reverse_lazy('empresas:empresa-list')

class EmpresaDeleteView(LoginRequiredMixin, DeleteView):
    model = Empresa
    template_name = 'empresas/empresa_confirm_delete.html'
    success_url = reverse_lazy('empresas:empresa-list')