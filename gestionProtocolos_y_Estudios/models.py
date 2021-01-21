# GESTION PROTOCOLOS Y ESTUDIOS
from django.db import models

# Create your models here.



class direccionProtocolo(models.Model):
	protocoloEstudio=models.CharField(max_length=300, verbose_name="Nombre del Protocolo")
	clave_Protocolo=models.IntegerField(null= True,verbose_name= "ID de Protocolo")
	tipoInvestigacion=models.CharField(max_length=150, verbose_name="Tipo de Investigacion")
	aceptadoDiseño_Metodológico=models.BooleanField(verbose_name="Aceptacion Diseño Metodológico") # este es un comentario
	fechaAceptacionDM=models.DateField(verbose_name="Fecha Diseño Metodológico")
	aceptadoConsetimiento_Informado=models.BooleanField(verbose_name="Aceptacion Consentimiento Informado") # este es un comentario
	fechaAceptacionCI=models.DateField(verbose_name="Fecha Consentimiento Informado")
	fechaInicioInvestigacion=models.DateField(verbose_name="Fecha Inicion de Investigacion")
	investigadorResponsable1=models.CharField(max_length=30, verbose_name="Investigador Responsable 1- IR_1")
	MP_IR1=models.IntegerField(verbose_name="Matricula Profesional IR_1")
	investigadorResponsable2=models.CharField(blank=True, null= True, max_length=30, verbose_name="Investigador Responsable 2- IR_2")
	MP_IR2=models.IntegerField(blank=True, null= True, verbose_name="Matricula Profesional IR_2")
	investigadorResponsable3=models.CharField(blank=True, null= True, max_length=30, verbose_name="Investigador Responsable 3- IR_3")
	MP_IR3=models.IntegerField(blank=True, null= True, verbose_name="Matricula Profesional IR_3")
	
