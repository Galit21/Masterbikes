# Generated by Django 5.2.3 on 2025-06-17 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterbikes_app', '0002_rename_contraseña_producto_contrasena'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contrasena', models.CharField(max_length=128)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=15)),
                ('rut', models.CharField(max_length=12)),
                ('id_rol', models.IntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
