from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeCreateSerializer(serializers.ModelSerializer):

    supervisor = EmployeeSerializer(read_only=True)
    supervisor_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
