#from django.urls import re_path as url
from django.urls import path,include
from .views import api

urlpatterns = [
    #path("", api.profile, name="api_profile"),
    path("students/", api.students, name="api_students"),
    path("student/", api.student, name="api_student"),
    path("marks/", api.marks, name="api_marks"),
    #path("attendance", api.attendance, name="api_attendance"),
    #path("unit", api.unit, name="api_unit"),

]