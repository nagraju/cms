from mbts.models import User, Students, Marks
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', "students"]



class StudentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Students
        fields = ['pin','email',"sname","sem"]


class LoginStudentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('_username')
    role = serializers.SerializerMethodField('_role')

    def _username(self,context):
        return self.context.get('username')       
    def _role(self,context):
        return self.context.get('role')  
    class Meta:
        model = Students
        fields = ['pin', 'email','sname','sem', 'username', 'role']

class MarksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marks
        fields = ['s1', "s1i",  "s1e", "s1t", "s1s", "s2", "s2i", "s2e", "s2t", "s2s"]

class LoginSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
