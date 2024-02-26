from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from mbts.serializers import StudentsSerializer
from mbts.models import Students, User
from mbts.models import Students,Attendance,Unit1marks

@api_view(['GET', 'POST'])
def students(request):
    
    if(request.POST):
        serializer = StudentsSerializer(data = request.POST)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, satatus =satatus.HTTP_201_CREATED)
    else:
        s = Students.objects.all()
        serializer = StudentsSerializer(s, many= True)
        return JsonResponse({"students":serializer.data})
    
def student(request):    
    if(request.POST):
        serializer = StudentsSerializer(data = request.POST)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, satatus =satatus.HTTP_201_CREATED)
    else:
        s = Students.objects.first()
        serializer = StudentsSerializer(s)
        return JsonResponse(serializer.data)
