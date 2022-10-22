from django.http import Http404

from rest_framework import generics
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Client
from .serializer import ClientSerializer

""" If the method is POST, the class expects a body of type Client and will create the client """
""" If the method is GET the function will return a clients list """
class ClientList(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.filter(is_active = True)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ClientSerializer(queryset, many = True)
        return Response(serializer.data)

""" If the method is GET, the function expects an id and return a Client """
""" If the method is PUT, the function expect a body of type Client and the client will be edited """
@api_view(['GET', 'PUT'])
def ClientDetail(request, id):
    try:
        client = Client.objects.get(pk = id)
    except Client.DoesNotExist as e:
        return Response(status = status.HTTP_404_NOT_FOUND, data = e.errors)
    
    if request.method == 'GET':
        serializer = ClientSerializer(client, context = {"request": request})
        return Response(status = status.HTTP_200_OK, data = serializer.data)
    
    if request.method == 'PUT':
        serializer = ClientSerializer(client, data = request.data, context = {'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_204_NO_CONTENT, data = serializer.data)