from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.urls import reverse_lazy

urlpatterns = [
    # Redirige la raíz del sitio a la vista de login
    path('', RedirectView.as_view(url=reverse_lazy('login'), permanent=False)),

    # Admin de Django
    path('admin/', admin.site.urls),

    # Módulo Login (asegúrate que la app se llame exactamente 'Login')
    path('login/', include('Login.urls')),

    # Módulo Dashboard
    path('dashboard/', include('Dashboard.urls')),
]
