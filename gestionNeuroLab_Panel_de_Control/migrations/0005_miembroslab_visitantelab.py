# Generated by Django 2.2.17 on 2021-01-29 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionNeuroLab_Panel_de_Control', '0004_auto_20210121_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiembrosLab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miembNombre', models.CharField(max_length=50, verbose_name='Miembro')),
            ],
        ),
        migrations.CreateModel(
            name='VisitanteLab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitaNombre', models.CharField(max_length=50, verbose_name='Visitante')),
            ],
        ),
    ]