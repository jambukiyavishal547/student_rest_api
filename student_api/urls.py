from django.urls import path
from django.contrib import admin
from student_api.views import FacultyDetail,FacultyList,StudentList,StudentDetail
urlpatterns = [
    path('facultys',FacultyList.as_view()),
    path('facultys/<int:pk>',FacultyDetail.as_view()),
    path('students',StudentList.as_view()),
    path('students/<int:pk>',StudentDetail.as_view()),
    path('admin/',admin.site.urls),
]