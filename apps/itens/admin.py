from django.contrib import admin
from .models import Tipo, Empresa, Item

admin.site.register(Tipo)
admin.site.register(Empresa)
admin.site.register(Item) # Também registramos o Item para facilitar