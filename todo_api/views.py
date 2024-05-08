from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Automobile, Parts, PartFile
from .serializers import AutomobileSerializer, PartsSerializer, PartFileSerializer

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
        parts = self.get_queryset()
        serializer = PartsSerializer(parts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        automobile = Automobile.objects.filter(manufacturer=request.Automobile.manufacturer)
        parts = Parts.objects.filter(autom=automobile)
        return parts

    def get_queryset(self):
        manufacturer = self.request.query_params.get('manufacturer')
        queryset = Automobile.objects.filter(manufacturer=manufacturer)
        return  queryset


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