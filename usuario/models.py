from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="país")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "países"


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    username = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
