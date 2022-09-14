from dataclasses import fields
from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'DepartmentID',
            'DepartmentName',
        )

class EmployeeSerializer(serializers.ModelSerializer)        :
    class Meta:
        model = Employee
        fields = (
            'EmployeeID',
            'EmployeeName',
            'Department',
            'DateJoined',
            'Photo',
        )