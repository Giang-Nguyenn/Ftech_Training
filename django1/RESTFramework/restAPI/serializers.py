from rest_framework import serializers
from datetime import datetime
from django.contrib.auth.models import User
from .models import Projects, Task, UserProject
from django.utils import timezone
now = timezone.now()


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProjectSerializers(serializers.ModelSerializer):
    # members=UserSerializers(many=True,allow_null=True,required=False,read_only=True)
    class Meta:
        model = Projects
        fields = ['name', 'describe', 'members',
                  'status', 'note', 'create_at', 'update_at']
        extra_kwargs = {
            'members': {
                "required": False
            }
        }

    def validate_status(self, value):
        if value in [-1, 0, 1]:
            return value
        raise serializers.ValidationError('Status không hợp lệ')

class UserReadOnlySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)

class ProjectReadOnlySerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    members = UserReadOnlySerializer(many=True, read_only=True)

class ProjectAddUserSerializers(serializers.ModelSerializer):
    username = serializers.ChoiceField(choices=User.objects.all())

    class Meta:
        model = User
        fields = ['username']


class TaskSerializers(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    user = UserSerializers()

    class Meta:
        model = Task
        fields = ['name', 'project', 'user', 'describe', 'status', 'start',
                  'end', 'deadline', 'note', 'create_at', 'update_at', 'update_by']


class TaskPostSerializers(serializers.ModelSerializer):
    start = serializers.DateTimeField(required=True)

    class Meta:
        model = Task
        fields = ['name', 'project', 'user', 'describe', 'status', 'start',
                  'end', 'deadline', 'note', 'create_at', 'update_at', 'update_by']

    def validate_start(self, value):
        # today=datetime.now()
        if now <= value:
            return value
        raise serializers.ValidationError(
            'start phải lớn hơn ngày hiện tại %s' % type(now))

    def validate(self, data):
        if data.get('end') is not None:
            if data['start'] > data['end']:
                raise serializers.ValidationError(
                    'Time end phải lớn hơn time start')

        if data.get('deadline') is not None:
            if data['start'] > data['deadline']:
                raise serializers.ValidationError(
                    'Time deadline phải lớn hơn time start')

        return data


class ProjectListUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProject
        fields = ['project', 'user', 'date_joined']




class TaskSerializers1(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['name', 'project', 'user', 'describe', 'status', 'start',
                  'end', 'deadline', 'note', 'create_at', 'update_at', 'update_by']

class TaskSerializers2(serializers.Serializer):
    name=serializers.CharField(read_only=True)
    project=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    describe=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    start=serializers.CharField(read_only=True)
    end=serializers.CharField(read_only=True)
    deadline=serializers.CharField(read_only=True)
    note=serializers.CharField(read_only=True)
    create_at=serializers.CharField(read_only=True)
    update_at=serializers.CharField(read_only=True)
    update_by=serializers.CharField(read_only=True)