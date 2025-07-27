#para instalar django:

# pip install django
# pip3 install django
# python -m pip install django
# python3 -m pip install django
# py -m pip install django

# Crear proyecto Django:
# django-admin startproject mi_primer_proyecto .
# python -m django startproject mi_primer_proyecto .
# py -m django startproject mi_primer_proyecto .
# python3 -m django startproject mi_primer_proyecto .

# ejecutar proyecto:
# python manage.py runserver

#mi proyecto es http://127.0.0.1:8000/

#comando para ir ejecutando cada vez que hago cambios en el models.py de Mi_primer_app
#manage.py makemigrations (sirve para generar el script en la carpeta migrations )
#manage.py migrate (migra todo de la carpeta migrations a la DB sql y crea las tablas..)

#en el peor de los casos, cuando no funcione la funcion makemigrations o migrate, lo que debo hacer es borrar la carpeta INITIAL de la carpeta MIGRATIONS