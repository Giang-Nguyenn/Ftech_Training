import datetime

from django import forms
from .models import User
from .models import Post

class SignForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'mail', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())

class AddPost(forms.Form):
    postName = forms.CharField(max_length=100)
    postContent = forms.CharField(max_length=1000)
