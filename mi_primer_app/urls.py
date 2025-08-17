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
    path('listar-clientes/', views.listar_clientes, name='listar-clientes'),#Anda OK
    #pedidos
    path('crear-pedido/', views.crear_pedido, name='crear-pedido'),#Anda OK
    path('listar-pedidos/', views.listar_pedidos, name='listar-pedidos'),
    # detalles de pedidos
    path('pedidos/<int:pedido_id>/agregar-detalle/', views.agregar_detalle_pedido, name='agregar-detalle-pedido'),
     #vistas basadas en clases
    path('crear-auto/', views.AutoCreateView.as_view(), name="crear-auto"),
    path('listar-autos/', views.AutoListView.as_view(), name="listar-autos"),
    path('detalle-auto/<int:pk>/',
         views.AutoDetailView.as_view(), name="detalle-auto"),
    path('editar/<int:pk>/', views.AutoUpdateView.as_view(), name='editar-auto'),
    path('eliminar/<int:pk>/', views.AutoDeleteView.as_view(), name='eliminar-auto'),
    path('about/', views.about, name='about'),
    #para los botones de detalle, ver, eliminar
    path('detalle-producto/<int:pk>/', views.ProductoDetailView.as_view(), name="detalle-producto"),
    path('editar-producto/<int:pk>/', views.ProductoUpdateView.as_view(), name="editar-producto"),
    path('eliminar-producto/<int:pk>/', views.ProductoDeleteView.as_view(), name="eliminar-producto"),
]