from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from RequestsLicense.forms import RequestLicenseForm
from RequestsLicense.models import RequestsLicense

# Create your views here.
@login_required
def request_license(request):
    employee = request.user.profile.employee
    if request.method == 'POST':
        form = RequestLicenseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print("formulario"+str(data))
            new_request = RequestsLicense(employee = employee)
            new_request.last_name = data['last_name']
            new_request.fist_name = data['first_name']
            new_request.usufruct = data['usufruct']
            new_request.date_form = data['date_form']
            new_request.date_to = data['date_to']
            new_request.description = data['description']

            new_request.save()

        
    return render (request, 'perfil/empleado/request.html')