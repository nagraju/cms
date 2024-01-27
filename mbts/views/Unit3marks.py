from django.shortcuts import render
from django.shortcuts import render
from mbts.models import Unit3marks,StudentClass
from django.core.files.storage import FileSystemStorage
from mbts.forms import ClassUnit3marks
from django.forms import modelformset_factory


def upload(request):
    context = {}
    if(request.method == "GET"):       
        
        return render(request, "Unit3marks/upload.html", context)
    else:
        if request.method == 'POST' and request.FILES['csvfile']:
            myfile = request.FILES['csvfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.path(filename)
            Unit2marks.import_csv(uploaded_file_url)
        return render(request, "Unit3marks/upload_res.html", context)

        
def index(request, sem='1'):
    sem = request.GET.get("sem",1)    
    sc = StudentClass.objects.filter(sem=sem)
    if(sc):
         u2m= sc[0].unit3marks_set.all
         context = {"u3m": u3m}        
    else:
        context = {"u3m": []}
    context["sem"] = sem
    return render(request, "Unit3marks/index.html", context)






def show(request, spin):
    s = Unit3marks.objects.get(student=spin)
    context = {"s" : s }
    return render(request, "Unit3marks/show.html", context)

def edit(request,sem):
    context = {}
    u2m= Unit3marks.objects.all
    fs = modelformset_factory(Unit2marks, fields=["pin", "s1","s2"])
    context["fs"] = fs
    return render(request, "Unit3marks/edit.html", context)  


def bulkedit(request,sem):
    fs = modelformset_factory(Unit3marks, fields=["s1","s2"])
    context = {}     
    if(request.method == "GET"):                          
        context["fs"] = fs
        return render(request, "Unit3marks/edit.html", context)
    else:
        f = fs(request.POST)
        f.save()
        context["fs"] = fs
        return render(request, "Unit3marks/edit.html", context)
     
            


