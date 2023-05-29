from django.urls import path
# Importando views del directorio actual
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("author/", views.author, name="author"),
    path("<str:name>", views.greet, name="greet")
]

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def author(request):
    return HttpResponse("Hello Author 👨‍🎤")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitilize()
    })