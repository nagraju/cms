#from django.urls import re_path as url
from django.urls import path,include
from .views import student
from .views import attendance
from .views import marks
from .views import Unit1marks,Unitmarks, Unit2marks,Unit3marks, totalattendance

urlpatterns = [
path("i/", student.index, name="student_index"),
path("i/upload", student.upload, name="student_upload"),
path("i/<str:spin>/show", student.show, name="student_show"),
path("i/<str:spin>/reset", student.pass_reset, name="student_reset_pass"),

path("i/<str:spin>/edit", student.edit, name="student_edit"),
path("i/<str:spin>/delete", student.delete, name="student_delete"),
path("i/new", student.newst, name="newst"),
path('profile/', student.profile, name='users-profile'),
path("i/report", student.report, name="student_report"),



#Attendance
path("a/upload", attendance.upload, name="atte_upload"),
path("a/index", attendance.index, name="atten_index"),
path("a/<str:pin>/edit", attendance.edit, name="atten_edit"),
path("a/<str:sem>/bulkedit", attendance.bulkedit, name="atten_bulkedit"),
path("<str:student>/show", attendance.show, name="atten_show"),
path("a/<str:sem>/delete", attendance.delete, name="atten_del_sem"),

path("t/", totalattendance.index, name="total_atten_index"),

path("m/upload", marks.upload, name="marks_upload"),
path("m/", marks.index, name="marks_index"),
path("m/<str:sem>",marks.index, name="m_index"),
path("m/<str:pin>/edit", marks.edit, name="m_edit"),
path("m/<str:sem>/bulkedit", marks.bulkedit, name="m_bulkedit"),
path("<str:spin>/m", marks.show, name="m_show"),


path("um/", Unitmarks.index, name="um_index"),
path("um/upload", Unitmarks.upload, name="um_upload"),
path("um/<str:spin>/edit", Unitmarks.edit, name="um_edit"),
path("um/<str:spin>/bulkedit", Unitmarks.bulkedit, name="um_bulkedit"),
path("um/<str:spin>", Unitmarks.show, name="um_show"),



path("u/", Unit1marks.index, name="um1_index"),
path("u/<str:sem>",Unit1marks.index, name="u1m_index"),
path("u/<str:spin>/edit", Unit1marks.edit, name="u1m_edit"),
path("u/<str:spin>/bulkedit", Unit1marks.bulkedit, name="u1m_bulkedit"),
path("u/<str:spin>", Unit1marks.show, name="u1m_show"),
path("u/upload", Unit1marks.upload, name="u1m_upload"),

]
