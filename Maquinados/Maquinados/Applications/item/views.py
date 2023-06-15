
from django.http import Http404

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








        