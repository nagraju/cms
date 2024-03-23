from django.shortcuts import render
from django.shortcuts import render
from mbts.models import Unit1marks,Students, UnitMarks, Unit2marks, Unit3marks
from django.core.files.storage import FileSystemStorage
from mbts.forms import ClassUnit1marks, UnitSearchForm, Unit1marksForm, Unit2marksForm, Unit3marksForm, UnitmarksForm
from django.forms import modelformset_factory


def upload(request):
    context = {}
    if(request.method == "GET"): 
        form = UnitSearchForm(request.GET)   
        sem = request.GET.get("sem",'1YEAR') 
        unit = request.GET.get("unit",'UNIT1')
        context["form"]  = form
        return render(request, "Unitmarks/upload.html", context)
    else:
        if request.method == 'POST' and request.FILES['csvfile']:
            form = UnitSearchForm(request.GET)   
            sem = request.POST.get("sem",'1YEAR') 
            unit = request.POST.get("unit",'UNIT1') 
            myfile = request.FILES['csvfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.path(filename)
            um= UnitMarks.import_csv(uploaded_file_url,sem,unit)            
        return render(request, "Unitmarks/upload_res.html", context)

        
def index(request):
    form = UnitSearchForm(request.GET)
    sem = request.GET.get("sem",'1YEAR') 
    unit = request.GET.get("unit",'UNIT1')
    um= UnitMarks.objects.filter(sem=sem,unit=unit).all()
    context = {"um": um} 
    context['form']  = form
    context['unit'] = unit
    context['sem']  = sem
    return render(request, "Unitmarks/index.html", context)


def show(request, spin):        
    s= Students.objects.get(pin=spin)
    um = s.unitmarks_set.all()    
    context = {"um" : um }        
    return render(request, "Unitmarks/show.html", context)



def edit(request,spin):
    context = {}
    sem = request.GET.get("sem",'1YEAR') 
    unit = request.GET.get("unit",'UNIT1')
    context['unit'] = unit
    context['sem']  = sem
    fs = ""    
    if request.method != 'POST':
        um= UnitMarks.objects.get(sem=sem,unit=unit, student_id=spin)
        fs = UnitmarksForm(instance = um)            
        context["fs"] = fs
        return render(request, "Unitmarks/edit.html", context)  
    else:
        um= UnitMarks.objects.get(sem=sem,unit=unit, student_id=spin)
        fs = UnitmarksForm(request.POST,instance=um)
        if fs.is_valid():
            fs.save()       
            return render(request, "Unitmarks/update.html")
        else:
            sem = request.GET.get("sem",'1YEAR') 
            unit = request.GET.get("unit",'UNIT1')
            context['unit'] = unit
            context['sem']  = sem
            context["fs"] = fs
            return render(request, "Unitmarks/edit.html", context)  
        
        




def bulkedit(request,spin):
    fs = modelformset_factory(UnitMarks, fields=["s1","s2"])
    context = {}     
    if(request.method == "GET"):                          
        context["fs"] = fs
        return render(request, "Unitmarks/edit.html", context)
    else:
        f = fs(request.POST)
        f.save()
        context["fs"] = fs
        return render(request, "Unitmarks/edit.html", context)
     
            


