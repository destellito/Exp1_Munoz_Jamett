# Generated by Django 4.1.2 on 2023-06-28 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_producto_id_alter_producto_idproducto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='idproducto',
        ),
    ]
