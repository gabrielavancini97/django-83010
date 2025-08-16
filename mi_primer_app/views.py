from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Familiar, Curso, Estudiante, Producto, Cliente, Pedido, DetallePedido, Auto
from .forms import CursoForm, EstudianteForm, ProductoForm, ClienteForm, PedidoForm, AutoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def home(request):
    return render(request, 'mi_primer_app/home.html')#ruta a donde esta el archivo en templates

def hola_mundo(request):
    print("¡Hola, mundo!")
    return HttpResponse("¡Hola, mundo!")

def crear_familiar(request, nombre):
    if nombre is not None:
        Familiar.objects.create(
            nombre=nombre, edad=30, fecha_nacimiento="1991-01-01", parentesco="Hermano")
    return render(request, 'mi_primer_app/crear-familiar.html', {"familiar": nombre})

def listar_familiares(request):
    familiares = Familiar.objects.all()
    return render(request, 'mi_primer_app/listar-familiares.html', {"familiares": familiares})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            curso = Curso(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                duracion_semanas=form.cleaned_data['duracion_semanas'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                fecha_fin=form.cleaned_data['fecha_fin'],
                activo=form.cleaned_data['activo']
            )
            curso.save()
            return redirect('listar-cursos')

    form = CursoForm()
    return render(request, 'mi_primer_app/crear-curso.html', {"form": form})

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mi_primer_app/listar-cursos.html', {"cursos": cursos})

def buscar_cursos(request): #Funcion para buscar curso
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '') #tiene que coincidir con el NOMBRE de la FORMS.PY y LISTAR-CURSOS.html
        cursos = Curso.objects.filter(nombre__icontains=nombre) #filter por nombre sea igual al nombre que tenemos guardado en cursos
        return render(request, 'mi_primer_app/listar-cursos.html', {"cursos": cursos, "nombre": nombre})
    
def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = Estudiante(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                edad=form.cleaned_data['edad'],
            )
            estudiante.save()
            return redirect('listar-estudiantes')

    form = EstudianteForm()
    return render(request, 'mi_primer_app/crear-estudiante.html', {"form": form})  

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'mi_primer_app/listar-estudiantes.html', {"estudiantes": estudiantes})  


#PROYECTO 
#Para crear producto:

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            Producto.objects.create(**form.cleaned_data)
            return redirect('listar-productos')
    else:
        form = ProductoForm()
    return render(request, 'mi_primer_app/crear_producto.html', {'form': form})

#Para listar productos:

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'mi_primer_app/listar_productos.html', {'productos': productos})


#para buscar productos
def buscar_productos(request):
    if request.method == 'GET':
        busqueda = request.GET.get('busqueda', '')
        productos = Producto.objects.filter(
            tipo__icontains=busqueda
        ) | Producto.objects.filter(
            medida__icontains=busqueda
        )

        return render(request, 'mi_primer_app/listar_productos.html', {
            'productos': productos,
            'busqueda': busqueda
        })

#para crear clientes:

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            Cliente.objects.create(**form.cleaned_data)
            return redirect('listar-clientes')
    else:
        form = ClienteForm()
    return render(request, 'mi_primer_app/crear_cliente.html', {'form': form})

#para listar los clientes

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'mi_primer_app/listar_clientes.html', {'clientes': clientes})

#para listar los pedidos

def listar_pedidos(request):
    pedidos = Pedido.objects.all().select_related('cliente')
    return render(request, 'mi_primer_app/listar_pedidos.html', {'pedidos': pedidos})

#para la creacion del pedido... me costo muchisimo.. lo hice con ayuda..

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            cliente_id = form.cleaned_data['cliente_id']
            cliente = Cliente.objects.get(id=cliente_id)

            Pedido.objects.create(cliente=cliente)  # fecha se agrega sola si es auto_now_add
            return redirect('listar-pedidos')
    else:
        form = PedidoForm()
    
    return render(request, 'mi_primer_app/crear_pedido.html', {'form': form})

def agregar_detalle_pedido(request, pedido_id):
    if request.method == 'POST':
        form = DetallePedidoForm(request.POST)
        if form.is_valid():
            pedido = Pedido.objects.get(id=pedido_id)
            producto = Producto.objects.get(id=form.cleaned_data['producto_id'])
            cantidad = form.cleaned_data['cantidad_metros']
            precio_unitario = form.cleaned_data['precio_unitario']

            DetallePedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad_metros=cantidad,
                precio_unitario=precio_unitario
            )
            return redirect('listar-pedidos')  # o a una vista de detalle del pedido
    else:
        form = DetallePedidoForm()
    
    return render(request, 'mi_primer_app/crear_detalle_pedido.html', {'form': form})

#vistas basadas en clases para auto

class AutoListView(ListView):#nombre del modelo/lista/view
    model = Auto #campo para el modelo
    template_name = 'mi_primer_app/listar-autos.html' #campo para el template
    context_object_name = 'autos' #como se llama el campo al que se va a llamar, exactamente igual al listar en el html


class AutoCreateView(LoginRequiredMixin, CreateView):
    model = Auto #que modelo
    form_class = AutoForm #que formulario
    template_name = 'mi_primer_app/crear-auto.html' #que template
    success_url = reverse_lazy('listar-autos') #a donde queremos que vaya luego de creado (antiguo redirect)


#class AutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Auto
    form_class = AutoForm
    template_name = 'mi_primer_app/crear-auto.html'
    success_url = reverse_lazy('listar-autos')


#class AutoDetailView(LoginRequiredMixin, DetailView):
    model = Auto
    template_name = 'mi_primer_app/detalle-auto.html'
    context_object_name = 'auto'


#class AutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Auto
    template_name = 'mi_primer_app/eliminar-auto.html'
    success_url = reverse_lazy('listar-autos')