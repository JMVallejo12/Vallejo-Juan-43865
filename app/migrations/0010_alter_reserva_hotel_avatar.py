# Generated by Django 4.2.3 on 2023-08-13 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0009_alter_reserva_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='hotel',
            field=models.CharField(choices=[('Skybay Hotel Gyeongpo', 'Skybay Hotel Gyeongpo'), ('Paradise Hotel Busan', 'Paradise Hotel Busan'), ('Lotte Hotel Busan', 'Lotte Hotel Busan'), ('Hotel Skypark Kingstown Dongdaemun', 'Hotel Skypark Kingstown Dongdaemun'), ('The Shilla Jeju', 'The Shilla Jeju'), ('Maison Glad Jeju', 'Maison Glad Jeju'), ('Grand Walkerhill', 'Grand Walkerhill'), ('Nine Tree Premier Hotel Myeongdong II', 'Nine Tree Premier Hotel Myeongdong II'), ('Nine Tree Premier Hotel Insadong', 'Nine Tree Premier Hotel Insadong'), ('Dormy Inn', 'Dormy Inn')], max_length=50),
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotoPerfil', models.ImageField(upload_to='fotosPerfil')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
