# Generated by Django 4.1.2 on 2023-07-12 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
