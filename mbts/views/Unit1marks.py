from django.shortcuts import render
from django.shortcuts import render
from mbts.models import Unit1marks
from django.core.files.storage import FileSystemStorage


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


def index(request):
    atte = Unit1marks.objects.all
    context = {"Unit1marks": Unit1marks}
    return render(request, "Unit1marks/index.html", context)
