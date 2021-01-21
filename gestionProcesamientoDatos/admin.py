# GESTION PROCESAMIENTO DE DATOS
from django.contrib import admin

from gestionProcesamientoDatos.models import PROC_Estudio, metodosPreprocesamiento, metodosPostprocesamiento
# Register your models here.


class PROC_EstudioAdmin(admin.ModelAdmin):
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
	
	
admin.site.register(PROC_Estudio, PROC_EstudioAdmin)
admin.site.register(metodosPreprocesamiento, metodosPreprocesamientoAdmin)
admin.site.register(metodosPostprocesamiento, metodosPostprocesamientoAdmin)
