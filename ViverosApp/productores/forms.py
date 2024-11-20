# productores/forms.py
from django import forms
from .models import Finca, Vivero, Labor

class FincaForm(forms.ModelForm):
    class Meta:
        model = Finca
        fields = ['numero_catastro', 'municipio', 'productor']

class ViveroForm(forms.ModelForm):
    class Meta:
        model = Vivero
        fields = ['codigo', 'tipo_cultivo', 'finca']


class LaborForm(forms.ModelForm):
    class Meta:
        model = Labor
        fields = ['fecha', 'descripcion', 'vivero']
