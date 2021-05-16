from django.db import models
from safedelete.config import HARD_DELETE_NOCASCADE, SOFT_DELETE
# from safedelete.config import HARD_DELETE
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE,HARD_DELETE
from safedelete import config

# Create your models here.
class School(SafeDeleteModel,models.Model):
    _safedelete_policy = HARD_DELETE
    _safedelete_visibility = config.DELETED_VISIBLE_BY_FIELD
    name=models.CharField(max_length=100)
    describe=models.CharField(max_length=100)

    def __str__(self):
        return ('%s_%s'%(self.name,self.id))

class Class(SafeDeleteModel,models.Model):
    _safedelete_visibility = config.DELETED_VISIBLE_BY_FIELD
    _safedelete_policy = HARD_DELETE_NOCASCADE
    school=models.ForeignKey(School, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    describe=models.CharField(max_length=100)


    def __str__(self):
        return ('%s_%s'%(self.name,self.id))

class Student(SafeDeleteModel,models.Model):
    _safedelete_policy = HARD_DELETE
    student_class=models.ForeignKey(Class, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    describe=models.CharField(max_length=100)

    def __str__(self):
        return ('%s_%s'%(self.name,self.id))
