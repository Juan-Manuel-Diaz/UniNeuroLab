# Generated by Django 2.2.17 on 2021-01-22 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionProcesamientoDatos', '0003_metodospostprocesamiento_metodospreprocesamiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='analisisCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCluster', models.CharField(max_length=30, verbose_name='Nombre del Estudio')),
                ('claveCluster', models.IntegerField(verbose_name='ID de Cluster')),
            ],
        ),
    ]