from django import forms
from django.forms import ModelForm
from .models import Students, Attendance, StudentClass

 
# creating a form 
class InputForm(forms.Form):
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
    password = forms.CharField(widget = forms.PasswordInput())



class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = ["pin","sname","dob"]

class ClassAttendance(ModelForm):
    attendance = forms.ModelChoiceField(Attendance.objects.all())
    class Meta:
        model = StudentClass
        fields = ("sem", "attendance")

class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ("nfw","npd")


class SearchForm(ModelForm):
    class Meta:
        model = StudentClass
        #SEMS = (("1YESR","1ST YEAR"),("3SEM","3 SEM"),("4SEM","4 SEM"),("5SEM","5 SEM"),("6SEM", "6 SEM"))
        fields = ['sem',]
        widgets = {
            'sem': forms.Select(choices=StudentClass.SEMS, attrs={'class': 'form-control'}),
        }