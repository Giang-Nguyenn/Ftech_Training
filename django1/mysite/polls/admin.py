from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question
from .models import Choice
from .models import test

class test1(admin.ModelAdmin):#tạo class để chỉ định những trường hienr thị trong admin
    fields = ['name', 'content','create'] #list các trường để hiển thị trên trang admin

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(test, test1)
