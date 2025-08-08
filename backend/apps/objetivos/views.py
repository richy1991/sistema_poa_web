from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ObjetivoEspecifico
from .serializers import ObjetivoEspecificoSerializer

class ObjetivoListCreateView(APIView):
    def get(self, request):
        objetivos = ObjetivoEspecifico.objects.all()
        serializer = ObjetivoEspecificoSerializer(objetivos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ObjetivoEspecificoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ObjetivoDetailView(APIView):
    def get_object(self, pk):
        try:
            return ObjetivoEspecifico.objects.get(pk=pk)
        except ObjetivoEspecifico.DoesNotExist:
            return None

    def get(self, request, pk):
        objetivo = self.get_object(pk)
        if objetivo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ObjetivoEspecificoSerializer(objetivo)
        return Response(serializer.data)

    def put(self, request, pk):
        objetivo = self.get_object(pk)
        if objetivo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ObjetivoEspecificoSerializer(objetivo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        objetivo = self.get_object(pk)
        if objetivo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        objetivo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
