import os
import base64
from django.http import Http404
from PIL import Image

from rest_framework import generics
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Item, Material, Measurement_units
from .serializer import ItemSerializer, MaterialSerializer, MeasurementSerializer

""" If the method is POST, the class expects a body of type Item and will create the Item """
""" If the method is GET the function will return a Item list """
class ItemList(generics.ListCreateAPIView):
    serializer_class =  ItemSerializer
    queryset = Item.objects.filter(is_active = True)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ItemSerializer(queryset, many = True)
        
        data = serializer.data
        newPath = os.path.abspath(".")
        current_path = newPath.replace(os.sep, "/")
        
        for item in data:     
            if 'http://localhost:8000/' in item['plane']:
                item['plane'].replace('http://localhost:8000/', '')
            
            image_path = f"{current_path}{item['plane']}"  # Replace with the actual image path 
            print(image_path)
            image_data = open(image_path, 'rb').read()
            base64_image = base64.b64encode(image_data).decode('UTF-8')    
            item['plane_base64'] = f'data:image/png;base64,{base64_image}'
            print(item['plane_base64'])
        
        return Response(serializer.data)
    

class MaterialList(generics.ListAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = MaterialSerializer(queryset, many = True)
        return Response(serializer.data)
    

class Measurement(generics.ListAPIView):    
    serializer_class = MeasurementSerializer
    queryset = Measurement_units.objects.all()
    
    def List(self, request): 
        queryset = self.get_queryset()
        serializer = MeasurementSerializer(queryset, many = True)
        return Response(serializer.data)


""" If the method is GET, the function expects an id and return a Item """
""" If the method is PUT, the function expect a body of type Item and the Item will be edited """
@api_view(['GET', 'PUT', 'DELETE'])
def ItemDetails(request, id):
    try:
        item =  Item.objects.get(pk = id)
    except Item.DoesNotExist as e:
        return Response( status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ItemSerializer(item, context = {'request': request})
        return Response(status = status.HTTP_200_OK, data = serializer.data)
    
    if request.method == 'DELETE':
        item.delete()
        return Response(
            {
                'message': 'El cliente fue eliminado satisfactoriamente'
            },
            status=status.HTTP_204_NO_CONTENT
        )
    
    if request.method == 'PUT':
        serializer = ItemSerializer(item, data = request.data, context = {'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_204_NO_CONTENT, data = serializer.data)
        
        return Response(
            {
                "detail": serializer.errors,
                "data": "Ha ocurrido un error, por favor revise los datos.",
            },
            status=status.HTTP_400_BAD_REQUEST) 








        