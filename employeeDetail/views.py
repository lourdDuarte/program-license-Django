from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from employee.models import Employee
from employeeDetail.models import EmployeeDetail

# Create your views here.
@login_required
def load_data(request):
    employee = Employee.objects.all()
    context = {'employee':employee}

    if request.method == 'POST':
        empleado = request.POST['employee']
        print ("********************"+ empleado + "**************************")
        detail = EmployeeDetail.objects.all().filter(employee=empleado)
        context_detail = {'detail':detail}
        context.update(context_detail) #update context
        
        

    return render (request,'data/data_licenses.html',context)

