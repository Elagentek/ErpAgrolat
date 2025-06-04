from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import dashboard_view, consultar_usuarios
from django.urls import include

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('usuarios/', consultar_usuarios, name='consultar_usuarios'),
    path('inventario/', include('Inventario.urls')),
]
