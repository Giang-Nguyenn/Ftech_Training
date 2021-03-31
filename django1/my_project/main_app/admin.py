from django.contrib import admin
from .models import Projects,UserProject,Task,UserSetting
# Register your models here.


admin.site.register(Projects)
admin.site.register(UserProject)
admin.site.register(Task)
admin.site.register(UserSetting)