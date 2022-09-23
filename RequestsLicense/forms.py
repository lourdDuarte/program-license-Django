from msilib.schema import CheckBox
from django import forms

class RequestLicenseForm(forms.Form):
    last_name = forms.CharField(max_length=25, required=False)
    first_name = forms.CharField(max_length=25, required=False)
    usufruct = forms.CharField(max_length=25, required=False) #lo que se pide
    date_form  = forms.CharField(max_length=25, required=False)
    date_to = forms.CharField(max_length=25, required=False)
    description = forms.CharField(max_length=50, required=False)
   
 