from django.http import Http404

from rest_framework import generics
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Employee, Eps
from .serializer import EmployeeSerializer, EPSSerializer

""" If the method is POST, the class expects a body of type Employee and will create the Employee """
""" If the method is GET the function will return a Employee list """
class EmployeeList(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter(is_active = True)
    
    def List(self, request):
        queryset =  self.get_queryset()
        serializer = EmployeeSerializer(queryset, many = True)
        return Response(serializer.data)
    
class EPSList(generics.ListCreateAPIView):
    serializer_class = EPSSerializer
    queryset = Eps.objects.all()
    
    def List(self, request):
        queryset =  self.get_queryset()
        serializer = Eps(queryset, many = True)
        return Response(serializer.data)
    
""" If the method is GET, the function expects an id and return a Employee """
""" If the method is PUT, the function expect a body of type Employee and the Employee will be edited """
@api_view(['GET', 'PUT'])
def EmployeeDetails(request, id):
    try:
        employee = Employee.objects.get(pk = id)
    except Employee.DoesNotExist as e:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee, context = {'request': request})
        return Response(status =  status.HTTP_200_OK, data = serializer.data)
    
    if request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data = request.data, context = {'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_204_NO_CONTENT, data = serializer.data)