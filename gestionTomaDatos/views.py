from django.shortcuts import render
from django.http import HttpResponse
from gestionTomaDatos.models import Estudio
from django.core.mail import send_mail
from django.conf import settings
from gestionTomaDatos.forms import FormularioContacto


# Create your views here.

def busquedaEstudios(request):
	
	return render(request, "busquedaEstudios.html")
	
def buscar(request):
	
	if request.GET["Estudio"]:
		
		#mensaje="El estudio buscado es: ", request.GET["Estudio"] # rescatar lo del corchete para que busque en la base de datos!!
		est= request.GET["Estudio"]
		
		if len(est)>20:
			mensaje="El texto es muy largo"
			
		else:
			
			estudioBDrecuperado= Estudio.objects.filter(nombre__icontains= est) # aqui el problema
			return render(request,"resultados_busqueda.html", {"estudios":estudioBDrecuperado,"query":est})
		
	else:
		mensaje="Usted no esta buscando nada"
	
	return HttpResponse(mensaje)
	
	
def contacto(request):
	
	if request.method== "POST":
		
		miFormulario1=FormularioContacto(request.POST)
		
		if  miFormulario1.is_valid():
			
			infForm= miFormulario1.cleaned_data
			
			send_mail(infForm['asunto'],infForm['mensaje'],
			infForm.get('email',''),['juan.manuel.diaz@unc.edu.ar'],)
			
			return render(request, "gracias.html")
			
	else:
		miFormulario1=FormularioContacto()
			
	return render(request, "formulario_contacto.html",{"form":miFormulario1})
		
		#subject=request.POST["asunto"]
		#message=request.POST["mensaje"]+" "+request.POST["email"]
		#email_from=settings.EMAIL_HOST_USER
		#recipient_list=["juan.manuel.diaz@unc.edu.ar"]
		#send_mail(subject,message,email_from,recipient_list)
		#return render(request, "gracias.html")'''
		
		
		
	#return render(request, "contacto.html") '''
