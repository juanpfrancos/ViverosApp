# productores/forms.py
from django import forms
from .models import Productor

class ProductorForm(forms.ModelForm):
    class Meta:
        model = Productor
        fields = ['documento_identidad', 'nombre', 'apellido', 'telefono', 'correo']
