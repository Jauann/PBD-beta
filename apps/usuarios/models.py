from django.contrib.auth.models import AbstractUser


class UsuarioCustomizado(AbstractUser):
    def __str__(self):
        return self.username
