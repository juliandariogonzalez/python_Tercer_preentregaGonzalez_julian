# Generated by Django 4.2.4 on 2023-08-21 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appCoder', '0003_rename_numero_cliente_clientes_telefono_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='fecha_de_compra',
        ),
    ]
