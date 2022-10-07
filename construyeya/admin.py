from django.contrib import admin
from .models import Categoria
from .models import Producto
from .models import Agencia
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio","description", "unidades")
    ordering = ["precio"]
    search_fields = ["nombre"]
    list_filter = ("disponible","precio")

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Agencia)