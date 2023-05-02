# Este es el views del Panel de Control
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import FormularioContacto
#from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.



	
def home(request):
	
	return render(request, "home.html")

def servicios(request):
	return render(request, "servicios.html")

def miembros(request):
	return render(request, "miembros.html")

def proyectos(request):
	return render(request, "proyectos.html")



def blog(request):
	return render(request, "blog.html")


def contacto(request):
	
	formulario_contacto=FormularioContacto()
	
	if request.method=="POST":
		formulario_contacto=FormularioContacto(data=request.POST)
		
		if formulario_contacto.is_valid():
			nombre= request.POST.get("nombreComunica")
			email= request.POST.get("email")
			mensaje= request.POST.get("mensaje")
			
			
			email= EmailMessage("Mensaje de UniNeuroLab Django",
			"El usuario con nombre{} con la direccion {} escribe lo siguiente: \n\n{}".format(nombre,email,mensaje),
			"",["juan.manuel.diaz@unc.edu.ar"],reply_to=[email])
			
			try: 
				email.send()
				
				return redirect("/pccontacto/?valido")
				
			except:
				
				return redirect("/pccontacto/?novalido")
	
	return render(request,"contacto.html", {"miFormulario": formulario_contacto})
	
	'''if request.method== "POST":
		
		miFormulario1=FormularioContacto(data=request.POST)
		
		if  miFormulario1.is_valid():
			
			asunto= request.POST.get("asunto")
			email= request.POST.get("email")
			mensaje= request.POST.get("mensaje")
			
			
			send_mail(infForm['asunto'],infForm['mensaje'],
			infForm.get('email',''),['juan.manuel.diaz@unc.edu.ar'],)
			
			return redirect("/pccontacto/?valido")
			
	else:
		miFormulario1=FormularioContacto()
			
	return render(request, "formulario_contacto.html",{"form":miFormulario1})'''
	




'''def contacto(request):
	
	
	
	if request.method== "POST":
		
		miFormulario1=FormularioContacto(request.POST)
		
		if  miFormulario1.is_valid():
			
			infForm= miFormulario1.cleaned_data
			
			send_mail(infForm['asunto'],infForm['mensaje'],
			infForm.get('email',''),['juan.manuel.diaz@unc.edu.ar'],)
			
			return render(request, "gracias.html")
			
	else:
		miFormulario1=FormularioContacto()
			
	return render(request, "formulario_contacto.html",{"form":miFormulario1})'''
	

