from django.contrib import admin
from .models import Students, Attendance, Unit1marks

admin.site.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    pass
