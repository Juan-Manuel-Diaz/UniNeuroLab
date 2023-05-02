# ESTE ES EL VIEWS DE RESULTADOS PROTOCOLO
from django.shortcuts import render

# Create your views here.


def resultadosProtocolo(request):
	
	return render(request, "resultadosProtocolo.html")
