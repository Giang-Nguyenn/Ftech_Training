from django.db import models

import datetime
from django.utils import timezone

from django.contrib.auth.models import AbstractUser,UserManager

from safedelete.models import SafeDeleteModel
from safedelete import config

# from django.contrib.auth.management.commands import createsuperuser


# Create your models here.

class Tenant(SafeDeleteModel,models.Model):
    _safedelete_policy=config.SOFT_DELETE_CASCADE
    name = models.CharField(max_length=100)
    subdomain_prefix = models.CharField(max_length=100, unique=True)
    # note=models.CharField(max_length=100,blank=True)
    def __str__(self):
        return str(self.name)+"_"+str(self.id)

class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE,default=1)

    class Meta:
        abstract = True

class User(TenantAwareModel,SafeDeleteModel,AbstractUser):
    _safedelete_policy=config.SOFT_DELETE_CASCADE
    objects = UserManager()
    supper_admin=models.BooleanField(default=False)


    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('supper_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        tenant=Tenant.objects.filter(name='admin') # ?

        return self._create_user(username, email, password, tenant , **extra_fields)
    
    class Meta(AbstractUser.Meta):
        db_table = 'auth_user'


class Projects(SafeDeleteModel,TenantAwareModel):  # Dự án
    _safedelete_policy=config.SOFT_DELETE_CASCADE

    name = models.CharField(max_length=50)
    describe = models.TextField(blank=True, null=True)
    # Quan hệ n-n với user,và lưu trữ thông tin thêm ở UserProject
    members = models.ManyToManyField(User, through='UserProject')
    list_status = (
        (-1, "Doing"),
        (0, 'NotDo'),
        (1, 'Done'),
    )
    status = models.IntegerField(default=0, choices=list_status)
    note = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ['status', 'create_at']

    def __str__(self):
        return str(self.name)+"_"+str(self.id)


class UserProject(SafeDeleteModel,TenantAwareModel):  # Liên kết dự án và user
    _safedelete_policy=config.SOFT_DELETE_CASCADE

    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)


class Task(SafeDeleteModel,TenantAwareModel):  # Các công việc
    _safedelete_policy=config.SOFT_DELETE_CASCADE

    name = models.CharField(max_length=200)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    describe = models.TextField(blank=True, null=True)
    list_status = (
        (-1, "Doing"),
        (0, 'NotDo'),
        (1, 'Done'),
    )
    status = models.IntegerField(default=0, choices=list_status)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(default=timezone.now, editable=False)
    update_at = models.DateTimeField(auto_now=True, editable=False)
    update_by = models.CharField(
        max_length=30, default=None, blank=True, null=True, editable=False)
    is_view = models.BooleanField(default=False)

    class Meta:
        ordering = ["status", '-create_at', 'project']

    def __str__(self):
        return str(self.id)+'_'+self.name