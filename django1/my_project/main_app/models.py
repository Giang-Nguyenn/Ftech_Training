import datetime
from django.utils import timezone
from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model): # Dự án 
    name=models.CharField(max_length=50) # Tên dự án
    describe=models.TextField(blank=True) # Miêu tả dự án
    members=models.ManyToManyField(User,through='UserProject') # Quan hệ n-n với user,và lưu trữ thông tin thêm ở UserProject
    counts=models.IntegerField(default=0,editable=False) # Số người tham gia
    status=models.IntegerField(default=0) # trạng thái -1(đang thực hiện),0(chưa thực hiện),1(đã hoàn thành)
    create_time=models.DateTimeField(default=timezone.now,editable=False) # Ngày tạo
    note=models.TextField(blank=True) # Ghi chú
    
    class Meta:
        ordering=['status','create_time']

    def __str__(self):
        return str(self.id)+'_'+self.name


class UserProject(models.Model): # Liên kết dự án và user
    project=models.ForeignKey(Projects,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_joined=models.DateTimeField(default=timezone.now,editable=False) # Ngày vào 
    

class Task(models.Model): # Các công việc 
    name=models.CharField(max_length=200) # Tên task
    project=models.ForeignKey(Projects,on_delete=models.CASCADE) # Thuộc dự án nào
    user=models.ForeignKey(User,on_delete=models.CASCADE) # Do ai đảm nhiệm
    describe=models.TextField(blank=True) # Miêu tả
    status=models.IntegerField(default=0) # Trạng thái -1(đang thực hiện),0(chưa thực hiện),1(đã hoàn thành)
    create_time=models.DateTimeField(default=timezone.now,editable=False) # Ngày tạo
    start=models.DateTimeField(blank=True,null=True) # Ngày bắt đầu
    end=models.DateTimeField(blank=True,null=True) # Ngày kết thúc
    dateline=models.DateTimeField(blank=True,null=True) # Hạn hoàn thành
    note=models.TextField(blank=True) # Ghi chú thêm
    
    class Meta:
        ordering=["status",'create_time']

    def __str__(self):
        return str(self.id)+'_'+self.name

