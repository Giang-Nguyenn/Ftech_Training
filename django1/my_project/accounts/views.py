from django.shortcuts import render,redirect
import datetime
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import SignForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

@login_required(login_url='accounts:login')
def home(request):
     user=request.user
     return render(request, 'registration/home.html', {'user': user})


class Sign(View): # Đăng kí
     def get(self,request):
          sign_form=SignForm
          return render(request,'registration/sign_form.html',{'sign_form':sign_form})

     def post(self,request): # Yêu cầu đăng kí được gửi
          sg=SignForm(request.POST)
          if sg.is_valid():
               isuser=User.objects.filter(username=sg.cleaned_data['username'])
               if isuser:
                    sign_form=SignForm
                    return render(request,'registration/sign_form.html',{'sign_form':sign_form})
               else: 
                    user=sg.save(commit=False)
                    user.set_password(sg.cleaned_data['password'])
                    user.save()
                    # success_notify='Success'
                    messages.success(request,"Thành công ")
                    return redirect('accounts:login')
          error_notify="Error"
          sign_form=SignForm
          messages.error(request,"Lỗi")
          return render(request,'registration/sign_form.html',{'sign_form': sign_form,'error_notify':error_notify})