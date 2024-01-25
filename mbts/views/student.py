from django.shortcuts import render
from django.shortcuts import render
from mbts.forms import StudentForm, SearchForm
from mbts.models import Students,Attendance
from django.core.files.storage import FileSystemStorage

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
            Students.import_csv(uploaded_file_url)
        return render(request, "attendance/upload_res.html", context)

def index(request):
    sl = Students.objects.all
    context = {"sl": sl}
    context["search"] = SearchForm()
    return render(request, "students/index.html", context)


# Create your views here.
def newst(request):
    context = {}
 
    if(request.method == "GET"):       
        context['forms'] = StudentForm()
        return render(request, "students/newst.html", context)
    else:
        sf = StudentForm(request.POST, request.FILES)
        sf.is_valid()     
        s = sf.save()
        context['s'] = s
        return render(request, "students/show.html", context)

  
def show(request, spin):
    s = Students.objects.get(pin=spin)
    context = {"s" : s }
    return render(request, "students/show.html", context)
    
   

def edit(request, spin):
    context = {}
    s = Students.objects.get(pin=spin)
    if(request.method == "GET"):    
        sf = StudentForm(instance=s)
        context['forms'] = sf
        return render(request, "students/edit.html",context)
    else:
        sf = StudentForm(request.POST, request.FILES, instance=s )
        sf.is_valid()     
        s = sf.save()
        context['s'] = s
        return render(request, "students/show.html", context)

def delete(request, spin):
    s = Students.objects.get(pk = spin)
    s.delete()
    return render(request, "students/delete.html")

def report(request):
    #projects = Project.objects.select_related('leader').all()
    spin = request.GET.get("spin","")
    context = {}
    if(spin!=""):        
        s = Students.objects.get(pin=spin)
        a= s.attendance_set.all()        
        context["s"] = s 
        context["spin"] = spin
        context["a"] = a
    return render(request, "students/report.html",context)  
    
