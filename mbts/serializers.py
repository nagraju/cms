from mbts.models import User, Students, Marks
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', "password", "students"]


class StudentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Students
        fields = ['pin',"sname","sem"]

class MarksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marks
        fields = ['s1', "s1i",  "s1e", "s1t", "s1s", "s2", "s2i", "s2e", "s2t", "s2s"]

class LoginSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
