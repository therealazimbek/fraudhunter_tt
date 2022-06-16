from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair
from .views import *

urlpatterns = [
    path('', hello),
    path('employees/', EmployeesView.as_view()),
    # path('employees/', employee_list),
    # path('employees/<int:pk>/', EmployeeDetailView.as_view()),
    path('employees/<int:pk>/', employee_detail),

    path('login/', token_obtain_pair),
    path('users/', UsersView.as_view()),
]