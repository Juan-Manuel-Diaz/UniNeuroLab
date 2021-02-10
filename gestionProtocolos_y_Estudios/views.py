# ESTE ES EL VIEWS DE gestionPROTOCOLOS Y ESTUDIO
from django.shortcuts import render

# Create your views here.

def verProtocolos(request):
	
	return render(request, "verProtocolos.html")
