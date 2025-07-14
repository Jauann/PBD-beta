from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.itens.models import Item # Importe o modelo Item

@login_required(login_url="/usuarios/login/")
def dashboard(request):
    # Busca os itens, o total e outras estatísticas
    itens_usuario = Item.objects.filter(proprietario=request.user)
    total_itens = itens_usuario.count()

    context = {
        "user": request.user,
        "page_title": "Meu Dashboard",
        "itens": itens_usuario,
        "total_itens": total_itens,
        # Você pode adicionar mais estatísticas aqui (aluguéis ativos, faturamento, etc.)
    }
    return render(request, "dashboard.html", context)