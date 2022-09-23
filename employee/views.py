from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profile.forms import ProfileForm

# Create your views here.
@login_required
def dashboard_view(request):
    return render(request, 'perfil/empleado/dashboard.html')


    
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
    
