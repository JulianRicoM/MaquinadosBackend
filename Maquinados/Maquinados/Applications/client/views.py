from django.http import Http404

from rest_framework import generics
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Client, Country, Department, City
from .serializer import ClientSerializer, CountriesSerializer, CitiesSerializer, DepartmentSerializer

# If the method is POST, the class expects a body of type Client and will create the client 
# If the method is GET the function will return a clients list 
class ClientList(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.filter(is_active = True)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ClientSerializer(queryset, many = True)
        return Response(serializer.data)

# If the method is GET, the function expects an id and return a Client
# If the method is PUT, the function expects a body of type Client and the client will be edited
# If the method is Delete, the functions expects an id and delete the Client
@api_view(['GET', 'PUT'])
def ClientDetail(request, id):
    try:
        client = Client.objects.get(pk = id)
    except Client.DoesNotExist as e:
        return Response(status = status.HTTP_404_NOT_FOUND, data = e.errors)
    
    if request.method == 'GET':
        serializer = ClientSerializer(client, context = {"request": request})
        return Response(status = status.HTTP_200_OK, data = serializer.data)
    
    if request.method == 'DELETE':
        client.delete()
        return Response(
            {
                'message': 'El cliente fue eliminado satisfactoriamente'
            },
            status=status.HTTP_204_NO_CONTENT
        )
    
    if request.method == 'PUT':
        serializer = ClientSerializer(client, data = request.data, context = {'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_204_NO_CONTENT, data = serializer.data)
        
        return Response(
            {
                "detail": serializer.errors,
                "data": "Ha ocurrido un error, por favor revise los datos.",
            },
            status=status.HTTP_400_BAD_REQUEST)

# If the method is POST, the class expects a body of type Country and will create the Country
# If the method is GET, the function will return a Country list
class CountriesList(generics.ListCreateAPIView):
    serializer_class = CountriesSerializer
    queryset = Country.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = CountriesSerializer(queryset, many = True)
        return Response(serializer.data)
    
# If the method is POST, the class expects a body of type City and will create the City
# If the method is GET, the function will return a Cities list
class CitiesList(generics.ListCreateAPIView):
    serializer_class = CitiesSerializer
    queryset = Country.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = CitiesSerializer(queryset, many = True)
        return Response(serializer.data)

# If the method is POST, the class expects a body of type Department and will create the City
# If the method is GET, the function will return a Departmens list
class DepartmentList(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = DepartmentSerializer(queryset, many = True)
        return Response(serializer.data)

# Only Get method is allowed, the function expects an id and return a Deparments list
@api_view(['GET'])
def DepartmentByCountry(request, id):
    queryset = Department.objects.filter(country = id)
    serializer = DepartmentSerializer(queryset, many = True)
    return Response(serializer.data)

# Only Get method is allowed, the function expects an id and return a Cities list
@api_view(['GET'])
def CitiesByDeparment(request, id):
    queryset = City.objects.filter(department = id)
    serializer = CitiesSerializer(queryset, many = True)
    return Response(serializer.data)
