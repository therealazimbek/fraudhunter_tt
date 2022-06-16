import django_filters
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes

from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework import filters

from .models import Employee
from .serializers import EmployeeSerializer, EmployeeCreateSerializer, UserSerializer, UserRegisterSerializer


def hello(request):
    return HttpResponse("Welcome to Employee Database " + "<a href='http://127.0.0.1:8000/api/employees'>Go to "
                                                          "database</a>")


class EmployeesView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = [EmployeeSerializer, EmployeeCreateSerializer]
    permission_classes = [IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['firstname', 'middlename', 'lastname', 'position', 'joined_date', 'salary']
    search_fields = ['firstname', 'middlename', 'lastname']
    ordering_fields = ['firstname', 'middlename', 'lastname', 'position', 'joined_date', 'salary', 'supervisor']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeSerializer
        elif self.request.method == 'POST':
            return EmployeeCreateSerializer


# class EmployeeDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = [EmployeeSerializer, EmployeeCreateSerializer]
#     lookup_field = 'pk'
#
#     def get_serializer_class(self):
#         if self.request.method == 'GET' or self.request.method == 'DELETE':
#             return EmployeeSerializer
#         elif self.request.method == 'PUT':
#             return EmployeeCreateSerializer


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def employee_detail(request, pk):
    try:
        employee = Employee.objects.get(id=pk)
    except Employee.DoesNotExist as e:
        return Response({'message': str(e)}, status=404)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmployeeCreateSerializer(instance=employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        employee.delete()
        return Response({'message': 'deleted'}, status=204)


class UsersView(ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    serializer_classes = [UserSerializer, UserRegisterSerializer]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        elif self.request.method == 'POST':
            return UserRegisterSerializer


# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
# def employee_list(request):
#     if request.method == 'GET':
#         employees = Employee.objects.all()
#         paginator = Paginator(employees, 25)  # Show 25 employees per page.
#
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         return render(request, 'api/employees_list.html', {'page_obj': page_obj})
#
#     elif request.method == 'POST':
#         serializer = EmployeeCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


