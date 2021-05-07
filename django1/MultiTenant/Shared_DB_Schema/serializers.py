from rest_framework import serializers
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
now = timezone.now()

from .models import Projects

class ProjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"
