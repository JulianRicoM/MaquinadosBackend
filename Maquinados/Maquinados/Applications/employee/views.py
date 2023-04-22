from django.http import Http404

from rest_framework import generics
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Employee, Eps, Position
from .serializer import EmployeeSerializer, EPSSerializer, EmployeeListSerializer, PositionSerializer


# Oonly POST method is allowed, the function expects a body of Employee type and will create the Employee
@api_view(['POST'])
def CreateEmployee(request):
    serializer = EmployeeSerializer(data = request.data)
    queryset = Employee.objects.filter(is_active = True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    return Response(
        {
            "detail": serializer.errors,
            "data": "Ha ocurrido un error, por favor revise los datos.",
        },
        status=status.HTTP_400_BAD_REQUEST,
    )
    
    
# Only Get Method is allowed, the function will returns an Employee list
@api_view(['GET'])
def EmployeeList(request):
    queryset = Employee.objects.filter(is_active=True)
    serializer = EmployeeListSerializer(queryset, many=True)
    return Response(serializer.data)


# If the method is POST, the class expects a body of type EPS and will create the EPS 
# If the method is GET the function will return an EPS list
class EPSList(generics.ListCreateAPIView):
    serializer_class = EPSSerializer
    queryset = Eps.objects.all()
    
    def List(self, request):
        queryset =  self.get_queryset()
        serializer = Eps(queryset, many = True)
        return Response(serializer.data)
    
# If the method is GET, the function expects an id and return a Employee
# If the method is PUT, the function expect a body of type Employee and the Employee will be edited 
@api_view(['GET', 'PUT','DELETE'])
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

    if request.method == 'DELETE':
            employee.delete()
            return Response(
                {
                    'message': 'El cliente fue eliminado satisfactoriamente'
                },
                status=status.HTTP_204_NO_CONTENT
            )        
        
# If the method is POST, the class expects a body of type Position and will create the Position  
# If the method is GET the function will return an Position list
class PositionList(generics.ListCreateAPIView):
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    
    def List(self, request):
        queryset =  self.get_queryset()
        serializer = Position(queryset, many = True)
        return Response(serializer.data)