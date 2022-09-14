from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 
#allows other domains to access our project
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *


@csrf_exempt
def department(request, id=0):
    if request.method == 'GET':
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializer(
            departments, many=True
            )
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)

        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('Added successfully', safe=False)
        return JsonResponse('failed to add ', safe=False)

    elif request.method == 'PUT': #used to update existing record
        department_data = JSONParser().parse(request)
        department = Department.objects.get(
            DepartmentID=department_data['DepartmentID'])
        department_serializer = DepartmentSerializer(
            department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('Update successful', safe=False)

    elif request.method == 'DELETE': #used to DELETE existing record
        department = Department.objects.get(DepartmentID=id)
        department.delete()
        return JsonResponse('Delete sucessful', safe=False)
