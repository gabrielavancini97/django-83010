from django.contrib import admin
from .models import Familiar, Curso, Estudiante, Producto, Cliente, Pedido, DetallePedido

# Register your models here.
register_models = [Familiar, Curso, Estudiante, Producto, Cliente, Pedido, DetallePedido]

admin.site.register(register_models)