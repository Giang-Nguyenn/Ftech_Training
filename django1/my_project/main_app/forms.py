from django import forms
import re

from django.contrib.auth.models import User
from .models import Projects,Task



class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','project','user','describe','status','start','end','dateline','note']

class ProjectForm(forms.Form):
    name=forms.CharField(max_length=50) 
    describe=forms.CharField(widget=forms.Textarea(attrs={'class': 'text_input1','cols':'40','rows':'5'})) 
    note=forms.CharField()

class UpdateProject(forms.ModelForm):
    class Meta:
        model=Projects
        fields='__all__'
