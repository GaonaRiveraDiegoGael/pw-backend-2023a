# Importar una biblioteca administradora de rutas 
from django.urls import path
# Importando views del directorio actual
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("author/", views.author, name="author"),
    path("<str:name>", views.greet, name="greet")
]
