from django.urls import path
from . import views

app_name = "usuario"

urlpatterns = [
    path("", views.home, name="home"),
    path("editar-perfil/", views.editar_perfil, name="editar_perfil"),
    path("perfil-actualizado/", views.perfil_actualizado, name="perfil_actualizado"),
]
