from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestionar_ventas, name='gestionar_ventas'),  # Página principal del módulo
    path('eliminar/<int:venta_id>/', views.eliminar_venta, name='eliminar_venta'),
    path('boleta/<int:venta_id>/', views.generar_boleta, name='generar_boleta'),

]
