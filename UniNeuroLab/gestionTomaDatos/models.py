# MODELS GESTION TOMA DATOS
from django.db import models


#from matrix_field import MatrixField

# Create your models here.

# CREAR UNA CLASE POR CADA TABLA DE NUESTRA BASE DE DATOS

class Participantes(models.Model):
	nombre=models.CharField(max_length=30)
	apellido=models.CharField(max_length=30)
	fechaNac=models.DateField(verbose_name="Fecha de Nacimiento")
	DNI=models.IntegerField()
	direccion=models.CharField(max_length=50)
	email=models.EmailField(blank=True, null= True) # Acepta email y nulo
	tfno=models.CharField(max_length=15, verbose_name="Telefono")
	
	def __str__(self):
		return 'El participante es ', (self.nombre), (self.apellido)
	
class Investigador_Clinico(models.Model):
	nombre=models.CharField(max_length=30)
	apellido=models.CharField(max_length=30)
	fechaNac=models.DateField(verbose_name="Fecha de Nacimiento")
	DNI=models.IntegerField()
	MP=models.IntegerField(verbose_name="Matricula Profesional")
	direccion=models.CharField(max_length=50)
	email=models.EmailField()
	tfno=models.CharField(max_length=15, verbose_name="Telefono")
	
	#def __str__(self):
		#return 'El investigador es: ' %(self.nombre, self.apellido)
	
class Estudio(models.Model):
	nombre=models.CharField(max_length=30, verbose_name="Nombre del Estudio")
	categoriaEstudio=models.CharField(max_length=30, verbose_name="Categoria")
	fechaEstudio=models.DateField(verbose_name="Fecha del Estudio")
	clave_Estudio=models.IntegerField(verbose_name= "ID de Estudio")
	num_muestra=models.IntegerField(verbose_name="Numero de Muestra")
	invResp=models.CharField(max_length=30, verbose_name="Investigador Responsable")
	protocoloEstudio=models.CharField(max_length=30, verbose_name="Nombre del Protocolo") 
	clave_Protocolo=models.IntegerField(null= True,verbose_name= "ID de Protocolo")
	participanteEstudio=models.IntegerField(verbose_name="ID del Participante")
	efectuado=models.BooleanField() # este es un comentario


class ProtocoloClinico(models.Model):
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
	
class AdqData_EEG_Protocolo(models.Model):
	nombre=models.CharField(max_length=50, verbose_name="Nombre del Estudio")
	estadoConciencia=models.CharField(max_length=50, verbose_name="Estado de Conciencia") # Vigilia-Dormido-Coma-Sedado
	condicionFisica=models.CharField(max_length=50, verbose_name="Condicion Fisica") # Reposo - Esfuerzo - Relajado
	estadoElectrofisiologico=models.CharField(max_length=150, verbose_name="Estado Electrofisiológico") # Reposo Ojos Cerrado- Reposo Ojos Abiertos - Hiperventilacion - Optoestimulacio -Suelo REM -Sueño No REM etc
	cantidad_EstadosElectrofisio=models.IntegerField(null= True,verbose_name= "N° de Estados Electrofisiologicos")
	duracion_Registro=models.IntegerField(null= True,verbose_name= "Duracion del Registro: min.")
	numero_Canales=models.IntegerField(null= True,verbose_name= "Numero de Canales") #20 - 32 - 64
	sample_canales=models.IntegerField(null= True,verbose_name= "Tasa de Muestreo: Hz") # 65Hz - 128Hz - 256Hz 512Hz
	eegData=models.CharField(null= True, max_length=50, verbose_name="Raw Signals") # aca va la matriz de datos como un objeto en un lugar en la memoria

#    class EEG_Data(models.Model):
#    eegValue = MatrixField(datatype='float', dimensions=(3, 2))
#    eegChannel = MatrixField(datatype='str', dimensions=(2,))
