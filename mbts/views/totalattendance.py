from django.shortcuts import render
from mbts.models import Students, TotalAttendance
from mbts.forms import SemSearchForm
from django.contrib.auth.decorators import login_required




def index(request):
    sem = request.GET.get("sem","1YEAR")
    totalAttendance = TotalAttendance.objects.filter(sem=sem)
    context = {}
    context["totalAttendance"] = totalAttendance
    context["semform"] = SemSearchForm({"sem":sem})
    return render(request, "totalattendance/index.html", context)

    
