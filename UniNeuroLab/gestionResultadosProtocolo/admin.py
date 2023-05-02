# GESTION RESULTADOS PROTOCOLOS
from django.contrib import admin
from gestionResultadosProtocolo.models import resultadosProtocolo, resultadosVisualizacionGrafica, resultadosVisualizacionTablas
# Register your models here.


class resultadosProtocoloAdmin(admin.ModelAdmin):
	list_display=("protocoloEstudio", "clave_Protocolo", "tipoInvestigacion", "aceptadoDiseño_Metodológico", "fechaAceptacionDM", "aceptadoConsetimiento_Informado", "fechaAceptacionCI","fechaCierreInvestigacion","fechaInicioInvestigacion", "investigadorResponsable1", "MP_IR1", "investigadorResponsable2", "MP_IR2", "investigadorResponsable3", "MP_IR3")
	search_fields=("protocoloEstudio", "clave_Protocolo", "tipoInvestigacion", "aceptadoDiseño_Metodológico", "fechaAceptacionDM", "aceptadoConsetimiento_Informado", "fechaAceptacionCI","fechaCierreInvestigacion","fechaInicioInvestigacion", "investigadorResponsable1", "MP_IR1", "investigadorResponsable2", "MP_IR2", "investigadorResponsable3", "MP_IR3")
	list_filter=("protocoloEstudio", "clave_Protocolo", "tipoInvestigacion", "aceptadoDiseño_Metodológico", "fechaAceptacionDM", "aceptadoConsetimiento_Informado", "fechaAceptacionCI","fechaCierreInvestigacion","fechaInicioInvestigacion", "investigadorResponsable1", "MP_IR1", "investigadorResponsable2", "MP_IR2", "investigadorResponsable3", "MP_IR3")
	date_hierarchy=("fechaInicioInvestigacion")
	
class resultadosVisualizacionGraficaAdmin(admin.ModelAdmin):
	list_display=("clave_Protocolo", "nombreAnalisisFinal", "graficoAnalisisFinal")
	search_fields=("clave_Protocolo", "nombreAnalisisFinal", "graficoAnalisisFinal")
	list_filter=("clave_Protocolo", "nombreAnalisisFinal", "graficoAnalisisFinal")
	#date_hierarchy=("clave_Protocolo", "nombreAnalisisFinal", "graficoAnalisisFinal")


class resultadosVisualizacionTablasAdmin(admin.ModelAdmin):
	list_display=("clave_Protocolo","nombreAnalisisFinal", "tablaAnalisisFinal")
	search_fields=("clave_Protocolo","nombreAnalisisFinal", "tablaAnalisisFinal")
	list_filter=("clave_Protocolo","nombreAnalisisFinal", "tablaAnalisisFinal")
	#date_hierarchy=("clave_Protocolo","nombreAnalisisFinal", "tablaAnalisisFinal")



admin.site.register(resultadosProtocolo, resultadosProtocoloAdmin)

admin.site.register(resultadosVisualizacionGrafica, resultadosVisualizacionGraficaAdmin)
admin.site.register(resultadosVisualizacionTablas, resultadosVisualizacionTablasAdmin)
