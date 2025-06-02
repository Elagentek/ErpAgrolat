from django.urls import path
from .views import registro_usuario

app_name = 'registro'

urlpatterns = [
    path('', registro_usuario, name='registro'),
]
