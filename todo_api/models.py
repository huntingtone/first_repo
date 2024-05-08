from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Automobile(models.Model):
    manufacturer = models.CharField(max_length=180)
    tipe = models.CharField(max_length=180)
    modl = models.CharField(max_length=180)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Parts(models.Model):
    name = models.CharField(max_length=180)
    autom = models.ForeignKey(Automobile, on_delete=models.CASCADE)


class PartFile(models.Model):
    file = models.FileField()
    parts = models.ForeignKey(Parts, related_name="files", on_delete=models.CASCADE)

# class Automobile:
#     def __init__(self):
#         self.__manufacturer = ''
#         self.__tipe = ''
#         self.__modl = ''
#         self.__parts = Parts()
#
#     def setmanufacturer(self, manufacturer):
#         print('setname() called')
#         self.__manufacturer = manufacturer
#
#     def getmanufacturer(self):
#         print('getname() called')
#         return self.__manufacturer
#
#     def settype(self, t):
#         print('setname() called')
#         self.__tipe = t
#
#     def gettype(self):
#         print('getname() called')
#         return self.__tipe
#
#     def setmodel(self, modl):
#         print('setname() called')
#         self.__modl = modl
#
#     def getmodel(self):
#         print('getname() called')
#         return self.__modl
#
#     manufacturer = property(getmanufacturer, setmanufacturer)
#     tipe = property(gettype, settype)
#     modl = property(getmodel, setmodel)
#
#
# class Parts:
#     def __init__(self):
#         self.__name = ''
#         self.__files = []
#
#     def setname(self, name):
#         print('setname() called')
#         self.__name = name
#
#     def getname(self):
#         print('getname() called')
#         return self.__name
#
#     def setfile(self, file):
#         print('setname() called')
#         self.__files.append(file)
#
#     def getfile(self, idx):
#         print('getname() called')
#         return self.__files[idx-1]
#
#     name = property(getname, setname)
#     files = property(getfile, setfile)


