# Comandos para configurar nuestra identidad:

# git config --global user.name "nombre apellido"
# git config --global user.email "nombre@example.com"

# git init  Se usa una sola vez (crea capeta .git)


# Se usan cuando nosotros queramos:
# git status  Muestra el estado del repo (archivos modificados, no agregados, etc.)
# git log  Muestra el historial de commits

# Se repiten siempre que haya cambios:
# git add .  Agrega todos los archivos al repo
# git commit -m "mensaje"  Crea un commit con los archivos agregados (etiqueta de info)
# git push origin main  Sube los cambios al repositorio remoto (GitHub, GitLab, etc.)

# ramas:
# crear y movernos a rama nueva:
# git checkout -b "funciones-nuevas" (el nombre de la rama no puede tener espacios)

# movernos a rama existente:
# git checkout "main"

# ver ramas:
# git branch (para ver en que rama estoy)

# juntar ramas en main:
# git merge "funciones-nuevas"

#Templates PADRE.HTML
#{% block NOMBRE DEL BLOQUE %} + {% endblock %}
#en el template de mi primer app, ponemos al principio {% extends "padre.html" %}
