import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View

from django.contrib.auth.models import User
from main_app.models import Projects,UserProject,Task
from .forms import TaskForm,ProjectForm,UpdateProject
# Create your views here.


class Home(LoginRequiredMixin,View): # Màn hình người dùng
    login_url='accounts:login'
    
    def get(self,request):
        list_project=request.user.projects_set.all()
        if request.GET: # Yêu cầu sắp xếp *
            if request.GET['project']=='all' and request.GET['status']=='all':
                list_task = Task.objects.filter(user=request.user)
            elif request.GET['project']=='all' and request.GET['status']!='all':
                list_task = Task.objects.filter(user=request.user,status=request.GET['status'])
            elif request.GET['project']!='all' and request.GET['status']=='all':
                list_task = Task.objects.filter(user=request.user,project=request.GET['project'])
            else:
                list_task = Task.objects.filter(user=request.user,project=request.GET['project'],status=request.GET['status'])
            return render(request, 'main_app/home.html', {'list_project':list_project,
                                                        'list_task':list_task})

        # Home 
        list_task = Task.objects.filter(user=request.user)
        return render(request, 'main_app/home.html', {'list_project':list_project,
                                                      'list_task':list_task})
    
    def post(self,request):
        pass

class ViewProject(LoginRequiredMixin,View): # Xem project
    login_url='accounts:login'


    def get(self,request,id):
        list_project=request.user.projects_set.all() # Danh sách project
        project = Projects.objects.get(pk=id) # project
        list_user=project.members.all() # Danh sách thành viên
        list_task=Task.objects.filter(project=project) # danh sách task
        list_user_add=User.objects.exclude(id__in=list_user.values_list('id',flat=True)) # Danh sách user có thể thêm
        list_count=[-1,-1,-1] # Danh sách thống kê trạng thái
        update_project_form=UpdateProject(instance=project)
        for i in range(3):
            list_count[i]=Task.objects.filter(project=project,status=i-1).count()
        # for user in list_user_all:
        #     if
        return render(request,'main_app/project.html',{'project':project,
                                                     'list_user':list_user,
                                                      'list_task':list_task,
                                                      'list_project':list_project,
                                                      'list_count':list_count,
                                                      'update_project_form':update_project_form,
                                                      'list_user_add':list_user_add})
                                                    
class ViewTask(LoginRequiredMixin,View): # xem các task
    login_url='accounts:login'
    
    def get(self,request,id):
        task_form=TaskForm(instance=Task.objects.get(pk=id))
        # task=
        return render(request,'main_app/task.html',{'task_form':task_form})
    
    def post(self,request,id): # chỉnh sửa task
        task_update=TaskForm(request.POST)
        if task_update.is_valid():
            data=task_update.cleaned_data
            task=Task.objects.filter(pk=id).update(name=data['name'],
                                                               project=data['project'],
                                                               user=data['user'],
                                                               describe=data['describe'],
                                                               status=data['status'],
                                                               dateline=data['dateline'],
                                                               start=data['start'],
                                                               end=data['end'],
                                                               note=data['note'])
            return redirect('main_app:home')
            
        return redirect('main_app:home')




class AddProject(LoginRequiredMixin,View): #Tạo dự án mới
    login_url='accounts:login'
    
    def get(self,request):
        projetc_form=ProjectForm
        return render(request,'main_app/add_project.html',{'form': projetc_form})
    
    def post(self,request):
        project=ProjectForm(request.POST)
        if project.is_valid():
            pr=Projects(name=project.cleaned_data['name'],
                        describe=project.cleaned_data['describe'],
                        note=project.cleaned_data['note'])
            pr.save()
            UserProject.objects.create(project=pr,user=request.user)
            return redirect('/projects/%s'%(pr.id))
        return render(request,'main_app:add_project')
        

class AddTask(LoginRequiredMixin,View): #Tạo task mới
    login_url='accounts:login'
    
    def get(self,request):
        add_task=TaskForm
        return render(request,'main_app/add_task.html',{'form': add_task})
    
    def post(self,request):
        task=TaskForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('main_app:home')


def demo(request):
    return render(request,'demo.html')