from django.db import models

# Create your models here.

# CREAR UNA CLASE POR CADA TABLA DE NUESTRA BASE DE DATOS

class Participantes(models.Model):
	nombre=models.CharField(max_length=30)
	apellido=models.CharField(max_length=30)
	fechaNac=models.DateField()
	DNI=models.IntegerField()
	direccion=models.CharField(max_length=50)
	email=models.EmailField()
	tfno=models.CharField(max_length=15)
	
class Investigador_Clinico(models.Model):
	nombre=models.CharField(max_length=30)
	apellido=models.CharField(max_length=30)
	fechaNac=models.DateField()
	DNI=models.IntegerField()
	MP=models.IntegerField()
	direccion=models.CharField(max_length=50)
	email=models.EmailField()
	tfno=models.CharField(max_length=15)
	
class Estudio(models.Model):
	nombre=models.CharField(max_length=30)
	categoriaEstudio=models.CharField(max_length=30)
	fechaEstudio=models.DateField()
	clave_Estudio=models.IntegerField()
	num_muestra=models.IntegerField()
	invResp=models.CharField(max_length=30)
	protocoloEstudio=models.CharField(max_length=30) 
	participanteEstudio=models.IntegerField()
	efectuado=models.BooleanField() # este es un comentario


