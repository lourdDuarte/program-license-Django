from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from profile.forms import ProfileForm
from employee.models import Employee
from employeeDetail.models import EmployeeDetail
from django.db.models import Count


# Create your views here.
@login_required
def dashboard_view(request):
    employee = request.user.profile.employee
    detail = EmployeeDetail.objects.all().filter(employee=employee).order_by('year')
    

    context = {'detail':detail}

    return render (request,'perfil/empleado/dashboard.html',context)

  
    
@login_required
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST)
    
        if form.is_valid():
            data = form.cleaned_data
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.username = data['username']
            user.email = data['email']
            user.save()
            return redirect('update_profile')
    else:
        form = ProfileForm()
        
    return render(
        request=request,
        template_name='perfil/empleado/profile.html',
        context={
            'profile': user,
            'user': request.user,
            'form': form
        }
    )



    
