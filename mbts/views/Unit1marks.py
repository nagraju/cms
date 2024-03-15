from django.shortcuts import render
from django.shortcuts import render
from mbts.models import Unit1marks,StudentClass, Unit2marks, Unit3marks
from django.core.files.storage import FileSystemStorage
from mbts.forms import ClassUnit1marks, UnitSearchForm
from django.forms import modelformset_factory


def upload(request):
    context = {}
    if(request.method == "GET"): 
        form = UnitSearchForm(request.GET)   
        sem = request.GET.get("sem",'1YEAR') 
        unit = request.GET.get("unit",'1UNIT') 
        
        return render(request, "Unit1marks/upload.html", context)
    else:
        if request.method == 'POST' and request.FILES['csvfile']:
            form = UnitSearchForm(request.GET)   
            sem = request.GET.get("sem",'1YEAR') 
            unit = request.GET.get("unit",'1UNIT') 
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
    unit = request.GET.get("unit",'1UNIT')
    if unit == 'UNIT3':
        um= Unit3marks.objects.filter(sem=sem).all()
    elif unit == 'UNIT2':
        um= Unit2marks.objects.filter(sem=sem).all()
    else:
        um= Unit1marks.objects.filter(sem=sem).all()
    context = {"um": um} 
    context['form']  = form
    context['unit'] = unit
    return render(request, "Unit1marks/index.html", context)

def show(request, sem):
    sem = request.GET.get("sem",'1YEAR') 
    unit = request.GET.get("unit",'1UNIT')
    if unit == 'UNIT3':
        um= Unit3marks.objects.filter(sem=sem).all()
    elif unit == 'UNIT2':
        um= Unit2marks.objects.filter(sem=sem).all()
    else:
        um= Unit1marks.objects.filter(sem=sem).all()
        context = {"um" : um }
        context['form']  = form
        context['unit'] = unit
    return render(request, "Unit1marks/show.html", context)



def edit(request,sem):
    context = {}
    u1m= Unit1marks.objects.all
    fs = modelformset_factory(Unit1marks, fields=["pin", "s1","s2"])
    context["fs"] = fs
    return render(request, "Unit1marks/edit.html", context)  


def bulkedit(request,sem):
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
     
            


