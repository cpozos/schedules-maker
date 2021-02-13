from django.shortcuts import render

from api.models import Subject, Degree
from api.serializers import SubjectSerializer, DegreeSerializer
from rest_framework import viewsets

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class DegreeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer