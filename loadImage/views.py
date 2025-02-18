from django.shortcuts import render
from .serializer import LoadImageSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from .serializer import TextSerializer
from .models import Text
from scripts import downloadImage, main
import asyncio
import shutil
import os
from django.conf import settings
from django.http import FileResponse

class LoadAPIView(APIView):

    # queryset = Text.objects.all()
    # serializer_class = TextSerializer

    def post(self,request):
        data = self.request.data

        serializers =LoadImageSerializer(data=data)
        
        if serializers.is_valid():
            
            url = serializers.validated_data.get('url')
            # Fonction pour suprimer ou crée en fonction du presence d'un fichier
            downloadImage.control()
            # fonction asynchrone
            asyncio.run(downloadImage.main(url))

            # Chemin du fichier qui contient les images
            #image_path = os.path.abspath("images")
            image_path = os.path.join(settings.MEDIA_ROOT,"images" )

            # Zip name
            zip_filename = "images.zip"
            # Où stocker le fichier zip
            zip_path = os.path.join(settings.MEDIA_ROOT, zip_filename)
            # Transformer un dossier en zip
            shutil.make_archive(zip_path.replace('.zip',''), 'zip', image_path)
            return FileResponse(open(zip_path,"rb"), as_attachment=True, filename=zip_filename)
            # return Response({'status':"reussi"}, status=status.HTTP_200_OK)
        else:

            return Response({"error":"Data is not succes"},status=status.HTTP_400_BAD_REQUEST)