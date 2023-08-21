from django.contrib import admin
from .models import *

#REGISTRO DE MODELOS
admin.site.register(Sucursal)
admin.site.register(Producto)
admin.site.register(Clientes)
admin.site.register(Envio)
admin.site.register(Devolucion)