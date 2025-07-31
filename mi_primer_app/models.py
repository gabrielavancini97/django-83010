from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    parentesco = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} ({self.edad} años) - {self.parentesco}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_semanas = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


#aqui avanzo con las clases para el trabajo proyecto, que va a terminar siendo una web para comercializar productos estructurales:

class Producto(models.Model):#productos a comercializar
    tipo = models.CharField(max_length=100)  # Ej: "Rectangular", "Redondo"
    medida = models.CharField(max_length=50)  # Ej: "40x60 mm", "50 mm"
    espesor = models.DecimalField(max_digits=5, decimal_places=2)  # mm
    largo = models.DecimalField(max_digits=6, decimal_places=2)  # metros
    precio_por_metro = models.DecimalField(max_digits=10, decimal_places=2)
    stock_metros = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tipo} {self.medida} x {self.espesor} mm"
    
class Cliente(models.Model): #los clientes que van a realizar los pedidos que pueden ser empresas o personas
    nombre = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=150, blank=True)
    cuit = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre}"
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    productos = models.ManyToManyField(Producto, through='DetallePedido') #este many to many me sugirio el chat para relacionar con detalles del pedido
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nombre} - {self.fecha}"
    
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_metros = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.cantidad_metros * self.precio_unitario
    
    #ahora deberia ejecutar los migrate--....