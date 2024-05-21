from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = "core"


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("about/", views.about, name="about"),
    path("producto/", views.producto, name="producto"),
    path("editar_producto/", views.editar_producto, name="editar_producto"),
    
]

urlpatterns += staticfiles_urlpatterns()
