import datetime

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View 

from django.contrib.auth.models import User

from .forms import SignForm
from .forms import EditForm

# Create your views here.

@login_required(login_url='accounts:login')
def home(request):
     user=request.user
     return render(request, 'registration/home.html', {'user': user})


class Sign(View): # Đăng kí
     def get(self,request):
          sign_form=SignForm
          return render(request,'registration/sign_form.html', {'sign_form':sign_form})

     def post(self,request): # Yêu cầu đăng kí được gửi
          sg=SignForm(request.POST,request.FILES)
          if sg.is_valid():
               isuser=User.objects.filter(username=sg.cleaned_data['username'])
               if isuser: # Đã tồn tại username
                    sign_form=SignForm
                    messages.error(request,"Tên người dùng đã tồn tại")
                    return render(request,'registration/sign_form.html',{'sign_form':sign_form})
               else: 
                    user=sg.save(commit=False)
                    user.set_password(sg.cleaned_data['password'])
                    user.save()
                    # success_notify='Success'
                    messages.success(request,"Đăng kí thành công thành công ")
                    return redirect('accounts:login')

          # error_notify="Error"
          # sign_form=SignForm
          # messages.error(request,"Lỗi")
          # return render(request,'registration/sign_form.html',{'sign_form': sign_form,'error_notify':error_notify})
          # sign_form=SignForm
          return render(request,'registration/sign_form.html',{'sign_form': sg})


class Edit(LoginRequiredMixin,View): # Chỉnh sửa thông tin người dùng
     login_url = 'accounts:login' # Chưa đăng nhập -> login
     def get(self,resquest):
          form = EditForm(instance=resquest.user)
          return render(resquest, 'registration/edit.html', {'form':form})
     
     def post(self,resquest): # Sửa thông tin
          user=User.objects.get(pk=resquest.user.id)
          user_update= EditForm(resquest.POST,resquest.FILES)
          if user_update.is_valid():
              user.first_name=user_update.cleaned_data['first_name']
              user.last_name=user_update.cleaned_data['last_name']
              user.email=user_update.cleaned_data['email']
              if user_update.cleaned_data['image'] != 'user_default.jpg': # Có update image
               #  return HttpResponse('có image %s'%user_update.cleaned_data['image'] )
                  user.image= user_update.cleaned_data['image'] # *
              user.save()
              messages.success(resquest, 'Edit thành công') 
              return redirect("accounts:home")
          else:
              messages.error(resquest, 'Edit lỗi') 
              return redirect("accounts:edit")


# from django.core.mail import send_mail
# def sent(request):
#      send_mail(
#     'Subject here',
#     'Here is the message.',
#     'from@example.com',
#     ['giangcongnguyenn@gmail.com'],
#     fail_silently=False,
# )