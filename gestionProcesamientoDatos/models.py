# GESTION PROCESAMIENTO DE DATOS
from django.db import models

# Create your models here.


# CREAR UNA CLASE POR CADA TABLA DE NUESTRA BASE DE DATOS


class Procesamiento_Estudio(models.Model):
	nombre=models.CharField(max_length=30, verbose_name="Nombre del Estudio")
	categoriaEstudio=models.CharField(max_length=30, verbose_name="Categoria")
	fechaEstudio=models.DateField(verbose_name="Fecha del Estudio")
	clave_Estudio=models.IntegerField(verbose_name= "ID de Estudio")
	num_muestra=models.IntegerField(verbose_name="Numero de Muestra")
	invResp=models.CharField(max_length=30, verbose_name="Investigador Responsable")
	protocoloEstudio=models.CharField(max_length=30, verbose_name="Nombre del Protocolo") 
	clave_Protocolo=models.IntegerField(null= True,verbose_name= "ID de Protocolo")
	participanteEstudio=models.IntegerField(verbose_name="ID del Participante")
	anaPre=models.CharField(blank=True, null= True, max_length=30, verbose_name="Analisis de Preprocesamiento")
	efectuadoPre=models.BooleanField(blank=True, null= True) # este es un comentario
	anaPost=models.CharField(blank=True, null= True, max_length=30, verbose_name="Analisis de Postprocesamiento")
	efectuadoPost=models.BooleanField(blank=True, null= True) # este es un comentario


class metodosPreprocesamiento(models.Model):
	nombreM_pre=models.CharField(max_length=30, verbose_name="Nombre del Método")
	clave_MetodoPre=models.IntegerField(verbose_name= "ID del Metodo_pre")
	cfMetodoPre=models.CharField(max_length=30, verbose_name="Codigo Fuente del Metodo")
	
	
class metodosPostprocesamiento(models.Model):
	nombreM_post=models.CharField(max_length=30, verbose_name="Nombre del Método")
	clave_MetodoPost=models.IntegerField(verbose_name= "ID del Metodo_post")
	cfMetodoPost=models.CharField(max_length=30, verbose_name="Codigo Fuente del Metodo")
	
##--------------------------------------##

class analisisCluster(models.Model):
	nombreCluster=models.CharField(max_length=30, verbose_name="Nombre del Estudio")
	claveCluster=models.IntegerField(verbose_name= "ID de Cluster")
	
	
class analisisEstadisticaDescriptiva(models.Model):
	nombreAnalisisED= models.CharField(max_length=30, verbose_name="Nombre AED")
	codigoAnalisisED= models.IntegerField(verbose_name= "ID de AED")
	cfAnalisisED= models.CharField(max_length=30, verbose_name="Codigo Fuente del AED")
	
class analisisEstadisticaInferencial(models.Model):
	nombreAnalisisEI= models.CharField(max_length=30, verbose_name="Nombre AEI")
	codigoAnalisisEI= models.IntegerField(verbose_name= "ID de AEI")
	cfAnalisisEI= models.CharField(max_length=30, verbose_name="Codigo Fuente del AEI")	
	
class Machine_LearningMetodo(models.Model):
	nombreAnalisisML= models.CharField(max_length=30, verbose_name="Nombre AML")
	codigoAnalisisML= models.IntegerField(verbose_name= "ID de AML")
	cfAnalisisML= models.CharField(max_length=30, verbose_name="Codigo Fuente del AML")
	
