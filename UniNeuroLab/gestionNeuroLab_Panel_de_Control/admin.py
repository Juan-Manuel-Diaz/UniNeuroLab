# GESTION PANEL DE CONTROL
from django.contrib import admin
from gestionNeuroLab_Panel_de_Control.models import APP_TableroControl #, gestionTomaDatos , gestionProcesamientoDatos, gestionProtocolos_y_Estudios, gestionResultadosProtocolo, gestionPlanificacion_y_Desarrollo_Proyectos_Nuevos


# Register your models here.



class APP_TableroControlAdmin(admin.ModelAdmin):
	list_display=("appsNombre", "appsNumero", "appsBDnombres", "appsBDcantidad")
	search_fields=("appsNombre", "appsNumero", "appsBDnombres", "appsBDcantidad")
	list_filter=("appsNombre", "appsNumero")
	#date_hierarchy=("fechaInicioInvestigacion")
	
	
admin.site.register(APP_TableroControl, APP_TableroControlAdmin)
