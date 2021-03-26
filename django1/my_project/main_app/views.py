import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
# Create your views here.


@login_required(login_url='accounts:login')
def home(request):
    user = request.user
    return render(request, 'main_app/home.html', {'user': user})
