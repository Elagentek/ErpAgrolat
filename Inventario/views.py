from .models import Producto
from django.shortcuts import render, redirect
from django.contrib import messages



def inventario_view(request):
    editar_id = request.GET.get('edit_id')
    query = request.GET.get('buscar', '')
    
    productos = Producto.objects.filter(nombre__icontains=query) if query else Producto.objects.all()

    if request.method == 'POST':
        if 'agregar' in request.POST:
            Producto.objects.create(
                nombre=request.POST['nombre'],
                categoria=request.POST['categoria'],
                stock=request.POST['stock'],
                precio=request.POST['precio']
            )
            messages.success(request, "Producto agregado correctamente.")
            return redirect('inventario')

        if 'guardar' in request.POST:
            p = Producto.objects.get(id=request.POST['producto_id'])
            p.nombre = request.POST['nombre']
            p.categoria = request.POST['categoria']
            p.stock = request.POST['stock']
            p.precio = request.POST['precio']
            p.save()
            messages.success(request, "Producto actualizado.")
            return redirect('inventario')

        if 'eliminar' in request.POST:
            Producto.objects.get(id=request.POST['eliminar']).delete()
            messages.success(request, "Producto eliminado.")
            return redirect('inventario')

    return render(request, 'Inventario/Inventario.html', {
        'productos': productos,
        'editar_id': int(editar_id) if editar_id else None,
        'buscar': query
    })
