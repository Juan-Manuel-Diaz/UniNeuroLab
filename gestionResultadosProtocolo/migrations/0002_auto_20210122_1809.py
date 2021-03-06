# Generated by Django 2.2.17 on 2021-01-22 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionResultadosProtocolo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='resultadosVisualizacionGrafica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave_Protocolo', models.IntegerField(null=True, verbose_name='ID de Protocolo')),
                ('nombreAnalisisFinal', models.CharField(max_length=300, verbose_name='Nombre del Analisis Final')),
                ('graficoAnalisisFinal', models.CharField(max_length=300, verbose_name='Gráfico del Analisis Final')),
            ],
        ),
        migrations.CreateModel(
            name='resultadosVisualizacionTablas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave_Protocolo', models.IntegerField(null=True, verbose_name='ID de Protocolo')),
                ('nombreAnalisisFinal', models.CharField(max_length=300, verbose_name='Nombre del Analisis Final')),
                ('tablaAnalisisFinal', models.CharField(max_length=300, verbose_name='Tabla del Analisis Final')),
            ],
        ),
        migrations.AddField(
            model_name='resultadosprotocolo',
            name='fechaCierreInvestigacion',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha Cierre de Investigacion'),
        ),
    ]
