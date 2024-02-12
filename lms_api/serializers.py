from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Person, Task, Result, Course


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
