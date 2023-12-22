from django.shortcuts import render
from django.shortcuts import render

from mbts.models import Attendance
from django.core.files.storage import FileSystemStorage


def upload(request):
    context = {}
    if(request.method == "GET"):       
        
        return render(request, "attendance/upload.html", context)
    else:
        if request.method == 'POST' and request.FILES['csvfile']:
            myfile = request.FILES['csvfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.path(filename)
            Attendance.import_csv(uploaded_file_url)
        return render(request, "attendance/upload_res.html", context)


def index(request):
    atte = Attendance.objects.all
    context = {"atte": atte}
    return render(request, "attendance/index.html", context)




