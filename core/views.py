from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .forms import CustomAuthenticationForm, CustomUserCreationForm

def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def producto(request):
    return render(request, "core/producto.html")

def editar_producto(request):
    return render(request, "producto/index.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"

def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Autenticar al usuario después de registrarse
            messages.success(request, 'Cuenta creada exitosamente.')
            return redirect('core:home')
        else:
            messages.error(request, 'Por favor corrige los errores a continuación.')
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})
