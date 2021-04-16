from django.db import models

# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100) 

class Student(models.Model):
    name=models.CharField(max_length=50)
    birth_day=models.DateField(blank=True,null=True)
    phone=models.CharField(max_length=12,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    school=models.ForeignKey(School,on_delete=models.CASCADE,default=1,related_name='students')



