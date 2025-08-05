from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hola-mundo/', views.hola_mundo, name='hola-mundo'),#cuando entramos a hola mundo, se ejecuta el view
    path('crear-familiar/<str:nombre>/',
         views.crear_familiar, name='crear-familiar'),
    path('listar-familiares/', views.listar_familiares, name="listar-familiares"),
    path('crear-curso/',
         views.crear_curso, name='crear-curso'),
    path('listar-cursos/', views.listar_cursos, name="listar-cursos"),
    path('cursos/buscar', views.buscar_cursos, name="buscar-cursos"),#para buscar cursos
    path('crear-estudiante/',
         views.crear_estudiante, name='crear-estudiante'),
    path('listar-estudiantes/', views.listar_estudiantes,
         name="listar-estudiantes"),


 #Los PATH a continuacion son.. para el proyecto
    path('crear-producto/', views.crear_producto, name='crear-producto'),#Anda OK
    path('listar-productos/', views.listar_productos, name='listar-productos'),#Anda OK
    path('productos/buscar/', views.buscar_productos, name='buscar-productos'),#Anda OK
    #clientes
    path('crear-cliente/', views.crear_cliente, name='crear-cliente'),#Anda OK
    path('listar-clientes/', views.listar_clientes, name='listar-clientes'),#Ver si Funciona
    #pedidos
    path('crear-pedido/', views.crear_pedido, name='crear-pedido'),#Ver si funciona
    path('listar-pedidos/', views.listar_pedidos, name='listar-pedidos'),
    # detalles de pedidos
    path('pedidos/<int:pedido_id>/agregar-detalle/', views.agregar_detalle_pedido, name='agregar-detalle-pedido'),

]