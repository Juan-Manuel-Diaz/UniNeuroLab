# ESTE ES EL VIEWS DE gestionTomaDatos
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q  # faltaba esta libreria
from gestionTomaDatos.models import Estudio

from django.core.mail import send_mail
from django.conf import settings
#from gestionTomaDatos.forms import FormularioContacto


# Create your views here.

def inputData(request):
	
	return render(request, "inputData.html")


def inputParticipante(request):
	
	return render(request, "inputParticipante.html")

def inputEstudio(request):
	
	return render(request, "inputEstudio.html")
	
	

	
	
# ACA ES NECESARIO CONECTAR CON POSGRESSQL
def busquedaEstudios(request):
	
	return render(request, "busquedaEstudios.html")
	
def buscar(request):
	
	if request.GET['metodo de estudio']:
		
		#mensaje="El estudio buscado es: ", request.GET["Estudio"] # rescatar lo del corchete para que busque en la base de datos!!
		est= request.GET['metodo de estudio']
		
		if len(est)>20:
			mensaje="El texto es muy largo"
			
		else:
			
			estudioBDrecuperado= Estudio.objects.filter(Q(nombre__icontains=est)) # aqui el problema
			return render(request,"resultados_busqueda.html", {"estudios":estudioBDrecuperado,"query":est})
		
	else:
		mensaje="Usted no esta buscando nada"
	
	return HttpResponse(mensaje)
	

		

