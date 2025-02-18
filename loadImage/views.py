from django.shortcuts import render
from .serializer import LoadImageSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from .serializer import TextSerializer
from .models import Text
from scripts.downloadImage import main
import asyncio

class LoadAPIView(APIView):

    # queryset = Text.objects.all()
    # serializer_class = TextSerializer

    async def post(self,request):
        data = self.request.data

        serializers =LoadImageSerializer(data=data)
        
        if serializers.is_valid():
            
            url = serializers.validated_data.get('url')
            await main(url)

            return Response({'status':"reussi"}, status=status.HTTP_200_OK)
        else:

            return Response({"error":"Data is not succes"},status=status.HTTP_400_BAD_REQUEST)