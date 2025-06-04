from django.urls import path
from .views import inventario_view

urlpatterns = [
    path('', inventario_view, name='inventario'),
]
