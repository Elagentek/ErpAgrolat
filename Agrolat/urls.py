
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login/')),  # <- redirige raíz a /login/
    path('admin/', admin.site.urls),
    path('login/', include('Login.urls')),  # O 'login.urls' si la carpeta es minúscula
]
