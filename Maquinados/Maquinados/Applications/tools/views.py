from django.http import Http404

from rest_framework import generics
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Tools, StatusTools
from .serializer import ToolsSerializer, StatusToolSerializer

# If the method is POST, the class expects a body of type Tool and will create the Tool 
# If the method is GET the function will return a Tool list 
class ToolList(generics.ListCreateAPIView):
    serializer_class = ToolsSerializer
    queryset = Tools.objects.filter(is_active = True)
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ToolsSerializer(queryset, many = True)
        return Response(serializer.data)
    

class Status(generics.ListCreateAPIView):
    serializer_class = StatusToolSerializer
    queryset = StatusTools.objects.all()
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = StatusToolSerializer(queryset, many = True)
        return Response(serializer.data)

# If the method is GET, the function expects an id and return a Tool 
# If the method is PUT, the function expect a body of type Tool and the Tool will be edited
@api_view(['GET', 'PUT', 'DELETE'])
def ToolDetails(request, id):
    try:
        tool = Tools.objects.get(pk = id)
    except Tools.DoesNotExist as e:
        return Response(status =  status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ToolsSerializer(tool, context = {'request': request})
        return Response(status = status.HTTP_200_OK, data = serializer.data)
    
    if request.method == 'PUT':
        serializer = ToolsSerializer(tool, data = request.data, context = {'request': request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_204_NO_CONTENT, data = serializer.data)
        
    if request.method == 'DELETE':
        tool.delete()
        return Response(
            {"message": "La herramienta fue eliminada satisfactoriamente"},
            status=status.HTTP_204_NO_CONTENT)