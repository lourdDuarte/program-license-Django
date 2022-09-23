from django.db import models
import employee
from employee.models import Employee
# Create your models here.

# Create your models here.
class RequestsLicense(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=25)
    fist_name = models.CharField(max_length=25)
    usufruct = models.CharField(max_length=25) #lo que se pide
    date_form = models.DateField(auto_now=False)
    date_to = models.DateField(auto_now=False)
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=False)



