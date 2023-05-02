# GESTION PROCESAMIENTO DE DATOS
from django.contrib import admin

from gestionProcesamientoDatos.models import Procesamiento_Estudio, metodosPreprocesamiento, metodosPostprocesamiento
from gestionProcesamientoDatos.models import analisisCluster, analisisEstadisticaDescriptiva, analisisEstadisticaInferencial, Machine_LearningMetodo
# Register your models here.

#- Analisis Individuales

class Procesamiento_EstudioAdmin(admin.ModelAdmin):
	list_display=("nombre","categoriaEstudio","clave_Estudio","fechaEstudio","num_muestra","invResp","clave_Protocolo","participanteEstudio", "anaPre", "anaPost")
	search_fields=("nombre","fechaEstudio","clave_Estudio","clave_Protocolo","participanteEstudio", "anaPre", "anaPost")
	list_filter=("nombre","fechaEstudio","clave_Estudio","clave_Protocolo","participanteEstudio", "anaPre", "anaPost")
	date_hierarchy=("fechaEstudio")


class  metodosPreprocesamientoAdmin(admin.ModelAdmin):
	list_display=("nombreM_pre","clave_MetodoPre", "cfMetodoPre")
	search_fields=("nombreM_pre","clave_MetodoPre", "cfMetodoPre")
	list_filter=("nombreM_pre","clave_MetodoPre", "cfMetodoPre")
	#date_hierarchy=("fechaEstudio")


class  metodosPostprocesamientoAdmin(admin.ModelAdmin):
	list_display=("nombreM_post","clave_MetodoPost", "cfMetodoPost")
	search_fields=("nombreM_post","clave_MetodoPost", "cfMetodoPost")
	list_filter=("nombreM_post","clave_MetodoPost", "cfMetodoPost")
	#date_hierarchy=("fechaEstudio")

## -----------------------------##

#- Analisis de Clusters-Grupos
	
class analisisClusterAdmin(admin.ModelAdmin):
	list_display=("nombreCluster","claveCluster")
	search_fields=("nombreCluster", "claveCluster")
	list_filter=("nombreCluster","claveCluster")
	#date_hierarchy=("fechaEstudio")
	
class analisisEstadisticaDescriptivaAdmin(admin.ModelAdmin):
	list_display=("nombreAnalisisED","codigoAnalisisED", "cfAnalisisED")
	search_fields=("nombreAnalisisED","codigoAnalisisED", "cfAnalisisED")
	list_filter=("nombreAnalisisED","codigoAnalisisED", "cfAnalisisED")
	
class analisisEstadisticaInferencialAdmin(admin.ModelAdmin):
	list_display=("nombreAnalisisEI","codigoAnalisisEI", "cfAnalisisEI")
	search_fields=("nombreAnalisisEI","codigoAnalisisEI", "cfAnalisisEI")
	list_filter=("nombreAnalisisEI","codigoAnalisisEI", "cfAnalisisEI")
	

class Machine_LearningMetodoAdmin(admin.ModelAdmin):
	list_display=("nombreAnalisisML","codigoAnalisisML", "cfAnalisisML")
	search_fields=("nombreAnalisisML","codigoAnalisisML", "cfAnalisisML")
	list_filter=("nombreAnalisisML","codigoAnalisisML", "cfAnalisisML")
	
admin.site.register(Procesamiento_Estudio, Procesamiento_EstudioAdmin)
admin.site.register(metodosPreprocesamiento, metodosPreprocesamientoAdmin)
admin.site.register(metodosPostprocesamiento, metodosPostprocesamientoAdmin)
admin.site.register(analisisCluster, analisisClusterAdmin)

admin.site.register(analisisEstadisticaDescriptiva, analisisEstadisticaDescriptivaAdmin)
admin.site.register(analisisEstadisticaInferencial, analisisEstadisticaInferencialAdmin)
admin.site.register(Machine_LearningMetodo, Machine_LearningMetodoAdmin)
