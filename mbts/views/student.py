from django.shortcuts import render
from mbts.forms import StudentForm, SearchForm, StudentProfileForm
from mbts.models import Students, User
from mbts.models import Students,Attendance,Unit1marks
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from mbts.resources import StudentsResource
import tablib 

def upload(request):
    context = {}
    if(request.method == "GET"):       
        
        return render(request, "students/upload.html", context)
    else:
        if request.method == 'POST' and request.FILES['csvfile']:
            myfile = request.FILES['csvfile']            
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.path(filename)
            with open(uploaded_file_url, 'r') as fh:
                imported_data = tablib.Dataset().load(fh)            
            sr = StudentsResource()                        
            result = sr.import_data(imported_data, dry_run=False) 
            context["result"] = result
            context["t"] = result.has_errors()
            return render(request, "students/upload_res.html", context)

@login_required  
def index(request):
    sl = Students.objects.all
    context = {"sl": sl}
    if(request.user.role == User.STUDENT):
        context["cu"] = request.user.students
        return render(request,"students/sindex.html", context)
    else:        
        context["search"] = SearchForm()
        return render(request, "students/index.html", context)

@login_required
def profile(request):
    context = {"u": request.user}
    s = request.user.students
    if(request.method=="GET"):        
        spf = StudentProfileForm(instance=s)
        context["s"] = s
        context["spf"] = spf
        return render(request, "students/profile.html", context)
    else:
        spf = StudentProfileForm(request.POST, instance=s )
        spf.is_valid()     
        s = spf.save()
        context['s'] = s
        context["spf"] = spf
        return render(request, "students/profile.html", context)

@login_required
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
    
   
@login_required
def edit(request, spin):
    context = {}
    s = Students.objects.get(pin=spin)
    if(request.method == "GET"):    
        sf = StudentForm(instance=s)
        context['forms'] = sf
        return render(request, "students/edit.html",context)
    else:
        sf = StudentForm(request.POST, request.FILES, instance=s )
        is_valid = sf.is_valid()     
        if(is_valid):
            s = sf.save()
        context['s'] = s
        context['sf'] = sf

        return render(request, "students/show.html", context)

@login_required
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
        u1m=s.unit1marks_set.all()       
        context["s"] = s 
        context["spin"] = spin
        context["a"] = a
        context["spin"] = spin
        context["u1m"] = u1m
        context["spin"] = spin

    return render(request, "students/report.html",context)  
    
