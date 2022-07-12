# Generated by Django 4.0.5 on 2022-06-16 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nombre_mascota', models.CharField(max_length=50)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'Veterinaria'], [1, 'Peluqueria'], [2, 'Consulta']])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
    ]