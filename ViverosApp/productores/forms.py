# productores/forms.py
from django import forms
from .models import Finca, Vivero, Labor,ProductoControl, ProductoControlHongo, ProductoControlPlaga, ProductoControlFertilizante
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



class ProductoControlForm(forms.ModelForm):
    class Meta:
        model = ProductoControl
        fields = ['registro_ica', 'nombre', 'frecuencia_aplicacion', 'valor', 'tipo']

class ProductoControlHongoForm(forms.ModelForm):
    class Meta:
        model = ProductoControlHongo
        fields = ['producto', 'periodo_carencia', 'hongo_afectado']

class ProductoControlPlagaForm(forms.ModelForm):
    class Meta:
        model = ProductoControlPlaga
        fields = ['producto', 'periodo_carencia']

class ProductoControlFertilizanteForm(forms.ModelForm):
    class Meta:
        model = ProductoControlFertilizante
        fields = ['producto', 'fecha_ultima_aplicacion']
