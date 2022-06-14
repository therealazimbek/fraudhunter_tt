from django.shortcuts import render

from rest_framework.generics import *
from rest_framework.permissions import *

from .models import Employee
from .serializers import EmployeeSerializer


def hello(request):
    return render(request, 'main.html')


class EmployeesView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]
