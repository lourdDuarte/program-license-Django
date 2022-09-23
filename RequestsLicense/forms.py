from msilib.schema import CheckBox
from django import forms

class RequestLicenseForm(forms.Form):
    last_name = forms.CharField(max_length=25, required=False)
    first_name = forms.CharField(max_length=25, required=False)
    usufructuado = forms.IntegerField(required=False) #lo que se pide
    date_desde = forms.CharField(max_length=25, required=False)
    date_hasta = forms.CharField(max_length=25, required=False)
    descripcion = forms.CharField(max_length=50, required=False)
   
 