# Generated by Django 2.2.17 on 2021-01-29 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionNeuroLab_Panel_de_Control', '0005_miembroslab_visitantelab'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembroslab',
            name='miembRoll',
            field=models.CharField(max_length=300, null=True, verbose_name='Roll'),
        ),
        migrations.AddField(
            model_name='visitantelab',
            name='visitaActividad',
            field=models.CharField(max_length=50, null=True, verbose_name='Actividad'),
        ),
    ]
