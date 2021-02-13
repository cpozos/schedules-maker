from django.shortcuts import render

from api.models import Subject
from api.serializers import SubjectSerializer
from rest_framework import viewsets

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer