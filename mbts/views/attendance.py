from django.shortcuts import render
from django.shortcuts import render

from mbts.models import Attendance, StudentClass
from mbts.forms import ClassAttendance, SemSearchForm, SearchForm
from django.core.files.storage import FileSystemStorage
from django.forms import modelformset_factory
from django.db.models import Sum


def upload(request):
    context = {}
    
    if(request.method == "GET"):        
        sf = SemSearchForm(request.GET)        
        context["sf"] = sf
        return render(request, "attendance/upload.html", context)
    else:
        if request.method == 'POST' and request.FILES['csvfile']:
            sem = request.POST.get("sem","1YEAR")
            myfile = request.FILES['csvfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.path(filename)
            Attendance.import_csv(uploaded_file_url,sem)
        return render(request,"attendance/upload_res.html", context)

def index(request):
    context = {}
    sem = request.GET.get("sem","1YEAR")            
    sf = SemSearchForm(request.GET)    
    context["semform"] = sf
    atte = Attendance.objects.filter(sem=sem).prefetch_related("student").all
    context["atte"] = atte
    context["sem"] = sem
    return render(request, "attendance/index.html", context)


def show(request, student):
    attendances = Attendance.objects.filter(student=student).all()
    context = {"attendances" : attendances }
    return render(request, "attendance/show.html", context)

def edit(request,pin):
    context = {}
    atte = Attendance.objects.all
    fs = modelformset_factory(Attendance, fields=["month","nfw","npd",],extra=0)
    context["fs"] = fs
    return render(request, "attendance/edit.html", context)


def bulkedit(request,sem):
    fs = modelformset_factory(Attendance, fields=["month","nfw","npd"],extra=2)
    context = {}     
    if(request.method == "GET"):                          
        context["fs"] = fs
        return render(request, "attendance/edit.html", context)
    else:
        f = fs(request.POST)
        f.save()
        context["fs"] = fs
        return render(request, "attendance/edit.html", context)

        





