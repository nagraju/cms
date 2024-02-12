from django.shortcuts import render
from django.shortcuts import render
from mbts.models import Unit2marks,StudentClass
from django.core.files.storage import FileSystemStorage
from mbts.forms import ClassUnit2marks
from django.forms import modelformset_factory


def upload(request):
    context = {}
    if(request.method == "GET"):       
        
        return render(request, "Unit2marks/upload.html", context)
    else:
        if request.method == 'POST' and request.FILES['csvfile']:
            myfile = request.FILES['csvfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.path(filename)
            Unit2marks.import_csv(uploaded_file_url)
        return render(request, "Unit2marks/upload_res.html", context)

        
def index(request, sem='1'):
    sem = request.GET.get("sem",1)    
    sc = StudentClass.objects.filter(sem=sem)
    if(sc):
         u2m= sc[0].unit2marks_set.all
         context = {"u2m": u2m}        
    else:
        context = {"u2m": []}
    context["sem"] = sem
    return render(request, "Unit2marks/index.html", context)






def show(request, spin):
    s = Unit2marks.objects.get(student=spin)
    context = {"s" : s }
    return render(request, "Unit2marks/show.html", context)

def edit(request,sem):
    context = {}
    u2m= Unit2marks.objects.all
    fs = modelformset_factory(Unit2marks, fields=["pin", "s1","s2"])
    context["fs"] = fs
    return render(request, "Unit2marks/edit.html", context)  


def bulkedit(request,sem):
    fs = modelformset_factory(Unit2marks, fields=["s1","s2"])
    context = {}     
    if(request.method == "GET"):                          
        context["fs"] = fs
        return render(request, "Unit2marks/edit.html", context)
    else:
        f = fs(request.POST)
        f.save()
        context["fs"] = fs
        return render(request, "Unit2marks/edit.html", context)
     
            


