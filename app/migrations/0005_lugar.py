# Generated by Django 4.2.3 on 2023-08-12 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_ciudad_superficie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=50)),
                ('precioEntrada', models.CharField(max_length=50)),
            ],
        ),
    ]