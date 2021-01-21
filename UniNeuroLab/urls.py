"""UniNeuroLab URL Configuration

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
from django.contrib import admin
from django.urls import path
from gestionTomaDatos import views
from gestionProcesamientoDatos import views
from gestionProtocolos_y_Estudios import views
from gestionResultadosProtocolo import views
from gestionPlanificacion_y_Desarrollo_Proyectos_Nuevos import views
from gestionNeuroLab_Panel_de_Control import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('busquedaEstudios/', views.busquedaEstudios),
    #path("buscar/",views.buscar),
    #path("contacto/", views.contacto),
]
