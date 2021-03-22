from django.shortcuts import render
import datetime
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='accounts:login')
def home(request):
     user=request.user
     return render(request, 'registration/home.html', {'user': user})