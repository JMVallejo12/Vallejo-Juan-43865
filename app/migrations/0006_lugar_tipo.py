# Generated by Django 4.2.3 on 2023-08-12 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_lugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugar',
            name='tipo',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
