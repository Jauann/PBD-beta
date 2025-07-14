from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioCustomizado


class FormularioSignUp(UserCreationForm):
    class Meta:
        model = UsuarioCustomizado
        fields = [
            "username",
            "password1",
            "password2",
        ]


class FormularioLogin(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
