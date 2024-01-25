#from django.urls import re_path as url
from django.urls import path,include
from .views import student
from .views import attendance
from .views import marks
from .views import Unit1marks

urlpatterns = [
path("i/", student.index, name="student_index"),
path("i/upload", student.upload, name="student_upload"),
path("i/<str:spin>/show", student.show, name="student_show"),

path("i/<str:spin>/edit", student.edit, name="student_edit"),
path("i/<str:spin>/delete", student.delete, name="student_delete"),
path("i/new", student.newst, name="newst"),
path("i/<str:spin>/report", student.report, name="student_report"),



path("a/upload", attendance.upload, name="atte_upload"),
path("a/", attendance.index, name="atten_index"),
path("a/<str:sem>", attendance.index, name="atten_index"),
path("a/<str:pin>/edit", attendance.edit, name="atten_edit"),
path("a/<str:sem>/bulkedit", attendance.bulkedit, name="atten_bulkedit"),
path("<str:student>/show", attendance.show, name="atten_show"),

path("m/upload", marks.upload, name="upload"),

path("m/", marks.index, name="Marks1_index"),
path("u1m/", Unit1marks.index, name="um1_index"),
path("a/<str:sem>",Unit1marks.index, name="u1m_index"),
path("a/<str:pin>/edit", Unit1marks.edit, name="u1m_edit"),
path("a/<str:sem>/bulkedit", Unit1marks.bulkedit, name="u1m_bulkedit"),

path("<str:spin>/um", Unit1marks.show, name="u1m_show"),

path("u1m/upload", Unit1marks.upload, name="u1m_upload"),
]
