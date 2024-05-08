from rest_framework import serializers
from .models import Automobile, Parts, PartFile


class AutomobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automobile
        fields = ["manufacturer", "tipe", "modl", "user"]


class PartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parts
        fields = ["name", "autom"]


class PartFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartFile
        fields = ["file", "parts"]