from rest_framework import serializers
from datetime import date
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Student
        fields=['name','phone','email','address','birth_day']

    def validate_birth_day(self,value):
        today=date.today()
        if today > value:
            return value
        raise serializers.ValidationError('birth_day phải nhỏ hơn ngày hiện tại')