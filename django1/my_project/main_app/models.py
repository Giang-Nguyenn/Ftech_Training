import datetime
from django.utils import timezone
from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model): # Dự án 
    name=models.CharField(max_length=50) # Tên dự án
    describe=models.TextField(blank=True,null=True) # Miêu tả dự án
    members=models.ManyToManyField(User,through='UserProject') # Quan hệ n-n với user,và lưu trữ thông tin thêm ở UserProject
    list_status = (
        (-1, "Doing"),
        (0, 'NotDo'),
        (1, 'Done'),
    )
    status=models.IntegerField(default=0,choices=list_status) # trạng thái -1(đang thực hiện),0(chưa thực hiện),1(đã hoàn thành)
    note=models.TextField(blank=True,null=True) # Ghi chú
    create_at=models.DateTimeField(auto_now_add=True,editable=False) # Ngày tạo
    update_at=models.DateTimeField(auto_now=True,editable=False) # Ngày cập nhật mới nhất
    
    class Meta:
        ordering=['status','create_at']

    def __str__(self):
        return str(self.id)+'_'+self.name


class UserProject(models.Model): # Liên kết dự án và user
    project=models.ForeignKey(Projects,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_joined=models.DateTimeField(default=timezone.now,editable=False) # Ngày vào 
    

class Task(models.Model): # Các công việc 
    name=models.CharField(max_length=200) # Tên task
    project=models.ForeignKey(Projects,on_delete=models.CASCADE) # Thuộc dự án nào
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True) # Do ai đảm nhiệm
    describe=models.TextField(blank=True,null=True) # Miêu tả
    list_status = (
        (-1, "Doing"),
        (0, 'NotDo'),
        (1, 'Done'),
    )
    status=models.IntegerField(default=0,choices=list_status) # Trạng thái -1(đang thực hiện),0(chưa thực hiện),1(đã hoàn thành)
    start=models.DateTimeField(blank=True,null=True) # Ngày bắt đầu
    end=models.DateTimeField(blank=True,null=True) # Ngày kết thúc
    deadline=models.DateTimeField(blank=True,null=True) # Hạn hoàn thành
    note=models.TextField(blank=True,null=True) # Ghi chú thêm
    create_at=models.DateTimeField(default=timezone.now,editable=False) # Ngày tạo
    update_at=models.DateTimeField(auto_now=True,editable=False) # Ngày cập nhật mới nhất
    
    class Meta:
        ordering=["status",'project']

    def __str__(self):
        return str(self.id)+'_'+self.name


class UserSetting(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    home_project=models.CharField(max_length=10,default='all')
    home_status=models.CharField(max_length=10 ,default='all')
    project_user=models.CharField(max_length=10,default='all')
    project_status=models.CharField(max_length=10,default='all')

