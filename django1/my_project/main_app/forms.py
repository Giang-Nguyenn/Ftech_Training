import pytz
from django import forms
import re
import datetime

from django.contrib.auth.models import User
from .models import Projects, Task, UserProject

from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
# DateInput = partial(forms.DateTimeInput, {'class': 'datetimepicker'})


utc = pytz.UTC


class TaskForm(forms.ModelForm):
    '''
     Form hiển Add,Update Task,truyền vào projetc_id(để lấy lấy chose project và list user thuộc project đó) 
    '''
    start = forms.DateField(widget=DateInput(), required=True)
    # start =forms.DateField(widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M'),required=True)
    end = forms.DateField(widget=DateInput(), required=False)
    deadline = forms.DateField(widget=DateInput(), required=False)
    describe = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'text_input1', 'cols': '50', 'rows': '3'}), required=False)
    note = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'text_input1', 'cols': '50', 'rows': '3'}), required=False)

    class Meta:
        model = Task
        fields = ['name', 'project', 'user', 'describe',
                  'status', 'start', 'end', 'deadline', 'note']

    def __init__(self, *args, project_id, **kwargs):  # Thêm tham số project_id
        # call standard __init__
        super().__init__(*args, **kwargs)
        # extend __init__
        self.fields['project'] = forms.ModelChoiceField(
            queryset=Projects.objects.filter(pk=project_id))
        self.fields['user'] = forms.ModelChoiceField(
            queryset=Projects.objects.get(pk=project_id).members.all())

    def clean_project(self):  # Kiểm tra id project có tồn tại không
        if self.cleaned_data.get('project') is not None:
            if Projects.objects.filter(pk=self.cleaned_data['project'].id):
                return self.cleaned_data['project']
        return forms.ValidationError('Không tồn tại id project')

    def clean_user(self):  # Kiểm tra user gửi lên có thuộc Project
        if self.cleaned_data.get('user') is not None:
            if User.objects.filter(pk=self.cleaned_data['user'].id):
                return self.cleaned_data['user']
            raise forms.ValidationError('Không tồn tại id user')
        if self.cleaned_data['user'] is None:
            return None
        raise forms.ValidationError('Không tìm thấy user được gửi')

    def clean_status(self):  # Kiểm tra status hợp lệ in [-1,0,1]
        if self.cleaned_data.get('status') is not None:
            if self.cleaned_data['status'] in [-1, 0, 1]:
                return self.cleaned_data['status']
        # return 0
        return forms.ValidationError('Status không hợp lệ')


# TaskForm để kiểm tra và thêm task task vào database(không dùng cho update)
class TaskFormAdd(TaskForm):

    def clean_start(self):  # start>=date_now ,start:m/d/Y
        '''
        Kiểm tra xem có thời gian gửi và khác None và kiểm tra hợp lệ >= ngày hiện tại,
        nếu không có thời gian gửi -> None
        '''
        # ('start' in self.cleaned_data) and (self.cleaned_data['start'] is not None)
        if self.cleaned_data.get('start') is not None:
            # raise forms.ValidationError('%s'%self.cleaned_data.get('start'))
            date = datetime.datetime.strftime(
                self.cleaned_data['start'], '%m/%d/%Y')
            date1 = datetime.datetime.strptime(date, '%m/%d/%Y')
            date2 = datetime.datetime(datetime.datetime.today(
            ).year, datetime.datetime.today().month, datetime.datetime.today().day)
            if date1 >= date2:
                return self.cleaned_data['start']
            raise forms.ValidationError(
                'Phải lớn hơn  hoặc bằng ngày hiện tại')
        return None

    def clean(self):
        cleaned_data = super().clean()  # Gọi clean lớp trên
        '''Kiểm tra time end >= time start'''
        if (cleaned_data.get('start') is not None and
                cleaned_data.get('end') is not None):
            if cleaned_data['start'] > cleaned_data['end']:
                self.add_error('end', 'End phải lớn hơn Start')

        '''Kiểm tra time deadline >= time start'''
        if (cleaned_data.get('start') is not None and
                cleaned_data.get('deadline') is not None):
            if cleaned_data['start'] > cleaned_data['deadline']:
                self.add_error('deadline', 'Deadline phải lớn hơn Start')


# TaskFormUpdate để kiểm tra và update task vào database()
class TaskFormUpdate(TaskForm):
    def clean(self):
        cleaned_data = super().clean()  # Gọi clean lớp trên
        '''Kiểm tra time end >= time start'''
        if (cleaned_data.get('start') is not None and
                cleaned_data.get('end') is not None):
            if cleaned_data['start'] > cleaned_data['end']:
                self.add_error('end', 'End phải lớn hơn Start')

        '''Kiểm tra time deadline >= time start'''
        if (cleaned_data.get('start') is not None and
                cleaned_data.get('deadline') is not None):
            if cleaned_data['start'] > cleaned_data['deadline']:
                self.add_error('deadline', 'Deadline phải lớn hơn Start')


class ProjectForm(forms.Form):  # Form để thêm mới project
    name = forms.CharField(max_length=50)
    describe = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'text_input1', 'cols': '50', 'rows': '3'}))
    note = forms.CharField()


class UpdateProject(forms.ModelForm):
    describe = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'text_input1', 'cols': '50', 'rows': '3'}), required=False)
    note = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'text_input1', 'cols': '50', 'rows': '3'}), required=False)

    class Meta:
        model = Projects
        fields = '__all__'
