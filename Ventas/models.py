from django.db import models
from Clientes.models import Cliente
from Inventario.models import Producto

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta #{self.id} - {self.cliente.nombre} - {self.fecha.strftime('%d/%m/%Y')}"

    @property
    def total(self):
        return sum(d.cantidad * d.precio_unitario for d in self.detalles.all())

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad} - Venta #{self.venta.id}"
