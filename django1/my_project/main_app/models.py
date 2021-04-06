import datetime
from django.utils import timezone
from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model): # Dự án 
    name=models.CharField(max_length=50) 
    describe=models.TextField(blank=True,null=True) 
    members=models.ManyToManyField(User,through='UserProject') # Quan hệ n-n với user,và lưu trữ thông tin thêm ở UserProject
    list_status = (
        (-1, "Doing"),
        (0, 'NotDo'),
        (1, 'Done'),
    )
    status=models.IntegerField(default=0,choices=list_status)
    note=models.TextField(blank=True,null=True)
    create_at=models.DateTimeField(auto_now_add=True,editable=False) 
    update_at=models.DateTimeField(auto_now=True,editable=False) 
    
    class Meta:
        ordering=['status', 'create_at']

    def __str__(self):
        return str(self.id)+'_'+self.name


class UserProject(models.Model): # Liên kết dự án và user
    project=models.ForeignKey(Projects,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_joined=models.DateTimeField(default=timezone.now,editable=False)
    

class Task(models.Model): # Các công việc 
    name=models.CharField(max_length=200)
    project=models.ForeignKey(Projects,on_delete=models.CASCADE) 
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    describe=models.TextField(blank=True,null=True)
    list_status = (
        (-1, "Doing"),
        (0, 'NotDo'),
        (1, 'Done'),
    )
    status=models.IntegerField(default=0,choices=list_status)
    start=models.DateTimeField(blank=True,null=True)
    end=models.DateTimeField(blank=True,null=True)
    deadline=models.DateTimeField(blank=True,null=True)
    note=models.TextField(blank=True,null=True)
    create_at=models.DateTimeField(default=timezone.now,editable=False)
    update_at=models.DateTimeField(auto_now=True,editable=False)
    update_by=models.CharField(max_length=30,default=None,blank=True,null=True,editable=False)
    is_view=models.BooleanField(default=False)
    
    class Meta:
        ordering=["status",'-create_at','project']

    def __str__(self):
        return str(self.id)+'_'+self.namepy 


class UserSetting(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    home_project=models.CharField(max_length=10,default='all')
    home_status=models.CharField(max_length=10 ,default='all')
    project_user=models.CharField(max_length=10,default='all')
    project_status=models.CharField(max_length=10,default='all')

