
from django.urls import path
from .views import student
from .views import attendance

urlpatterns = [
path("i/", student.index, name="index"),
path("n/", student.newst, name="newst"),
path("a/upload", attendance.upload, name="upload"),
path("a/", attendance.index, name="atten_index"),
path("m/upload", Marks.upload, name="upload"),
path("m/", Marks.index, name="atten_index"),

path("<str:spin>/", student.show, name="show"),
path("<str:spin>/edit", student.edit, name="edit"),




]
