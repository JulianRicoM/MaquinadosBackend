from django.http import Http404

from rest_framework import generics
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Quote
from .serializer import QuoteSerializer

# If the method is POST, the class expects a body of type Quote and will create the Quote 
# If the method is GET the function will return a Quote list 
class QuoteList(generics.ListCreateAPIView):
    serializer_class =  QuoteSerializer
    queryset = Quote.objects.filter(is_active = True)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = QuoteSerializer(queryset, many = True)
        return Response(serializer.data)

# If the method is GET, the function expects an id and return a Quote 
# If the method is PUT, the function expect a body of type Quote and the Quote will be edited 
@api_view(['GET', 'PUT'])
def QuoteDetails(request, id):
    try:
        quote = Quote.objects.get(pk = id)
    except Quote.DoesNotExist as e:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = QuoteSerializer(quote, context = {'request': request})
        return Response(status = status.HTTP_200_OK, data = serializer.data, context = {'request': request})
    
    if request.method == 'PUT':
        serializer = QuoteSerializer(quote, data = request.data, context = {'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_204_NO_CONTENT, data = serializer.data)

# Only the get method is allowed and it returns the list of quotes for a specific client        
@api_view(['GET'])
def QuoteByClient(request, nit):
    try:
        quotes = Quote.objects.filter(nit = nit)
    except Quote.DoesNotExist as e:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serialiser = QuoteSerializer(quotes, many = True)