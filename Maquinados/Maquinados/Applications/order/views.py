from django.http import Http404

from rest_framework import generics
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Order
from .serializer import OrderSerializer

# If the method is POST, the class expects a body of type Order and will create the Order 
# If the method is GET the function will return a Order list 
class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.filter(is_active = True)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = OrderSerializer(queryset, many = True)
        return Response(serializer.data)

# If the method is GET, the function expects an id and return an Ordern 
# If the method is PUT, the function expect a body of type Order and the Order will be edited
@api_view(['GET', 'PUT'])
def OrderDetail(request, id):
    try:
        order = Order.objects.get(pk = id)
    except Order.DoesNotExist as e:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = OrderSerializer(order, context = {'request': request})
        return Response(status = status.HTTP_200_OK, data = serializer.data, context = {'request': request})
    
    if request.method == 'PUT':
        serializer = OrderSerializer(order, data = request.data, context = {'request': request})
        
        if serializer.is_valid():
            return Response(status = status.HTTP_204_NO_CONTENT, data = serializer.data)

# Only the get method is allowed and it returns the list of quotes for a specific client        
@api_view(['GET'])
def OrderByClient(request, nit):
        
    try:
        orders = Order.objects.filter(quote_number__client_id__nit = nit)
    except Order.DoesNotExist as e:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer = OrderSerializer(orders,  context = {'request': request}, many = True)
    return Response(status = status.HTTP_200_OK, data = serializer.data)