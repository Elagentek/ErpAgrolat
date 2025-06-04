from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Dashboard principal
@login_required
def dashboard_view(request):
    return render(request, 'Dashboard/dashboard.html')

def consultar_usuarios(request):
    usuarios = User.objects.all()

    editar_usuario = None
    if 'edit_id' in request.GET:
        editar_usuario = get_object_or_404(User, pk=request.GET.get('edit_id'))

    if request.method == 'POST':
        if 'save_user' in request.POST:
            usuario = get_object_or_404(User, pk=request.POST.get('id'))
            usuario.username = request.POST.get('username')
            usuario.email = request.POST.get('email')
            usuario.save()
            messages.success(request, 'Usuario actualizado correctamente.')
            return redirect('consultar_usuarios')

        elif 'delete_user' in request.POST:
            usuario = get_object_or_404(User, pk=request.POST.get('id'))
            usuario.delete()
            messages.success(request, 'Usuario eliminado correctamente.')
            return redirect('consultar_usuarios')

    return render(request, 'Dashboard/consultausuarios.html', {
        'usuarios': usuarios,
        'editar_usuario': editar_usuario
    })

def inventario_view(request):
    return render(request, 'Inventario/Inventario.html')
