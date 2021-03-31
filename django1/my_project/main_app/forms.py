from django import forms
import re
import datetime 

from django.contrib.auth.models import User
from .models import Projects,Task,UserProject

from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

import pytz

utc=pytz.UTC


class TaskForm(forms.ModelForm): # Form hiển Add,Update Task,truyền vào projetc_id(để lấy lấy chose project và list user thuộc project đó) 
    start =forms.DateField(widget=forms.DateInput(attrs={'class':'timepicker'}))
    end =forms.DateField(widget=DateInput(),required=False)
    deadline =forms.DateField(widget=DateInput(),required=False)
    class Meta:
        model=Task
        fields=['name','project','user','describe','status','start','end','deadline','note']

    def __init__(self,*args,project_id,**kwargs): # Thêm tham số project_id,chú ý vị trí của projetc_id
          # call standard __init__
        super().__init__(*args,**kwargs)
          #extend __init__
        self.fields['project'] =forms.ModelChoiceField(queryset=Projects.objects.filter(pk=project_id))
        self.fields['user'] =forms.ModelChoiceField(queryset=Projects.objects.get(pk=project_id).members.all())
    
    def clean_project(self): # Kiểm tra id project có tồn tại không
        if self.cleaned_data['project']:
            if Projects.objects.get(pk=self.cleaned_data['project'].id):
                return self.cleaned_data['project']
        return forms.ValidationError('Không tồn tại id project')

    def clean_user(self): # Kiểm tra user gửi lên có thuộc Project
        if self.cleaned_data['user']:
            if User.objects.get(pk=self.cleaned_data['user'].id) or (self.cleaned_data['user']==''):
                return self.cleaned_data['user']
            raise forms.ValidationError('Không tồn tại id user')
        raise forms.ValidationError('Không tìm thấy user được gửi')

    def clean_status(self): # Kiểm tra status hợp lệ in [-1,0,1]
        if 'status' in self.cleaned_data:
            if self.cleaned_data['status'] in [-1,0,1]:
                return self.cleaned_data['status']
        return forms.ValidationError('Status không hợp lệ')

class TaskFormAdd1(TaskForm):
    def clean_start(self): #start>=date_now ,start:m/d/Y

        '''
        Kiểm tra xem có thời gian gửi và khác None và kiểm tra hợp lệ >= ngày hiện tại,
        nếu không có thời gian gửi -> None
        '''
        if ('start' in self.cleaned_data) and (self.cleaned_data['start'] is not None): 
            date=datetime.datetime.strftime(self.cleaned_data['start'],'%m/%d/%Y')
            date1=datetime.datetime.strptime(date,'%m/%d/%Y')
            date2 = datetime.datetime(datetime.datetime.today().year,datetime.datetime.today().month,datetime.datetime.today().day)
            # date2 = utc.localize(date2)
            # raise forms.ValidationError('Phải lớn hơn ngày hiện tại là %s --%s'%(date1,date2))
            # date1 = utc.localize(date1) 
            if date1 >= date2 :
                return self.cleaned_data['start']
            raise forms.ValidationError('Phải lớn hơn  hoặc bằng ngày hiện tại')
        return None

    # def clean_end(self):
    #     if 'start' in self.cleaned_data:
    #         raise forms.ValidationError('Có')
    #     raise forms.ValidationError('Không')
    #     if ('end' in self.cleaned_data) and self.cleaned_data['end'] is not None:
    #         # raise forms.ValidationError('123 %s-%s'%(self.cleaned_data['end'],self.cleaned_data['start']))
    #         if ('start' in self.cleaned_data) and (self.cleaned_data['start'] is not None):
    #             raise forms.ValidationError('123 %s   -%s '%(self.cleaned_data['end']),self.cleaned_data['start'])
    #             if self.cleaned_data['end']>=self.cleaned_data['start']:
    #                 raise forms.ValidationError('lớn hơn ')
                
    #     raise forms.ValidationError('Không ')

    
    # def clean_deadline(self): #deadline>=date_now ,start:m/d/Y
    #     '''
    #     Kiểm tra xem có thời gian gửi và khác None và kiểm tra hợp lệ >= ngày hiện tại,
    #     nếu không có thời gian gửi -> None
    #     '''
    #     if ('deadline' in self.cleaned_data) and (self.cleaned_data['deadline'] is not None): 
    #         date=datetime.datetime.strftime(self.cleaned_data['deadline'],'%m/%d/%Y')
    #         date1=datetime.datetime.strptime(date,'%m/%d/%Y')
    #         date2 = datetime.datetime(datetime.datetime.today().year,datetime.datetime.today().month,datetime.datetime.today().day)
    #         # date2 = utc.localize(date2)
    #         # raise forms.ValidationError('Phải lớn hơn ngày hiện tại là %s --%s'%(date1,date2))
    #         # date1 = utc.localize(date1) 
    #         if date1 >= date2 :
    #             return self.cleaned_data['deadline']
    #         raise forms.ValidationError('Phải lớn hơn  hoặc bằng ngày hiện tại')
    #     return None

    def clean(self):
        cleaned_data=super().clean() # Gọi clean lớp trên
        '''Kiểm tra time end >= time start'''
        if ('start' in cleaned_data and 
            'end' in cleaned_data and 
            cleaned_data['start'] is not None and 
            cleaned_data['end'] is not None):
            if cleaned_data['start']>=cleaned_data['end']:
                self.add_error('end','end phải lớn hơn start')

        '''Kiểm tra time deadline >= time start'''
        if ('start' in cleaned_data and 
            'deadline' in cleaned_data and 
            cleaned_data['start'] is not None and 
            cleaned_data['deadline'] is not None):
            if cleaned_data['start']>=cleaned_data['deadline']:
                self.add_error('deadline','deadline phải lớn hơn start')


class TaskFormAdd(TaskForm): # TaskForm để kiểm tra và thêm task task vào database(không dùng cho update)
    
    def clean_start(self): #start>=date_now ,start:m/d/Y

        '''
        Kiểm tra xem có thời gian gửi và khác None và kiểm tra hợp lệ >= ngày hiện tại,
        nếu không có thời gian gửi -> None
        '''
        if ('start' in self.cleaned_data) and (self.cleaned_data['start'] is not None): 
            date=datetime.datetime.strftime(self.cleaned_data['start'],'%m/%d/%Y')
            date1=datetime.datetime.strptime(date,'%m/%d/%Y')
            date2 = datetime.datetime(datetime.datetime.today().year,datetime.datetime.today().month,datetime.datetime.today().day)
            if date1 >= date2 :
                return self.cleaned_data['start']
            raise forms.ValidationError('Phải lớn hơn  hoặc bằng ngày hiện tại')
        return None    
        
    def clean(self):
        cleaned_data=super().clean() # Gọi clean lớp trên
        '''Kiểm tra time end >= time start'''
        if ('start' in cleaned_data and 
            'end' in cleaned_data and 
            cleaned_data['start'] is not None and 
            cleaned_data['end'] is not None):
            if cleaned_data['start']>cleaned_data['end']:
                self.add_error('end','End phải lớn hơn Start')

        '''Kiểm tra time deadline >= time start'''
        if ('start' in cleaned_data and 
            'deadline' in cleaned_data and 
            cleaned_data['start'] is not None and 
            cleaned_data['deadline'] is not None):
            if cleaned_data['start']>cleaned_data['deadline']:
                self.add_error('deadline','Deadline phải lớn hơn Start')

class TaskFormUpdate(TaskForm): # TaskFormUpdate để kiểm tra và update task vào database()
    def clean(self):
        cleaned_data=super().clean() # Gọi clean lớp trên
        '''Kiểm tra time end >= time start'''
        if ('start' in cleaned_data and 
            'end' in cleaned_data and 
            cleaned_data['start'] is not None and 
            cleaned_data['end'] is not None):
            if cleaned_data['start'] >cleaned_data['end']:
                self.add_error('end','End phải lớn hơn Start')

        '''Kiểm tra time deadline >= time start'''
        if ('start' in cleaned_data and 
            'deadline' in cleaned_data and 
            cleaned_data['start'] is not None and 
            cleaned_data['deadline'] is not None):
            if cleaned_data['start']>cleaned_data['deadline']:
                self.add_error('deadline','Deadline phải lớn hơn Start')

class ProjectForm(forms.Form): # Form để thêm mới project
    name=forms.CharField(max_length=50) 
    describe=forms.CharField(widget=forms.Textarea(attrs={'class': 'text_input1','cols':'50','rows':'3'})) 
    note=forms.CharField()


class UpdateProject(forms.ModelForm):
    class Meta:
        model=Projects
        fields='__all__'
