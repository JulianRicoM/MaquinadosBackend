from django.http import Http404

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Order, OrderProcess, PaymentMethod, Currency
from .serializer import OrderSerializer, ListOrderSerializer, OrderProcessSerializer, PaymentSerializer
from .serializer import CurrencySerializer


# Only Get Method is allowed, the function will returns a Order list
@api_view(['GET'])
def ListOrder(request):
    queryset = Order.objects.filter(is_active=True)
    serializer = ListOrderSerializer(queryset, many=True)
    return Response(serializer.data)

# only POST method is allowed, the function expects a body of Order type and will create the Order
@api_view(['POST'])
def createOrder(request):
    serializer = OrderSerializer(data=request.data)

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

# If the method is GET, the function expects an id and return an Ordern
# If the method is PUT, the function expect a body of type Order and the Order will be edited
# If the method is DELETE, the function expects an id and delete the Order


@api_view(['GET', 'PUT', 'DELETE'])
def OrderDetail(request, id):
    try:
        order = Order.objects.get(pk=id)
    except Order.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ListOrderSerializer(order, context={'request': request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    if request.method == 'DELETE':
        order.delete()
        return Response(
            {
                'message': 'La order fue eliminada satisfactoriamente'
            },
            status=status.HTTP_204_NO_CONTENT
        )

    if request.method == 'PUT':
        serializer = OrderSerializer(
            order, data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT, data=serializer.data)

        return Response(
            {
                "detail": serializer.errors,
                "data": "Ha ocurrido un error, por favor revise los datos.",
            },
            status=status.HTTP_400_BAD_REQUEST)

# Only the get method is allowed and it returns the list of quotes for a specific client
@api_view(['GET'])
def OrderByClient(request, nit):

    try:
        orders = Order.objects.filter(quote_number__client_id__nit=nit)
    except Order.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = OrderSerializer(
        orders,  context={'request': request}, many=True)
    return Response(status=status.HTTP_200_OK, data=serializer.data)

# Only the get method is allowed and it returns the list of order process
@api_view(['GET'])
def getOrderProcess(request):
    queryset = OrderProcess.objects.all()
    serializer = OrderProcessSerializer(queryset, many = True)
    return Response(serializer.data)
    

@api_view(['GET'])
def PaymentMethods(request):
    queryset = PaymentMethod.objects.all()
    serializer = PaymentSerializer(queryset, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def Currencies(request):
    queryset = Currency.objects.all()
    serializer = CurrencySerializer(queryset, many = True)
    return Response(serializer.data)