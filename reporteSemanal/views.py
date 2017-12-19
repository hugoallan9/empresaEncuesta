from django.shortcuts import render
from .forms import FormaReporte
# Create your views here.

def hacerReporte(request):
    form = FormaReporte()
    return render(request, 'reporteSemanal/edicion_reporte.html', {'form':form})