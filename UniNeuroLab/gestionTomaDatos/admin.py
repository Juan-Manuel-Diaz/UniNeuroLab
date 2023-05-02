# GESTION TOMA DATOS
from django.contrib import admin

from gestionTomaDatos.models import Participantes, Investigador_Clinico, Estudio, ProtocoloClinico, AdqData_EEG_Protocolo

# Register your models here.

# Para visualizar mas campos de la base de datos en
# el panel de administracion tengo que crear esta clase

class ParticipantesAdmin(admin.ModelAdmin):
	list_display=("nombre","apellido","DNI")
	search_fields=("nombre","apellido")
	list_filter=("nombre","apellido","DNI")
	
class EstudioAdmin(admin.ModelAdmin):
	list_display=("nombre","categoriaEstudio","clave_Estudio","fechaEstudio","num_muestra","invResp","clave_Protocolo","participanteEstudio")
	search_fields=("nombre","fechaEstudio","clave_Estudio","clave_Protocolo","participanteEstudio")
	list_filter=("nombre","fechaEstudio","clave_Estudio","clave_Protocolo","participanteEstudio")
	date_hierarchy=("fechaEstudio")
	
class Investigador_ClinicoAdmin(admin.ModelAdmin):
	list_display=("nombre", "apellido", "fechaNac", "MP", "email")
	search_fields=("nombre", "apellido", "fechaNac", "MP")
	list_filter=("nombre", "apellido", "fechaNac", "MP")
	date_hierarchy=("fechaNac")
	
	
class ProtocoloClinicoAdmin(admin.ModelAdmin):
	list_display=("protocoloEstudio", "clave_Protocolo", "tipoInvestigacion", "aceptadoDiseño_Metodológico", "fechaAceptacionDM", "aceptadoConsetimiento_Informado", "fechaAceptacionCI","fechaInicioInvestigacion", "investigadorResponsable1", "MP_IR1", "investigadorResponsable2", "MP_IR2", "investigadorResponsable3", "MP_IR3")
	search_fields=("protocoloEstudio", "clave_Protocolo", "tipoInvestigacion", "aceptadoDiseño_Metodológico", "fechaAceptacionDM", "aceptadoConsetimiento_Informado", "fechaAceptacionCI","fechaInicioInvestigacion", "investigadorResponsable1", "MP_IR1", "investigadorResponsable2", "MP_IR2", "investigadorResponsable3", "MP_IR3")
	list_filter=("protocoloEstudio", "clave_Protocolo", "tipoInvestigacion", "aceptadoDiseño_Metodológico", "fechaAceptacionDM", "aceptadoConsetimiento_Informado", "fechaAceptacionCI","fechaInicioInvestigacion", "investigadorResponsable1", "MP_IR1", "investigadorResponsable2", "MP_IR2", "investigadorResponsable3", "MP_IR3")
	date_hierarchy=("fechaInicioInvestigacion")
	

class AdqData_EEG_ProtocoloAdmin(admin.ModelAdmin):
	list_display=("nombre", "estadoConciencia", "condicionFisica", "estadoElectrofisiologico", "cantidad_EstadosElectrofisio", "duracion_Registro","numero_Canales", "sample_canales", "eegData")
	search_fields=("nombre", "estadoConciencia", "condicionFisica", "estadoElectrofisiologico", "cantidad_EstadosElectrofisio", "duracion_Registro","numero_Canales", "sample_canales")
	list_filter=("nombre", "estadoConciencia", "condicionFisica", "estadoElectrofisiologico", "cantidad_EstadosElectrofisio", "duracion_Registro","numero_Canales", "sample_canales")
	#date_hierarchy=("fechaInicioInvestigacion")
	


admin.site.register(Participantes,ParticipantesAdmin)
admin.site.register(Investigador_Clinico, Investigador_ClinicoAdmin)
admin.site.register(Estudio, EstudioAdmin)
admin.site.register(ProtocoloClinico, ProtocoloClinicoAdmin)
admin.site.register(AdqData_EEG_Protocolo, AdqData_EEG_ProtocoloAdmin)


