from django.shortcuts import render
from rest_framework import generics
from .models import Faculty,Student
from.serializers import FacultySerializers,StudentSerializers
# Create your views here.

class FacultyList(generics.ListCreateAPIView):
    queryset=Faculty.objects.all()
    serializer_class=FacultySerializers
              
class FacultyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Faculty
    serializer_class=FacultySerializers


class StudentList(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
                
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student
    serializer_class=StudentSerializers
