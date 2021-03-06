from rest_framework import serializers
from datetime import datetime
# from django.contrib.auth.models import User
from .models import Projects, Task, UserProject, User, Tenant
from django.utils import timezone

from Shared_DB_Schema import models
now = timezone.now()


class TenantSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = "__all__"


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'tenant']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class SuperUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password',
                  'tenant', 'is_staff', 'is_superuser']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class SuperUserSerializersAll(serializers.Serializer):
    username=serializers.CharField(read_only=True)
    tenant=serializers.CharField(read_only=True)
    deleted=serializers.DateTimeField()



class UserReadOnlySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['name', 'describe', 'members',
                  'status', 'note', 'create_at', 'update_at', 'tenant']
        extra_kwargs = {
            'members': {
                "required": False
            },
            'tenant': {
                "required": False
            }
        }

    def validate_status(self, value):
        if value in [-1, 0, 1]:
            return value
        raise serializers.ValidationError('Status không hợp lệ')


class ProjectReadOnlySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    describe = serializers.CharField(read_only=True)
    status = serializers.IntegerField(read_only=True)
    create_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)
    note = serializers.CharField(read_only=True)


class ProjectUpdateUserSerializers(serializers.Serializer):
    id = serializers.CharField()

    def validate_id(self, value):
        '''
        value='1,2,3,n'
        '''
        list_id_user = value.split(',')
        for i in list_id_user:
            try:
                int(i)
            except:
                raise serializers.ValidationError(
                    'Không phải dạng int:  %s' % i)

        for i in list_id_user:
            user = User.objects.filter(pk=i)
            if not user:
                raise serializers.ValidationError(
                    'Không có user có id là   %s' % (i))
        return value


class TaskSerializers(serializers.ModelSerializer):
    # project = ProjectSerializers()

    class Meta:
        model = Task
        fields = ['name', 'project', 'user', 'describe', 'status', 'start',
                  'end', 'deadline', 'note', 'create_at', 'update_at', 'update_by','tenant']
        extra_kwargs = {
            'tenant': {
                "required": False
            }
        }


class TaskPostSerializers(serializers.ModelSerializer):
    start = serializers.DateTimeField(required=True)

    class Meta:
        model = Task
        fields = ['name', 'project', 'user', 'describe', 'status', 'start',
                  'end', 'deadline', 'note', 'create_at', 'update_at', 'update_by']
        extra_kwargs = {
            'tenant': {
                "required": False
            }
        }

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


class TenantSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = "__all__"

class TenantSerializersAll(serializers.ModelSerializer):
    # CHOICES = (
    #     ('True', 'Male'),
    #     ('F', 'Female'),
    # )
    deleted=serializers.DateTimeField()
    class Meta:
        model = Tenant
        fields = "__all__"
        extra_kwargs = {
            'name': {
                "read_only": True
            },
            'subdomain_prefix': {
                "read_only": True
            },
        }

class UserReadOnlySerializerAll(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    deleted=serializers.DateTimeField()

class ProjectSerializerAll(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    describe = serializers.CharField(read_only=True)
    status = serializers.IntegerField(read_only=True)
    note = serializers.CharField(read_only=True)
    deleted=serializers.DateTimeField()