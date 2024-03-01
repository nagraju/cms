from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.exceptions  import AuthenticationFailed
from mbts.serializers import StudentsSerializer, MarksSerializer, LoginSerializer
from mbts.models import Students, User
from mbts.models import Students,Attendance,Unit1marks
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([]) 
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


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])    
def student(request):    
    if(request.POST):        
        serializer = StudentsSerializer(data = request.POST)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, satatus =satatus.HTTP_201_CREATED)
    else:
        student = request.user.students
        serializer = StudentsSerializer(student)
        return JsonResponse([serializer.data],safe=False)
        
        
    

def marks(request):    
    s = Students.objects.first()
    marks = s.marks_set.all()
    sub  = []
    for k in marks:
        sub.append(k.to_subjects())
    student_serializer = StudentsSerializer(s)
    marks_serializer = MarksSerializer(marks,many= True)
    return JsonResponse({"students":student_serializer.data, "marks":sub})



class LoginAPI(APIView):
    permission_classes = []
    def post(self,request):
        if ('username' not in request.data) or ('password' not in request.data):
            raise AuthenticationFailed("Empty Username or password")

        username = request.data['username']
        password = request.data['password']
        
        
        user = authenticate(request, username=username, password=password)
        if(user is None):
            raise AuthenticationFailed("User not Found")
        
        refresh = RefreshToken.for_user(user)
             
        return JsonResponse({"refresh":str(refresh),
                             'access': str(refresh.access_token)
                             })
        

