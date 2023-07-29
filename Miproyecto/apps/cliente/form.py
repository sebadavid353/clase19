from django import forms

from .models import cliente, pais

class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['nombre', 'apellido', 'nacimiento', 'pais_origen_id']
        
class paisform(forms.ModelForm):
    class Meta:
        model = pais
        fields = '__all__'