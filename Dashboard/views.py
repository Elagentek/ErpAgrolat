from django.shortcuts import render

def dashboard_view(request):
    context = {
        'mensaje': 'Bienvenido al Dashboard de Agrolat'
    }
    return render(request, 'Dashboard/Dashboard_Usuario.html', context)
