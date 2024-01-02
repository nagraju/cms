from django.shortcuts import render
from django.shortcuts import render
from mbts.forms import StudentForm
from mbts.models import Students


def index(request):
    sl = Students.objects.all
    context = {"sl": sl}
    return render(request, "students/index.html", context)


# Create your views here.
def newst(request):
    context = {}
    if(request.method == "GET"):       
        context['forms'] = StudentForm()
        return render(request, "students/newst.html", context)
    else:
        sf = StudentForm(request.POST)
        sf.is_valid()     
        s = sf.save()
        context['s'] = s
        return render(request, "students/show.html", context)

def show(request, spin):
    s = Students.objects.get(pin=spin)
    context = {"s" : s }
    return render(request, "students/show.html", context)
    
   

def edit(request, spin):
    context = {}
    s = Students.objects.get(pin=spin)
    if(request.method == "GET"):    
        sf = StudentForm(instance=s)
        context['forms'] = sf
        return render(request, "students/edit.html",context)
    else:
        sf = StudentForm(request.POST, instance=s )
        sf.is_valid()     
        s = sf.save()
        context['s'] = s
        return render(request, "students/show.html", context)

def delete(request, spin):
    return render(request, "students/delete.html")
