from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def load_data(request):
    return render (request,'data/data_licenses.html')