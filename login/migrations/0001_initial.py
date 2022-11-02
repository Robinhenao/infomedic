# Generated by Django 3.2.16 on 2022-10-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('telefono', models.CharField(max_length=20, verbose_name='Telefono')),
                ('correo', models.CharField(max_length=100, unique=True, verbose_name='Correo')),
                ('password', models.CharField(max_length=20, verbose_name='Contrase;a')),
            ],
        ),
    ]