from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from django.urls import reverse
from django.contrib import messages

def lista_clientes(request):
    consulta = request.GET.get('buscar', '')
    if consulta:
        clientes = Cliente.objects.filter(nombre__icontains=consulta)
    else:
        clientes = Cliente.objects.all()

    total = clientes.count()

    return render(request, 'Clientes/gestion_clientes.html', {
        'clientes': clientes,
        'total': total,
        'consulta': consulta
    })

def crear_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        telefono = request.POST.get('telefono', '')

        if Cliente.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está registrado.')
        else:
            Cliente.objects.create(nombre=nombre, email=email, telefono=telefono)
            messages.success(request, 'Cliente creado correctamente.')

        return redirect('lista_clientes')
    return redirect('lista_clientes')

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.email = request.POST['email']
        cliente.telefono = request.POST.get('telefono', '')
        cliente.save()
        messages.success(request, 'Cliente actualizado correctamente.')
        return redirect('lista_clientes')

    return render(request, 'Clientes/editar_cliente.html', {'cliente': cliente})

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    messages.success(request, 'Cliente eliminado correctamente.')
    return redirect('lista_clientes')
