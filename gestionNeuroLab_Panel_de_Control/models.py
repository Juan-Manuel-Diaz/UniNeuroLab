# GESTION PANEL DE CONTROL
from django.db import models
#from gestionNeuroLab_Panel_de_Control import gestionTomaDatos, gestionProcesamientoDatos, gestionProtocolos_y_Estudios, gestionResultadosProtocolo, gestionPlanificacion_y_Desarrollo_Proyectos_Nuevos

# Create your models here.

class APP_TableroControl(models.Model):
	appsNombre=models.CharField(max_length=300, verbose_name="Nombre del APPs")
	appsNumero=models.IntegerField(null= True,verbose_name= "ID de APPs")
	appsBDnombres=models.CharField(blank=True, null= True,max_length=300, verbose_name="Bases de Datos de la APPs")
	appsBDcantidad=models.IntegerField(null= True,verbose_name= "N°BD de la APPs")
