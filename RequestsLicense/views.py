from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from RequestsLicense.forms import RequestLicenseForm
from RequestsLicense.models import RequestsLicense

# Create your views here.
@login_required
def request_license(request):
    req = request.user.perfil
    if request.method == 'POST':
        form = RequestLicenseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print("formulario"+str(data))
            new_request = RequestsLicense()
            new_request.empleado = req
            new_request.nombre = data['last_name']
            new_request.apellido = data['first_name']
            new_request.usufructuados = data['usufructuado']
            new_request.fecha_desde = data['date_desde']
            new_request.fecha_hasta = data['date_hasta'] 
            new_request.descripcion = data['descripcion']
            new_request.save()

        
    return render (request, 'perfil/empleado/request.html')