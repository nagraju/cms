#from django.urls import re_path as url
from django.urls import path,include
from .views import student
from .views import attendance
from .views import marks
from .views import Unit1marks

urlpatterns = [
path("i/", student.index, name="index"),
path("n/", student.newst, name="newst"),
path("a/upload", attendance.upload, name="upload"),
path("m/upload", marks.upload, name="upload"),
path("u1m/upload", Unit1marks.upload, name="upload"),
path("a/", attendance.index, name="atten_index"),
path("m/", marks.index, name="Marks_index"),
path("u1m/", Unit1marks.index, name="Marks_index"),
path("<str:spin>/", student.show, name="show"),
path("<str:spin>/edit", student.edit, name="edit"),
]
