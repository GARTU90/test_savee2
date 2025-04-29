from django import forms
from .models import RespuestaMedica

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = RespuestaMedica
        fields = ['seguro', 'problema']
