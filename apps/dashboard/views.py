from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url="/usuarios/login/")
def dashboard(request):
    context = {"user": request.user, "page_title": "Meu Dashboard"}
    return render(request, "dashboard/dash.html", context)
