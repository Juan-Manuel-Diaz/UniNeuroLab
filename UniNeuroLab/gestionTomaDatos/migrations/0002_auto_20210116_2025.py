# Generated by Django 2.2.17 on 2021-01-16 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionTomaDatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantes',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]