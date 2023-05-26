# Importar una biblioteca administradora de rutas 
from django.urls import path

# importando pistas
from . import views

# Declarando las rutas validas
urlpatterns = [
    path("", views.index, name="index")
]
