from django.db import models


#Modelos de objetos: 

class Sucursal(models.Model):
    nombre_sucursal = models.CharField(max_length=40)
    localidad_sucursal = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.nombre_sucursal} - {self.localidad_sucursal}"


class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    tipo_producto = models.CharField(max_length=30)
    numero_producto = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.tipo_producto} - {self.numero_producto}"


class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.telefono} - {self.email}"


class Envio(models.Model):
    fecha_de_entrega = models.IntegerField()
    nombre_cadete = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.fecha_de_entrega} - {self.nombre_cadete}"


class Devolucion(models.Model):
    nombre_cliente = models.CharField(max_length=30)
    apellido_cliente = models.CharField(max_length=30)
    producto_devolucion = models.CharField(max_length=30)
    motivo = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre_cliente} - {self.apellido_cliente} - {self.producto_devolucion} - {self.motivo}"

