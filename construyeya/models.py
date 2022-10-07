from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings
from .validators import validar_par 
from .validators import validar_nombre_categoria 
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, validators=[validar_nombre_categoria,]) 

    def __str__(self):
        return self.nombre

    class Meta:
        permissions = [
            ("reporte_cantidad", "Visualizar el reporte de cantidad"),
            ("reporte_detalle", "Reporte detallado de cantidades"),
        ]
class ProductUnits(models.TextChoices):
    UND = 'ud', 'Unidades'
    KG = 'kg', 'Kilogramo'   
    TON= 'ton','Tonelada'     

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True) 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    description = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    unidades = models.CharField(
        max_length=5,
        choices=ProductUnits.choices,
        default=ProductUnits.UND
    )
    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Producto - %s" % self.nombre

class Agencia(models.Model):
    nombreAgencia = models.CharField(max_length=150, unique=True)
    direccionAgencia = models.CharField(max_length=150)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
