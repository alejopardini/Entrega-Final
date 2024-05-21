from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import UsuarioForm

@login_required
def home(request):
    consulta_usuarios = Usuario.objects.all()
    context = {"usuarios": consulta_usuarios}
    return render(request, "usuario/index.html", context)

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('core:home')  # Redirigir al inicio después de actualizar el perfil
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario/editar_perfil.html', {'form': form})

@login_required
def perfil_actualizado(request):
    return render(request, 'usuario/perfil_actualizado.html')

