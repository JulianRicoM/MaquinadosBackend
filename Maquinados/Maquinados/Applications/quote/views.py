from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Quote, StatusQuote
from .serializer import QuoteSerializer, StatusQuoteSerializer, ListQuoteSerializer


# Only Get Method is allowed, the function will returns a Quote list
@api_view(['GET'])
def ListQuote(request):
    queryset = Quote.objects.filter(is_active=True)
    serializer = ListQuoteSerializer(queryset, many=True)
    return Response(serializer.data)

# Only POST method is allowed, the function expects a body of Quote type and will create the Quote
@api_view(['POST'])
def CreateQuote(request):
    serializer = QuoteSerializer(data=request.data)

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

# If the method is GET, the function expects an id and returns a Quote
# If the method is PUT, the function expects a body of type Quote and the Quote will be edited
# if the method is DELETE, the function an id and delete the Quote


@api_view(['GET', 'PUT', 'DELETE'])
def QuoteDetails(request, id):
    try:
        quote = Quote.objects.get(pk=id)
    except Quote.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ListQuoteSerializer(quote, context={'request': request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    if request.method == 'DELETE':
        quote.delete()
        return Response(
            {"message": "La cotización fue eliminada satisfactoriamente"},
            status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        serializer = QuoteSerializer(
            quote, data=request.data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(
            {
                "detail": serializer.errors,
                "data": "Ha ocurrido un error, por favor revise los datos.",
            },
            status=status.HTTP_400_BAD_REQUEST)

# Only the GET method is allowed and it returns the quote list for a specific client


@api_view(['GET'])
def QuoteByClient(request, nit):

    try:
        quotes = Quote.objects.filter(client_id__nit=nit)
    except Quote.DoesNotExist as e:
        return Response(status=status.HTTP_404_NOT_FOUND,)

    serializer = QuoteSerializer(
        quotes,  context={'request': request}, many=True)
    return Response(status=status.HTTP_200_OK, data=serializer.data)

# If the method is GET, the function returns a status quote list
# If the method is POST, the function expects a body of Status Quote type and will create the Status Quote


class StatusQuoteList(generics.ListCreateAPIView):
    serializer_class = StatusQuoteSerializer
    queryset = StatusQuote.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = StatusQuoteSerializer(queryset, many=True)
        return Response(serializer.data)
