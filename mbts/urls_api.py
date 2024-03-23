#from django.urls import re_path as url
from django.urls import path,include
from .views import api
from django.contrib.auth.views import LogoutView
from mbts.views.api import LoginAPI

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    #path("", api.profile, name="api_profile"),
    path("students/", api.students, name="api_students"),
    path("student/", api.student, name="api_student"),
    path("marks/", api.marks, name="api_marks"),
    #path("attendance", api.attendance, name="api_attendance"),
    #path("unit", api.unit, name="api_unit"),

    path('login/', LoginAPI.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]