from django.shortcuts import render
from django.shortcuts import render
from mbts.models import Unit1marks,Students, Unit2marks, Unit3marks
from django.core.files.storage import FileSystemStorage
from mbts.forms import ClassUnit1marks, UnitSearchForm, Unit1marksForm, Unit2marksForm, Unit3marksForm
from django.forms import modelformset_factory


def upload(request):
    context = {}
    if(request.method == "GET"): 
        form = UnitSearchForm(request.GET)   
        sem = request.GET.get("sem",'1YEAR') 
        unit = request.GET.get("unit",'1UNIT')
        context["form"]  = form
        return render(request, "Unit1marks/upload.html", context)
    else:
        if request.method == 'POST' and request.FILES['csvfile']:
            form = UnitSearchForm(request.GET)   
            sem = request.POST.get("sem",'1YEAR') 
            unit = request.POST.get("unit",'1UNIT') 
            myfile = request.FILES['csvfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.path(filename)
            if unit == 'UNIT3':
                um= Unit3marks.import_csv(uploaded_file_url,sem)
            elif unit == 'UNIT2':
                um= Unit2marks.import_csv(uploaded_file_url,sem)
            else:
                um= Unit1marks.import_csv(uploaded_file_url,sem)
            
        return render(request, "Unit2marks/upload_res.html", context)

        
def index(request):
    form = UnitSearchForm(request.GET)
    sem = request.GET.get("sem",'1YEAR') 
    unit = request.GET.get("unit",'UNIT1')
    if unit == 'UNIT3':
        um= Unit3marks.objects.filter(sem=sem).all()
    elif unit == 'UNIT2':
        um= Unit2marks.objects.filter(sem=sem).all()
    else:
        um= Unit1marks.objects.filter(sem=sem).all()
    context = {"um": um} 
    context['form']  = form
    context['unit'] = unit
    context['sem']  = sem
    return render(request, "Unit1marks/index.html", context)

def show(request, spin):
        
    s= Students.objects.get(pin=spin)
    um = s.unit1marks_set.all()
    
    context = {"um" : um }        
        
    return render(request, "Unit1marks/show.html", context)



def edit(request,spin):
    context = {}
    sem = request.GET.get("sem",'1YEAR') 
    unit = request.GET.get("unit",'UNIT1')
    context['unit'] = unit
    context['sem']  = sem
    fs = ""    
    if request.method != 'POST':
        if(unit=="UNIT1"):
            u1m= Unit1marks.objects.filter(sem=sem,student_id=spin).first()
            fs = Unit1marksForm(instance = u1m)
        elif(unit=="UNIT2"):
            u1m= Unit2marks.objects.filter(sem=sem,student_id=spin).first()
            fs = Unit2marksForm(instance = u1m)
        else:
            u1m= Unit3marks.objects.filter(sem=sem,student_id=spin).first()
            fs = Unit3marksForm(instance = u1m)
            
        context["fs"] = fs
        return render(request, "Unit1marks/edit.html", context)  
    else:
        if(unit=="UNIT1"):            
            fs = Unit1marksForm(request.POST)
            fs.save()
        elif(unit=="UNIT2"):            
            fs = Unit2marksForm(request.POST)
            fs.save()
        else:            
            fs = Unit3marksForm(request.POST)
            fs.save()
        return render(request, "Unit1marks/update.html")




def bulkedit(request,spin):
    fs = modelformset_factory(Unit1marks, fields=["s1","s2"])
    context = {}     
    if(request.method == "GET"):                          
        context["fs"] = fs
        return render(request, "Unit1marks/edit.html", context)
    else:
        f = fs(request.POST)
        f.save()
        context["fs"] = fs
        return render(request, "Unit1marks/edit.html", context)
     
            


