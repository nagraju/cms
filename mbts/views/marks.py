
from django.shortcuts import render
from mbts.models import Marks
from django.core.files.storage import FileSystemStorage
from mbts.models import Marks,StudentClass
from mbts.forms import ClassMarks
from django.forms import modelformset_factory



def index(request, sem='1'):
    sem = request.GET.get("sem",1)    
    sc = StudentClass.objects.filter(sem=sem)
    if(sc):
         u1m= sc[0].Marks_set.all
         context = {"m": m}        
    else:
        context = {"m": []}
    context["sem"] = sem
    return render(request, "Marks/index.html", context)


def upload(request):
    context = {}
    if(request.method == "GET"):       
        
        return render(request, "Marks/upload.html", context)
    else:
        if request.method == 'POST' and request.FILES['csvfile']:
            myfile = request.FILES['csvfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.path(filename)
            Marks.import_csv(uploaded_file_url)
        return render(request, "Marks/upload_res.html", context)



def show(request, spin):
    s =Marks.objects.get(student=spin)
    context = {"s" : s }
    return render(request, "Marks/show.html", context)

def edit(request,sem):
    context = {}
    m= Marks.objects.all
    fs = modelformset_factory(Marks, fields=["pin", "s1","s2"])
    context["fs"] = fs
    return render(request, "Marks/edit.html", context)  


def bulkedit(request,sem):
    fs = modelformset_factory(Marks, fields=["s1","s2"])
    context = {}     
    if(request.method == "GET"):                          
        context["fs"] = fs
        return render(request, "Marks/edit.html", context)
    else:
        f = fs(request.POST)
        f.save()
        context["fs"] = fs
        return render(request, "Marks/edit.html", context)
     
            






