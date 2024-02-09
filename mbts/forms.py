from django import forms
from django.forms import ModelForm
from .models import Students, Attendance, StudentClass
from .models import Students, Unit1marks, StudentClass,Unit2marks,Unit3marks


 
# creating a form 
class InputForm(forms.Form):
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
    password = forms.CharField(widget = forms.PasswordInput())



class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = ["pin","sname","fname","mname","phno","fphno","dob","gender","category","scategory","religion","sacno","sbranch","macno","mifsc","mbranch","email","sscrank","sschallticketno","address","village","mandal","dist","allotedcategory","dateofjoining","polycetrank","polycetno","aadharno","rationno","tcno","tcissueddate","discontinueddate","odno","odissueddate","studycertificateissueddate"]	 
        widgets = {
            'student_image': forms.FileInput(attrs={'class': 'form-control'}),                     
        }      
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Enter ' + field
            })

class ClassAttendance(ModelForm):
    attendance = forms.ModelChoiceField(Attendance.objects.all())
    class Meta:
        model = StudentClass
        fields = ("sem", "attendance")

class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ("nfw","npd")

#unit marks form

class ClassUnit1marks(ModelForm):
    Unit1marks= forms.ModelChoiceField(Unit1marks.objects.all())
    class Meta:
        model = StudentClass
        fields = ("sem", "Unit1marks")

class Unit1marksForm(ModelForm):
    class Meta:
        model = Unit1marks
        fields = ("s1","s2")

class ClassUnit2marks(ModelForm):
    Unit2marks= forms.ModelChoiceField(Unit2marks.objects.all())
    class Meta:
        model = StudentClass
        fields = ("sem", "Unit2marks")

class Unit2marksForm(ModelForm):
    class Meta:
        model = Unit2marks
        fields = ("s1","s2")

class ClassUnit3marks(ModelForm):
    Unit3marks= forms.ModelChoiceField(Unit3marks.objects.all())
    class Meta:
        model = StudentClass
        fields = ("sem", "Unit3marks")

class Unit3marksForm(ModelForm):
    class Meta:
        model = Unit3marks
        fields = ("s1","s2")        





        
    

class SearchForm(ModelForm):
    class Meta:
        model = StudentClass
        #SEMS = (("1YESR","1ST YEAR"),("3SEM","3 SEM"),("4SEM","4 SEM"),("5SEM","5 SEM"),("6SEM", "6 SEM"))
        fields = ['sem',]
        widgets = {
            'sem': forms.Select(choices=StudentClass.SEMS, attrs={'class': 'form-control'}),
        }
