from django import forms
from .models import Airplane

class AirplaneForm(forms.ModelForm):
    class Meta:
        model = Airplane
        fields = ['name', 'capacity', 'rows', 'columns', 'state']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'rows': forms.NumberInput(attrs={'class': 'form-control'}),
            'columns': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'})
        }

