from django.shortcuts import render
from rest_framework import generics

from .models import Person
from .serializers import PersonSerializer


# Create your views here.
class PersonGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
