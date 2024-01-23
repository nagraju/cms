from django.shortcuts import render
from django.shortcuts import render
from mbts.models import Unit1marks,StudentClass
from django.core.files.storage import FileSystemStorage
from mbts.forms import ClassUnit1marks
from django.forms import modelformset_factory


def upload(request):
    context = {}
    if(request.method == "GET"):       
        
        return render(request, "Unit1marks/upload.html", context)
    else:
        if request.method == 'POST' and request.FILES['csvfile']:
            myfile = request.FILES['csvfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.path(filename)
            Unit1marks.import_csv(uploaded_file_url)
        return render(request, "Unit1marks/upload_res.html", context)

        
def index(request, sem='1'):
    sem = request.GET.get("sem",1)    
    sc = StudentClass.objects.filter(sem=sem)
    if(sc):
         u1m= sc[0].Unit1marks_set.all
         context = {"u1m": u1m}        
    else:
        context = {"u1m": []}
    context["sem"] = sem
    return render(request, "Unit1marks/index.html", context)






def show(request, student):
    s = Unit1marks.objects.get(student=student)
    context = {"s" : s }
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
     
            


