from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from .forms import FormularioSignUp, FormularioLogin


class SignupView(View):
    template_name = "usuarios/signup.html"
    form_class = FormularioSignUp

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home:home")
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect("usuarios:login")
        return render(request, self.template_name, {"form": form})


class LoginView(View):
    template_name = "usuarios/login.html"
    form_class = FormularioLogin

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home:home")
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login realizado com sucesso!")
                return redirect("home:home")
        messages.error(request, "Usuário ou senha incorretos")
        return render(request, self.template_name, {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "Você foi desconectado com sucesso.")
    return redirect("home:home")
