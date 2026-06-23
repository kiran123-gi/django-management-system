from django.shortcuts import render
from rest_framework import viewsets
from .models import employess
from .serialization import employeeSerializers

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employess.objects.all()
    serializer_class = employeeSerializers
