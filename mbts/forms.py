from django import forms
from django.forms import ModelForm
from .models import Students, Attendance, StudentClass
from .models import Students, Unit1marks, StudentClass,Unit2marks,Unit3marks, UnitMarks


 
# creating a form 
class InputForm(forms.Form):
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
    password = forms.CharField(widget = forms.PasswordInput())



class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = ["pin","sname","sem","fname","mname","phno","fphno","dob","gender","category","scategory","religion","sacno","sbranch","macno","mifsc","mbranch","email","sscrank","sschallticketno","address","village","mandal","dist","allotedcategory","dateofjoining","polycetrank","polycetno","aadharno","rationno","tcno","tcissueddate","discontinueddate","odno","odissueddate","studycertificateissueddate"]	 
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
        fields = ("month","sem","nfw","npd")

#unit marks form

class ClassUnit1marks(ModelForm):
    Unit1marks= forms.ModelChoiceField(Unit1marks.objects.all())
    class Meta:
        model = StudentClass
        fields = ("sem", "Unit1marks")

class Unit1marksForm(ModelForm):
    class Meta:
        model = Unit1marks
        fields = ("s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11")

class ClassUnit2marks(ModelForm):
    Unit2marks= forms.ModelChoiceField(Unit2marks.objects.all())
    class Meta:
        model = StudentClass
        fields = ("sem", "Unit2marks")


class UnitmarksForm(ModelForm):
    class Meta:
        model = UnitMarks
        fields = ("s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11")

class Unit2marksForm(ModelForm):
    class Meta:
        model = Unit2marks
        fields = ("s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11")

class ClassUnit3marks(ModelForm):
    Unit3marks= forms.ModelChoiceField(Unit3marks.objects.all())
    class Meta:
        model = StudentClass
        fields = ("sem", "Unit3marks")

class Unit3marksForm(ModelForm):
    class Meta:
        model = Unit3marks
        fields = ("s1","s2","s3","s4","s5","s6","s7","s8","s9","s10","s11")        




class SearchForm(ModelForm):
    class Meta:
        model = StudentClass
        #SEMS = (("1YEAR","1ST YEAR"),("3SEM","3 SEM"),("4SEM","4 SEM"),("5SEM","5 SEM"),("6SEM", "6 SEM"))
        fields = ['sem',]
        widgets = {
            'sem': forms.Select(choices=StudentClass.SEMS, attrs={'class': 'form-control'}),
        }


class SemSearchForm(forms.Form):    
    sem = forms.ChoiceField(required=False, choices=StudentClass.SEMS, widget=forms.Select( attrs={'class': 'btn btn-primary btn-neutral'}))
    

class UnitSearchForm(forms.Form):   
    SEMS = (("1YEAR","1st YEAR"),("3SEM","3rd SEM"),("4SEM","4th SEM"),("5SEM","5th SEM")) 
    UNITS = (("UNIT1","UNIT 1"),('UNIT2','UNIT 2'),('UNIT3', 'UNIT 3'))
    sem = forms.ChoiceField(required=False, choices= SEMS, widget=forms.Select( attrs={'class': 'btn btn-primary btn-neutral'}))
    unit = forms.ChoiceField(required=False, choices= UNITS, widget=forms.Select( attrs={'class': 'btn btn-primary btn-neutral'}))


class StudentProfileForm(ModelForm):
    class Meta:
        model = Students
        fields = ["fname","address","village","mandal","dist","email",]
