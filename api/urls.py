from django.urls import path
from .views import *

urlpatterns = [
    path('', hello),
    path('employees/', EmployeesView.as_view())
]