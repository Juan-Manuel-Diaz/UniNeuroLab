# ESTE ES EL VIEWS DE PROCESAMIENTO DE DATOS
from django.shortcuts import render

# Create your views here.



def pd_neuroimagenes(request):
	
	return render(request, "pdNEUROIMAGENES.html")


def pd_eeg(request):
	
	return render(request, "pdEEG.html")

