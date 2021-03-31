import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.models import User
from main_app.models import Projects,UserProject,Task,UserSetting
from .forms import TaskForm,ProjectForm,UpdateProject,TaskFormAdd,TaskFormUpdate,TaskFormAdd1
# Create your views here.


class Home(LoginRequiredMixin,View): # Màn hình người dùng
    login_url='accounts:login'
    
    def get(self,request):
        if request.GET.get('seach'): # Có yêu cầu tìm kiếm
            # if request.GET['keyword'] !='':
            #     list_task=Task.objects.filter(name__icontains=request.GET['keyword'])
            # else:
            #     list_task=Task.objects.filter(name__icontains=request.GET['keyword'])
            choice_project=request.GET['project']
            choice_status=request.GET['status']
            choice_keyword=request.GET['keyword']
            if choice_project=='all' and choice_status=='all':
                list_task=Task.objects.filter(user=request.user)
            elif choice_project!='all' and choice_status=='all':
                list_task=Task.objects.filter(user=request.user,project=choice_project)
            elif choice_project=='all' and choice_status!='all':
                list_task=Task.objects.filter(user=request.user,status=choice_status)
            else :
                list_task=Task.objects.filter(user=request.user,project=choice_project,status=choice_status)
            if request.GET['keyword']!='': # Có keyword tìm kiếm được gửi 
                list_task=list_task.filter(name__icontains=request.GET['keyword'])

            # Convert choice_project về int nếu nó khác 'all'
            if choice_project!='all': #...
                choice_project=int(choice_project)
        else: # không có yêu cầu tìm kiếm được gửi
            list_task=Task.objects.filter(user=request.user)
            choice_project='all'
            choice_status='all'
            choice_keyword=''

        # Phân trang
        paginator = Paginator(list_task, 5)
        pageNumber = request.GET.get('page')
        try:
            l_task = paginator.page(pageNumber)
        except PageNotAnInteger:
            l_task = paginator.page(1)
        except EmptyPage:
            l_task = paginator.page(paginator.num_pages)

        list_project=request.user.projects_set.all()
        return render(request, 'main_app/home.html', {'list_project':list_project,
                                                      'list_task':l_task,
                                                      'choice_project':choice_project,
                                                      'choice_status':choice_status,
                                                      'choice_keyword':choice_keyword
                                                      })
        # if request.GET.get('Sort'): # Yêu cầu sắp xếp *
        #     usersetting=UserSetting.objects.filter(user=request.user)
        #     if usersetting: # nếu có thì cập nhật
        #         usersetting.update(home_project=request.GET['project'],
        #                            home_status=request.GET['status']
        #                            )
        #     else : # Chưa có thì tạo mới
        #         UserSetting.objects.create(user=request.user,home_project=request.GET['project'],
        #                            home_status=request.GET['status']
        #                             )
        # if not UserSetting.objects.filter(user=request.user):
        #     UserSetting.objects.create(user=request.user)
        # choice_project=UserSetting.objects.get(user=request.user).home_project
        # choice_status=UserSetting.objects.get(user=request.user).home_status
        # # lấy list_task
        # if choice_project=='all' and choice_status=='all':
        #     list_task = Task.objects.filter(user=request.user)
        # elif choice_project=='all' and choice_status!='all':
        #     list_task = Task.objects.filter(user=request.user,status=choice_status)
        # elif choice_project!='all' and choice_status=='all':
        #     list_task = Task.objects.filter(user=request.user,project=choice_project)
        # else:
        #     list_task = Task.objects.filter(user=request.user,project=choice_project,status=choice_status)
        # # Phân trang
        # paginator = Paginator(list_task, 15)
        # pageNumber = request.GET.get('page')
        # try:
        #     l_task = paginator.page(pageNumber)
        # except PageNotAnInteger:
        #     l_task = paginator.page(1)
        # except EmptyPage:
        #     l_task = paginator.page(paginator.num_pages)
            
        # if choice_project!='all': #...
        #     choice_project=int(choice_project) 
        # return render(request, 'main_app/home.html', {'list_project':list_project,
        #                                             'list_task':l_task,
        #                                             'choice_project':choice_project,
        #                                             'choice_status':choice_status})

            # if request.GET['project']=='all' and request.GET['status']=='all':
            #     list_task = Task.objects.filter(user=request.user)
            # elif request.GET['project']=='all' and request.GET['status']!='all':
            #     list_task = Task.objects.filter(user=request.user,status=request.GET['status'])
            # elif request.GET['project']!='all' and request.GET['status']=='all':
            #     list_task = Task.objects.filter(user=request.user,project=request.GET['project'])
            # else:
            #     list_task = Task.objects.filter(user=request.user,project=request.GET['project'],status=request.GET['status'])
            # if request.GET['project']=='all': #...
            #     choice_project=request.GET['project']
            # else:
            #     choice_project=int(request.GET['project']) 
            # choice_status=request.GET['status']
            # paginator = Paginator(list_task, 5)
            # pageNumber = request.GET.get('page')
            # try:
            #     task = paginator.page(pageNumber)
            # except PageNotAnInteger:
            #     task = paginator.page(1)
            # except EmptyPage:
            #     task = paginator.page(paginator.num_pages)
            # return render(request, 'main_app/home.html', {'list_project':list_project,
            #                                               'list_task':task,# list_task
            #                                               'choice_project':choice_project,
            #                                               'choice_status':choice_status})

        # Home 
        # list_task = Task.objects.filter(user=request.user)
        # Thêm
        # paginator = Paginator(list_task, 5)
        # pageNumber = request.GET.get('page')
        # try:
        #     task = paginator.page(pageNumber)
        # except PageNotAnInteger:
        #     task = paginator.page(1)
        # except EmptyPage:
        #     task = paginator.page(paginator.num_pages)
        #hết
        # return render(request, 'main_app/home.html', {'list_project':list_project,
        #                                               'list_task':list_task}) #list_task
    

    def post(self,request):
        pass


class ViewProject(LoginRequiredMixin,View): # Trang xem project
    login_url='accounts:login'

    def get(self,request,id):
        project = Projects.objects.get(pk=id) # project
        if request.GET.get('seach'): # Có yêu cầu tìm kiếm
            choice_user=request.GET['user']
            choice_status=request.GET['status']
            choice_keyword=request.GET['keyword']
            if choice_user=='all' and choice_status=='all':
                list_task=Task.objects.filter(project=project)
            elif choice_user!='all' and choice_status=='all':
                list_task=Task.objects.filter(project=project,user=choice_user)
            elif choice_user=='all' and choice_status!='all':
                list_task=Task.objects.filter(project=project,status=choice_status)
            else :
                list_task=Task.objects.filter(project=project,user=choice_user,status=choice_status)
            if request.GET['keyword']!='': # Có keyword tìm kiếm được gửi 
                list_task=list_task.filter(name__icontains=request.GET['keyword'])

            # Convert choice_project về int nếu nó khác 'all'
            if choice_user!='all': #...
                choice_user=int(choice_user)
        else: # Không có yêu cầu tìm kiếm được gửi
            list_task=Task.objects.filter(project=project)
            choice_user='all'
            choice_status='all'
            choice_keyword=''

        # Phân trang
        paginator = Paginator(list_task, 5)
        pageNumber = request.GET.get('page')
        try:
            l_task = paginator.page(pageNumber)
        except PageNotAnInteger:
            l_task = paginator.page(1)
        except EmptyPage:
            l_task = paginator.page(paginator.num_pages)

        list_project=request.user.projects_set.all() # Danh sách project
        list_user=project.members.all() # Danh sách thành viên
        list_user_add=User.objects.exclude(id__in=list_user.values_list('id',flat=True)) # Danh sách user có thể thêm
        list_count=[-1,-1,-1] # Danh sách thống kê trạng thái
        update_project_form=UpdateProject(instance=project)
        for i in range(3): # list thống kê 
            list_count[i]=Task.objects.filter(project=project,status=i-1).count()

        return render(request,'main_app/project.html',{'project':project,
                                                      'list_user':list_user,
                                                      'list_task':l_task,
                                                      'list_project':list_project,
                                                      'list_count':list_count,
                                                      'update_project_form':update_project_form,
                                                      'list_user_add':list_user_add,
                                                      'choice_user':choice_user,
                                                      'choice_status':choice_status,
                                                      'choice_keyword':choice_keyword
                                                      })


    def post(self,request,id):
        # project: Thêm ,xoá thành viên
        if request.POST.get('add_user') is not None: # Thêm thành viên
            list_user=request.POST.getlist('add_user')
            pr=Projects.objects.get(pk=id)
            for user in list_user:
                UserProject.objects.create(project=pr,user=User.objects.get(pk=user))
            messages.success(request,'Thêm thành công ')
            return redirect('/projects/%s'%id)

        if request.POST.get('delete_user') is not None: # Xoá thành viên
            list_user=request.POST.getlist('delete_user')
            pr=Projects.objects.get(pk=id)
            # for user in list_user:
            UserProject.objects.filter(project=pr,user__id__in=list_user).delete()
            return redirect('/projects/%s'%id)

        redirect('/home')


class TaskCRUD(LoginRequiredMixin,View): # xem các task
    login_url='accounts:login'
    
    def get(self,request,id):
        if 'update_task' in request.path:
            task_form=TaskForm(instance=Task.objects.get(pk=id),project_id=Task.objects.get(pk=id).project.id) #*
            # task=
            return render(request,'main_app/update_task.html',{'task_form':task_form})
        
        if 'add_task' in request.path:
            task_form=TaskFormAdd(project_id=id) 
            # task_form=TaskFormAdd
            return render(request,'main_app/add_task.html',{'task_form':task_form})
    
    def post(self,request,id): # POST,id là id của task
        if request.POST.get('UpdateTask') is not None: # update task
            task_update=TaskFormUpdate(request.POST,project_id=Task.objects.get(pk=id).project.id)
            if task_update.is_valid():
                data=task_update.cleaned_data
                task=Task.objects.filter(pk=id).update(name=data['name'],
                                                               project=data['project'],
                                                               user=data['user'],
                                                               describe=data['describe'],
                                                               status=data['status'],
                                                               deadline=data['deadline'],
                                                               start=data['start'],
                                                               end=data['end'],
                                                               note=data['note'])
                pr_id=Task.objects.get(pk=id).project.id
                messages.success(request,'Update thành công')
                return redirect('/projects/%s'%pr_id)
            messages.error(request,'Update không thành công')
            return render(request,'main_app/update_task.html',{'task_form':task_update})
        
        if request.POST.get('AddTask') is not None: # add task,id là id project
            task_add=TaskFormAdd(request.POST,project_id=id)
            if task_add.is_valid():
                task_add.save()
                messages.success(request,'Thêm task thành công')
                return redirect('/projects/%s'%id)
            messages.error(request,'Error')
            return render(request,'main_app/add_task.html',{'task_form':task_add})
        
        if request.POST.get('DelTask') is not None: # delete task,id là id task
            pr_id=Task.objects.get(pk=id).project.id
            Task.objects.filter(pk=id).delete()
            messages.success(request,"Xoá thành công task")
            return redirect('/projects/%s'%pr_id)

        return HttpResponse('okkk')
                                                    
class ViewTask(LoginRequiredMixin,View): # xem các task
    login_url='accounts:login'
    
    def get(self,request,id):
        task_form=TaskForm(instance=Task.objects.get(pk=id))
        return render(request,'main_app/task.html',{'task_form':task_form})


class ProjectCRUD(LoginRequiredMixin,View): #thêm sửa xoá cập nhật dự án mới
    login_url='accounts:login'
    
    def get(self,request):
        if 'add_project' in request.path: # Form add Project
            projetc_form=ProjectForm
            return render(request,'main_app/add_project.html',{'form': projetc_form})
        
        if 'update_project' in request.path: # Form Update project
            return HttpResponse('update')
        
        if 'del_project' in request.path: # xoá projetc
            return HttpResponse('del')

        return redirect('/home')
    
    def post(self,request):
        if request.POST.get('AddProject') is not None: # Thêm project
            project=ProjectForm(request.POST)
            if project.is_valid():
                pr=Projects(name=project.cleaned_data['name'],
                            describe=project.cleaned_data['describe'],
                            note=project.cleaned_data['note'])
                pr.save()
                UserProject.objects.create(project=pr,user=request.user)
                messages.success(request,'Thêm thành công projetc')
                return redirect('/projects/%s'%(pr.id))
            messages.error(request,'Error')
            return render(request,'main_app/add_project.html',{'form': project})
        
        if request.POST.get('UpdateProject') is not None: # Sửa project
            form_update=ProjectForm(request.POST)
            a=request.POST['project_id']
            if form_update.is_valid():
                Projects.objects.filter(pk=a).update(name=form_update.cleaned_data['name'],
                                                                        describe=form_update.cleaned_data['describe'],
                                                                        note=form_update.cleaned_data['note'],
                                                                        )
                messages.success(request,'Update thành công project')
                return redirect('/projects/%s'%a)
            messages.error(request,'Error')
            return redirect('/projects/%s'%a)
        return HttpResponse('123')
        

class UpdateUserProject(LoginRequiredMixin,View):
    login_url='accounts:login'
    def post(self,request,id):
        if request.POST.get('ProjectAddUser'):
            list_user=request.POST.getlist('add_user')
            pr=Projects.objects.get(pk=id)
            for user in list_user:
                UserProject.objects.create(project=pr,user=User.objects.get(pk=user))
            messages.success(request,'Thêm thành công')
            return redirect('/projects/%s'%id)
            # return HttpResponse('%s'%list_user)

        if request.POST.get('ProjectDelUser'): 
            '''
            Xoá user khỏi project
            Các task chưa làm và đang làm sẽ đưa về trạng thái chưa làm,và chưa có người làm
            '''
            list_user=request.POST.getlist('delete_user')
            pr=Projects.objects.get(pk=id)
            for user_id in list_user:
                Task.objects.filter(project=pr,user=User.objects.get(pk=user_id)).exclude(status=1).update(status=0,
                                                                                                           user=None,
                                                                                                            )
                UserProject.objects.filter(project=pr,user=User.objects.get(pk=user_id)).delete()
            messages.success(request,'Xoá thành công')
            return redirect('/projects/%s'%id)

            # return HttpResponse('deluser%s'%(list_user))
        return HttpResponse('123')




def demo(request):
    messages.warning(request,'Success ok')
    return render(request,'demo.html')