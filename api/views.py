from django.shortcuts import render

from rest_framework.generics import *
from rest_framework.permissions import *

from .models import Employee
from .serializers import EmployeeSerializer, EmployeeCreateSerializer


def hello(request):
    return render(request, 'main.html')


class EmployeesView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = [EmployeeSerializer, EmployeeCreateSerializer]
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeSerializer
        elif self.request.method == 'POST':
            return EmployeeCreateSerializer


class EmployeeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    permission_classes = [AllowAny]
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
