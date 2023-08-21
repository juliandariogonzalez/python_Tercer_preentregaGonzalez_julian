from django.shortcuts import render
from .models import *
from appCoder.forms import *
from django.http import HttpResponse



#Vista de inicio:

def inicio(request):
    return render(request, "appCoder/inicio.html")



#FORMULARIOS PARA REGISTRAR SUCURSAL EN BASE DE DATOS:

def sucursales(request):
    if request.method == "POST":
        form = FormularioSucursal(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre_sucursal = info["nombre_sucursal"]
            localidad_sucursal = info["localidad_sucursal"]
            sucursal= Sucursal(nombre_sucursal=nombre_sucursal,localidad_sucursal=localidad_sucursal)
            sucursal.save()
            sucursal_formulario=FormularioSucursal()
            return render(request, "appCoder/sucursales.html", {"mensaje":"Sucursal creada", "formulario":sucursal_formulario})
        return render(request,"appCoder/sucursales.html", {"mensaje": "datos invalidos"})
    else:
        sucursal_formulario = FormularioSucursal()
        return render(request, "appCoder/sucursales.html", {"formulario": sucursal_formulario})
    

#FORMULARIOS PARA REGISTRAR PRODUCTO EN BASE DE DATOS:

def productos(request):
    if request.method == "POST":
        form = FormularioProducto(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            tipo_producto = info["tipo_producto"]
            numero_producto = info["numero_producto"]
            producto= Producto(nombre=nombre, tipo_producto=tipo_producto, numero_producto=numero_producto)
            producto.save()
            producto_formulario=FormularioProducto()
            return render(request, "appCoder/productos.html", {"mensaje":"Producto creado", "formulario":producto_formulario})
        return render(request,"appCoder/productos.html", {"mensaje": "datos invalidos"})
    else:
        producto_formulario = FormularioProducto()
        return render(request, "appCoder/productos.html", {"formulario": producto_formulario})
    


#FORMULARIOS PARA REGISTRAR CLIENTE EN BASE DE DATOS:

def clientes(request):
    if request.method == "POST":
        formulario = FormularioCliente(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            telefono = info["telefono"]
            email =info["email"]
            cliente= Clientes(nombre=nombre, apellido=apellido, telefono=telefono, email=email )
            cliente.save()
            cliente_formulario=FormularioCliente()
            return render(request, "appCoder/clientes.html", {"mensaje":"Cliente creado", "formulario": cliente_formulario})
        else:
            return render(request,"appCoder/clientes.html", {"mensaje": "Datos invalidos"})
    else:
        cliente_formulario = FormularioCliente()
    
    return render(request, "appCoder/clientes.html", {"formulario": cliente_formulario})
    


#FORMULARIOS PARA PROGRAMAR LOS ENVIOS EN BASE DE DATOS:

def envios(request):
    if request.method == "POST":
        form = FormularioEnvio(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            fecha_de_entrega = info["fecha_de_entrega"]
            nombre_cadete = info["nombre_cadete"]
            envio= Envio(fecha_de_entrega=fecha_de_entrega, nombre_cadete=nombre_cadete)
            envio.save()
            envio_formulario=FormularioEnvio()
            return render(request, "appCoder/envios.html", {"mensaje":"Envio programado", "formulario":envio_formulario})
        return render(request,"appCoder/envios.html", {"mensaje": "datos invalidos"})
    else:
        envio_formulario = FormularioEnvio()
        return render(request, "appCoder/envios.html", {"formulario": envio_formulario})



#FORMULARIOS PARA PROGRAMAR LAS DEVOLUCIONES EN LA BASE DE DATOS:

def devoluciones(request):
    if request.method == "POST":
        form = FormularioDevolucion(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre_cliente = info["nombre_cliente"]
            apellido_cliente = info["apellido_cliente"]
            producto_devolucion = info["producto_devolucion"]
            motivo = info["motivo"]
            envio= Devolucion(nombre_cliente=nombre_cliente, apellido_cliente=apellido_cliente, producto_devolucion=producto_devolucion, motivo=motivo)
            envio.save()
            envio_formulario=FormularioDevolucion()
            return render(request, "appCoder/devoluciones.html", {"mensaje":"Devolucion programada", "formulario":envio_formulario})
        return render(request,"appCoder/devoluciones.html", {"mensaje": "datos invalidos"})
    else:
        envio_formulario = FormularioDevolucion()
        return render(request, "appCoder/devoluciones.html", {"formulario": envio_formulario})
    


#FORMULARIO DE BUSQUEDA DE PRODUCTO EN BD:

def BusquedaProductos(request):
    return render(request, "appCoder/busquedaproducto.html")

def buscar(request):
    nombre= request.GET["producto"]
    if nombre != "":
        productos= Producto.objects.filter(nombre__icontains=nombre)
        return render(request, "appCoder/resultadobusqueda.html", {"productos": productos})
    else:
        return render(request, "appCoder/resultadobusqueda.html", {"mensaje": "No se ingreso el producto a buscar!"})
    
