# GESTION RESULTADOS PROTOCOLOS
from django.contrib import admin
from gestionResultadosProtocolo.models import resultadosProtocolo
# Register your models here.


class resultadosProtocoloAdmin(admin.ModelAdmin):
	list_display=("protocoloEstudio", "clave_Protocolo", "tipoInvestigacion", "aceptadoDiseño_Metodológico", "fechaAceptacionDM", "aceptadoConsetimiento_Informado", "fechaAceptacionCI","fechaInicioInvestigacion", "investigadorResponsable1", "MP_IR1", "investigadorResponsable2", "MP_IR2", "investigadorResponsable3", "MP_IR3")
	search_fields=("protocoloEstudio", "clave_Protocolo", "tipoInvestigacion", "aceptadoDiseño_Metodológico", "fechaAceptacionDM", "aceptadoConsetimiento_Informado", "fechaAceptacionCI","fechaInicioInvestigacion", "investigadorResponsable1", "MP_IR1", "investigadorResponsable2", "MP_IR2", "investigadorResponsable3", "MP_IR3")
	list_filter=("protocoloEstudio", "clave_Protocolo", "tipoInvestigacion", "aceptadoDiseño_Metodológico", "fechaAceptacionDM", "aceptadoConsetimiento_Informado", "fechaAceptacionCI","fechaInicioInvestigacion", "investigadorResponsable1", "MP_IR1", "investigadorResponsable2", "MP_IR2", "investigadorResponsable3", "MP_IR3")
	date_hierarchy=("fechaInicioInvestigacion")
	
	
admin.site.register(resultadosProtocolo, resultadosProtocoloAdmin)
