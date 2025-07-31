from django import forms


class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Curso')
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción')
    duracion_semanas = forms.IntegerField(label='Duración (semanas)')
    fecha_inicio = forms.DateField(
        widget=forms.SelectDateWidget, label='Fecha de Inicio')
    fecha_fin = forms.DateField(
        widget=forms.SelectDateWidget, label='Fecha de Fin')
    activo = forms.BooleanField(
        required=False, initial=True, label='Activo')  # Campo opcional


class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    apellido = forms.CharField(max_length=100, label='Apellido')
    email = forms.EmailField(label='Email')
    edad = forms.IntegerField(label='Edad')

#detallo a continuacion los forms para el proyecto:


class ProductoForm(forms.Form):
    tipo = forms.CharField(max_length=100, label='Tipo de Caño')  # Ej: "Redondo", "Rectangular"
    medida = forms.CharField(max_length=50, label='Medida')        # Ej: "50x50 mm"
    espesor = forms.DecimalField(max_digits=5, decimal_places=2, label='Espesor (mm)')
    largo = forms.DecimalField(max_digits=6, decimal_places=2, label='Largo (m)')
    precio_por_metro = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio por metro ($)')
    stock_metros = forms.DecimalField(max_digits=10, decimal_places=2, label='Stock disponible (metros)')


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre o Empresa')
    razon_social = forms.CharField(max_length=150, required=False, label='Razón Social')
    cuit = forms.CharField(max_length=20, required=False, label='CUIT')
    email = forms.EmailField(label='Email')
    telefono = forms.CharField(max_length=20, label='Teléfono')
    direccion = forms.CharField(widget=forms.Textarea, label='Dirección')

class PedidoForm(forms.Form):
    cliente_id = forms.IntegerField(label='ID del Cliente')


#esto podria ser para agregar productos al pedido
class DetallePedidoForm(forms.Form):
    producto_id = forms.IntegerField(label='ID del Producto')
    cantidad_metros = forms.DecimalField(max_digits=10, decimal_places=2, label='Cantidad (metros)')
    precio_unitario = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio unitario ($)')