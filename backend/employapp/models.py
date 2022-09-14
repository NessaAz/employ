from django.db import models

class Department(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=200)

class Employee(models.Model)    :
    EmployeeID = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=200)
    Department = models.CharField(max_length=200)
    DateJoined = models.DateField()
    Photo = models.CharField(max_length=200)