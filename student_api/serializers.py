from rest_framework import serializers
from.models import Faculty,Student

class FacultySerializers(serializers.ModelSerializer):
    class Meta:
        model=Faculty
        fields=('id','name','email','mobile','subject')
        

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('id','name','email','mobile','subject','faculty')