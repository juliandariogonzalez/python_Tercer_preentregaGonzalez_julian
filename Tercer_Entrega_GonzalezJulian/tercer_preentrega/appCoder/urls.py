from django.urls import path
from .views import *

#URLS DE LAS VIEWS
urlpatterns = [
    path("sucursales/", sucursales, name = "sucursales" ),
    path("productos/", productos, name="productos"),
    path("clientes/", clientes, name="clientes"),
    path("envios/", envios, name="envios"),
    path("devoluciones/", devoluciones, name="devoluciones"),
    path("busquedaproducto", BusquedaProductos, name="busquedaproducto"),
    path("buscar/", buscar, name="buscar")
]