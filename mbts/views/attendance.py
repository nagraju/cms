from django.shortcuts import render
from django.shortcuts import render

from mbts.models import Attendance, StudentClass
from mbts.forms import ClassAttendance, SearchForm
from django.core.files.storage import FileSystemStorage
from django.forms import modelformset_factory
from django.db.models import Sum


def upload(request):
    context = {}
    if(request.method == "GET"):       
        
        return render(request, "attendance/upload.html", context)
    else:
        if request.method == 'POST' and request.FILES['csvfile']:
            myfile = request.FILES['csvfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.path(filename)
            Attendance.import_csv(uploaded_file_url)
        return render(request,"attendance/upload_res.html", context)


def index(request, sem='1'):
    context = {}
    sem = request.GET.get("sem",1)        
    sc = StudentClass.objects.filter(sem=sem)
    sf = SearchForm(request.GET,instance=StudentClass())    
    context["sform"] = sf
    if(sc):        
        atte = (Attendance.objects.filter(studentclass_id=sc[0].sem).select_related("student").values("student_id","student__sname").annotate(tp = Sum("npd"),tw = Sum("nfw")).order_by())
        context["atte"] = atte
    else:
        context["atte"] = []
    context["sem"] = sem
    return render(request, "attendance/index.html", context)

def monthly(request, sem='1'):
    context = {}
    sem = request.GET.get("sem",1)        
    sc = StudentClass.objects.filter(sem=sem)
    sf = SearchForm(request.GET,instance=StudentClass())    
    context["sform"] = sf
    if(sc):        
        atte = Attendance.objects.filter(studentclass_id=sc[0].sem).prefetch_related("student").all
        context["atte"] = atte
    else:
        context["atte"] = []
    context["sem"] = sem
    return render(request, "attendance/monthly.html", context)


def show(request, student):
    s = Attendance.objects.get(student=student)
    context = {"s" : s }
    return render(request, "attendance/show.html", context)

def edit(request,pin):
    context = {}
    atte = Attendance.objects.all
    fs = modelformset_factory(Attendance, fields=["student", "nfw","npd","twd","tpd","per"])
    context["fs"] = fs
    return render(request, "attendance/edit.html", context)


def bulkedit(request,sem):
    fs = modelformset_factory(Attendance, fields=["nfw","npd"])
    context = {}     
    if(request.method == "GET"):                          
        context["fs"] = fs
        return render(request, "attendance/edit.html", context)
    else:
        f = fs(request.POST)
        f.save()
        context["fs"] = fs
        return render(request, "attendance/edit.html", context)

        





