# ARCHIVO URLS DE LA APLICACION COORDINADORA
"""gestionNeuroLab_Panel_de_Control URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path , include
from gestionNeuroLab_Panel_de_Control import views
#from django.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('visualizarControlPanel/', views.visualizarControlPanel),
    #path('pcmiembros/', views.vermiembrosLab, name="Equipo"),
    #path('pcvisitante/', views.vervisitanteLab),
    path('home/', views.home, name="Home"), #faltaba esto
    path('pccontacto/', views.contacto, name= "Contacto"), # aca mezclo el css
	path('pcentorno/', views.blog, name="Entorno"), # aca mezclo el css
	path('pcproyectos/', views.proyectos, name="Proyectos"), # aca mezclo el css
	path('pcservicios/', views.servicios, name="Servicios"), # aca mezclo el css
	path('pcequipo/', views.miembros, name="Equipo"), # aca mezclo el css
	path('pcblog/', views.blog, name="Blog"), # aca mezclo el css
	
	# aca incluimos las url para la APP que se gestionaran desde el panel de control
	path('',include('gestionTomaDatos.urls')),
    path('',include('gestionProcesamientoDatos.urls')),
    path('',include('gestionResultadosProtocolo.urls')),
    path('',include('gestionProtocolos_y_Estudios.urls')),
    path('',include('gestionPlanificacion_y_Desarrollo_Proyectos_Nuevos.urls')),
]

#urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns+=static(settings.UNINEUROLAB_URL, document_root=settings.UNINEUROLAB_ROOT)
# necesito especificar donde esta la ruta para que se pueda conectar el formulario con la base de datos
