from django.contrib.auth.models import User
from django.db import models

ROLES = (
    ('admin', 'Administrador'),
    ('vendedor', 'Vendedor'),
)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=10, choices=ROLES)

    def __str__(self):
        return f'{self.user.username} ({self.get_rol_display()})'
