from django import forms
from trabajadores.models import Trabajador

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ["nombre", "apellido", "correo", "rut", "tienda", "fecha_ingreso"]
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "apellido": forms.TextInput(attrs={'class': 'form-control'}),
            "correo": forms.EmailInput(attrs={'class': 'form-control'}),
            "rut": forms.TextInput(attrs={'class': 'form-control'}),
            "tienda": forms.TextInput(attrs={'class': 'form-control'}),
            "fecha_ingreso": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }