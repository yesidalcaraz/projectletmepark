from django import forms
from .models import EjemploDato

class EjemploDatoForm (forms.ModelForm):
    class Meta:
        model = EjemploDato
        fields = ['nombre', 'longitud', 'latitud', 'direccion']
        labels= {'nombre': 'nombre de la zona', 'longitud':'indique la longitud' ,'latitud': 'Indique la latitud', 'direccion': 'Diga la direccion'}
        
        widgets={
            'nombre': forms.TextInput(
                attrs={'class': 'form-control', 
                'id': 'nombre'
            }
            ),
            'longitud': forms.NumberInput(
                attrs={'class': 'form-control',
                 'id': 'longitud'
                 }),
            'latitud': forms.TextInput(
                attrs={'class':'form-control',
                'id':'latitud',
                'placeholder':'texto para ver'
                }
            ),
            'direccion': forms.TextInput(
                attrs={'class':'form-control',
                'id':'direccion'
                }
            )

        }