# GESTION PLANIFICACION Y DESARROLLOS DE PROYECTOS NUEVOS
from django.contrib import admin
from gestionPlanificacion_y_Desarrollo_Proyectos_Nuevos.models import proyectoInvestigacion

# Register your models here.


class proyectoInvestigacionAdmin(admin.ModelAdmin):
	list_display=("protocoloEstudio", "clave_Protocolo", "tipoInvestigacion", "aceptadoDiseño_Metodológico", "fechaAceptacionDM", "aceptadoConsetimiento_Informado", "fechaAceptacionCI","fechaInicioInvestigacion", "investigadorResponsable1", "MP_IR1", "investigadorResponsable2", "MP_IR2", "investigadorResponsable3", "MP_IR3")
	search_fields=("protocoloEstudio", "clave_Protocolo", "tipoInvestigacion", "aceptadoDiseño_Metodológico", "fechaAceptacionDM", "aceptadoConsetimiento_Informado", "fechaAceptacionCI","fechaInicioInvestigacion", "investigadorResponsable1", "MP_IR1", "investigadorResponsable2", "MP_IR2", "investigadorResponsable3", "MP_IR3")
	list_filter=("protocoloEstudio", "clave_Protocolo", "tipoInvestigacion", "aceptadoDiseño_Metodológico", "fechaAceptacionDM", "aceptadoConsetimiento_Informado", "fechaAceptacionCI","fechaInicioInvestigacion", "investigadorResponsable1", "MP_IR1", "investigadorResponsable2", "MP_IR2", "investigadorResponsable3", "MP_IR3")
	date_hierarchy=("fechaInicioInvestigacion")
	
	
admin.site.register(proyectoInvestigacion, proyectoInvestigacionAdmin)
