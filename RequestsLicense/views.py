from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from RequestsLicense.forms import RequestLicenseForm
from RequestsLicense.models import RequestsLicense

import smtplib

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

            # new_request.save()
            
            last_name = data['last_name']
            first_name = data['first_name']

            # mail notice
            m = ("La persona: "+ last_name + "," + first_name + " acaba de enviar una nueva solicitud " +
            "de licencia, ingresar al sistema para confirmarlo. ")


            message = str(m)
            destino = 'lourdes123duarte@gmail.com'

            SUBJECT = "Nueva solicitud de licencia"
            TEXT = message

            text = "Subject: {}\n\n{}".format(SUBJECT, TEXT)

            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login('mail.diplomatura@gmail.com','piucomltoimebgdw')

                # Enviamos el mensaje
            smtpserver.sendmail('mail.licenses@gmail.com', destino, text)
                # Cerramos la conexion
            smtpserver.close()
        
    return render (request, 'perfil/empleado/request.html')