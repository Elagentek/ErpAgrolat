from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Clientes.models import Cliente
from Inventario.models import Producto
from .models import Venta, DetalleVenta

def gestionar_ventas(request):
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    ventas = Venta.objects.all().order_by('-fecha')

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        productos_ids = request.POST.getlist('producto[]')
        cantidades = request.POST.getlist('cantidad[]')

        if not cliente_id or not productos_ids:
            messages.error(request, "Debes seleccionar un cliente y al menos un producto.")
            return redirect('gestionar_ventas')

        cliente = get_object_or_404(Cliente, id=cliente_id)

        # Validación de stock antes de crear la venta
        for prod_id, cant in zip(productos_ids, cantidades):
            producto = get_object_or_404(Producto, id=prod_id)
            cantidad = int(cant)
            if producto.stock < cantidad:
                messages.error(request, f"No hay suficiente stock para {producto.nombre}.")
                return redirect('gestionar_ventas')

        venta = Venta.objects.create(cliente=cliente)

        for prod_id, cant in zip(productos_ids, cantidades):
            producto = Producto.objects.get(id=prod_id)
            cantidad = int(cant)

            producto.stock -= cantidad
            producto.save()

            DetalleVenta.objects.create(
                venta=venta,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=producto.precio
            )

        messages.success(request, "Venta registrada correctamente.")
        return redirect('gestionar_ventas')

    total_general = sum(v.total for v in ventas)

    return render(request, 'Ventas/dashboard_ventas.html', {
        'clientes': clientes,
        'productos': productos,
        'ventas': ventas,
        'total_general': total_general
    })

def eliminar_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    for detalle in venta.detalles.all():
        detalle.producto.stock += detalle.cantidad
        detalle.producto.save()
    venta.delete()
    messages.success(request, "Venta eliminada correctamente.")
    return redirect('gestionar_ventas')
