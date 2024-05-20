from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Producto
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models

def cervezas(request):
    cervezas_list = Producto.objects.filter(categoria_id__nombre='Cervezas')
    context = {
        'cervezas_list': cervezas_list
    }
    return render(request, "producto/cervezas.html",context)


def quesos(request):
    quesos_list = Producto.objects.filter(categoria_id__nombre='Quesos')
    context = {
        'quesos_list': quesos_list
    }
    return render(request, "producto/quesos.html",context)

def promociones(request):
    promociones_list = Producto.objects.filter(categoria_id__nombre='Promociones')
    context = {
        'promociones_list': promociones_list
    }
    return render(request, 'producto/promociones.html', context)


def home(request):
    return render(request, "producto/index.html")





def gin(request):
    productos_gin = Producto.objects.filter(categoria_id__nombre='Gin Artesanal')
    context = {
        'productos_gin': productos_gin
    }
    return render(request, 'producto/gin.html', context)



class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria

    # context_object_name = "productos"
    # template_name = "producto/productocategoria___list.html"

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.ProductoCategoria.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.ProductoCategoria.objects.all()
        return object_list


class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:home")



class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")




class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria
    




class ProductoCategoriaDelete(LoginRequiredMixin, DeleteView):
    model = models.ProductoCategoria
    
    success_url = reverse_lazy("producto:productocategoria_list")


# *** PRODUCTO


class ProductoList(ListView):
    model = models.Producto

    def get_queryset(self) -> QuerySet:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Producto.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Producto.objects.all()
        return object_list


class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:home")


class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")


class ProductoDetail(DetailView):
    model = models.Producto


class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")


