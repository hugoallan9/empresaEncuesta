from django import forms

from .models import Reporte

class FormaReporte(forms.ModelForm):


    class Meta:
        model = Reporte
        fields = (
            'inicio_semana', 
            'producto1', 
            'producto2', 
            'producto3',
        ) 