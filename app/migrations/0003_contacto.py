# Generated by Django 3.1.2 on 2020-11-07 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('correo', models.EmailField(max_length=254)),
                ('motivo_consulta', models.IntegerField(choices=[[0, 'felicitaciones'], [1, 'reclamos'], [2, 'sugerencias'], [3, 'consultas']])),
                ('mensaje', models.TextField()),
            ],
        ),
    ]
