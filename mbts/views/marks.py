from django.shortcuts import render
from django.shortcuts import render
from mbts.models import Marks
from django.core.files.storage import FileSystemStorage


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


def index(request):
    Marks= Marks.objects.all
    context = {"Marks": Marks}
    return render(request, "Marks/index.html", context)

