# Generated by Django 3.2.8 on 2021-10-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='nit',
            field=models.IntegerField(blank=True, max_length=9, null=True, verbose_name='Nit'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='numero',
            field=models.IntegerField(blank=True, max_length=9, null=True, verbose_name='Numero de contacto'),
        ),
    ]