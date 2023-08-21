from django import forms

#Clases de Objetos creados, PARA CREAR LOS FORMULARIOS

class FormularioSucursal(forms.Form):
    nombre_sucursal = forms.CharField(max_length=40)
    localidad_sucursal = forms.CharField(max_length=40)
 
class FormularioProducto(forms.Form):
    nombre = forms.CharField(max_length=30)
    tipo_producto = forms.CharField(max_length=30)
    numero_producto = forms.IntegerField()

class FormularioCliente(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    telefono = forms.IntegerField()
    email = forms.EmailField()
   
class FormularioEnvio(forms.Form):
    fecha_de_entrega = forms.IntegerField()
    nombre_cadete = forms.CharField(max_length=30)

class FormularioDevolucion(forms.Form):
    nombre_cliente = forms.CharField(max_length=30)
    apellido_cliente = forms.CharField(max_length=30)
    producto_devolucion = forms.CharField(max_length=30)
    motivo = forms.CharField(max_length=50)

