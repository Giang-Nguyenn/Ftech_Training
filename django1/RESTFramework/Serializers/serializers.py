from rest_framework import serializers
from datetime import datetime
from .models import Student,School


class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model=School
        fields=['name','address']


class StudentSerializers(serializers.ModelSerializer):
    # school1 = serializers.StringRelatedField(many=True)
    school = SchoolSerializers()


    class Meta:
        model=Student
        fields=['name','phone','members','email','address','birth_day','school']

    def validate_birth_day(self,value):
        today=datetime.now()
        if today > value:
            return value
        raise serializers.ValidationError('birth_day phải nhỏ hơn ngày hiện tại %s'%value)




class StudentSerializers1(serializers.Serializer):
    school = SchoolSerializers(read_only=True)
    name=serializers.CharField(max_length=50,initial='123')
    phone=serializers.CharField(max_length=12,allow_blank=True)
    email=serializers.EmailField(required=False)
    address=serializers.CharField(max_length=50)
    birth_day=serializers.DateField(allow_null=True)