from multiprocessing import context
from django.http import Http404

from rest_framework import generics
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Item
from .serializer import ItemSerializer

""" If the method is POST, the class expects a body of type Client and will create the client """
""" If the method is GET the function will return a clients list """
class ItemList(generics.ListCreateAPIView):
    serializer_class =  ItemSerializer
    queryset = Item.objects.filter(is_active = True)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many = True)
        return Response(serializer.data)

""" If the method is GET, the function expects an id and return a Client """
""" If the method is PUT, the function expect a body of type Client and the client will be edited """
@api_view(['GET', 'PUT'])
def ItemDetails(request, id):
    try:
        item =  Item.objects.get(pk = id)
    except Item.DoesNotExist as e:
        return Response( status = status.HTTP_404_NOT_FOUND, data = e.error)
    
    if request.method == 'GET':
        serializer = ItemSerializer(item, context = {'request': request})
        return Response(status = status.HTTP_200_OK, data = serializer.data)
    
    if request.method == 'PUT':
        serializer = ItemSerializer(item, data = request.data, context = {'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_204_NO_CONTENT, data = serializer.data)