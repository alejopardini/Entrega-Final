from django.shortcuts import render

# Create your views here.
from . import models


def home(request):
    consulta_usuarios = models.Usuario.objects.all()
    context = {"usuarios": consulta_usuarios}
    return render(request, "usuario/index.html", context)
