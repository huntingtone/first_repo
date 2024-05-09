from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Automobile, Parts, PartFile
from .serializers import AutomobileSerializer, PartsSerializer, PartFileSerializer
from django.core.files.storage import FileSystemStorage
import os



# Create your views here.


class AutomobileListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        auto = Automobile.objects.filter(user=request.user.id)
        serializer = AutomobileSerializer(auto, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'manufacturer': request.data.get('manufacturer'),
            'tipe': request.data.get('tipe'),
            'modl': request.data.get('modl'),
            'user': request.user.id
        }
        serializer = AutomobileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PartsListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        # self.request = request
        # automobile = self.get_queryset()
        manufacturer = self.request.query_params.get('manufacturer')
        if manufacturer is None:
            manufacturer = ''
        parts = Parts.objects.filter(autom__manufacturer__contains=manufacturer)
        serializer = PartsSerializer(parts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'name': request.data.get('name'),
            'autom': request.data.get('autom'),
        }
        serializer = PartsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileUploadView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, )

    def post(self, request, format=None):
        '''
        to check this one you can enjoy some curl like below:
        curl -X POST -H "Content-Type:multipart/form-data" -u admin:user -F "file=@/Users/sayedmohmmadrazavi/Desktop/photo.jpg" http://127.0.0.1:8000/autos/upload?parts=1
        '''
        parts = request.query_params.get('parts')
        if parts:
            file_obj = request.FILES['file']

            tmp_address = os.path.join(f'media/' + parts + '/')
            fss = FileSystemStorage(location=tmp_address, base_url=tmp_address)
            filename = fss.save(file_obj.name, file_obj)
            url = fss.url(filename)
            data = {
                'file': file_obj,
                'parts': int(parts),
            }
            serializer = PartFileSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(file_obj.name, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response('No parts found in query parameters.', status=status.HTTP_400_BAD_REQUEST)


class PartFilesListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the  items for given requested user
        '''
        # self.request = request
        # automobile = self.get_queryset()
        part_id = self.request.query_params.get('part_id')
        if part_id:
            parts = PartFile.objects.filter(parts__parts_id__contains=part_id)
            serializer = PartFileSerializer(parts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Response(status=status.HTTP_404_NOT_FOUND)