As I promised I updated it :wink:

download, install requirements.txt, migrate, create a superuser for authentication

first and foremost you should login to api using http://127.0.0.1:8000/api-auth/login

http://127.0.0.1:8000/autos/api

http://127.0.0.1:8000/autos/parts?manufacturer=manufacturer1

### pattern to add records for automobile (remember that you should add records one by one):
```
{
    "manufacturer": "manufacturer1",
    "tipe": "tipe1",
    "modl": "modl1",
    "user": 1
}

{
    "manufacturer": "manufacturer2",
    "tipe": "tipe2",
    "modl": "modl2",
    "user": 1
}

{
    "manufacturer": "manufacturer2",
    "tipe": "tipe2",
    "modl": "modl2",
    "user": 1
}
```
### pattern to add records for parts (remember that you should add records one by one):
```
{
    "name": "gear1",
    "autom": 1
}

{
    "name": "shift1",
    "autom": 1
}

{
    "name": "pedal1",
    "autom": 1
}

{
    "name": "wheel1",
    "autom": 1
}


{
    "name": "gear2",
    "autom": 2
}

{
    "name": "shift2",
    "autom": 2
}

{
    "name": "pedal2",
    "autom": 2
}

{
    "name": "wheel2",
    "autom": 2
}
```
### after adding automobiles and parts you can upload files related to parts using post request like below:
```
curl -X POST -H "Content-Type:multipart/form-data" -u admin:user -F "file=@/Users/sayedmohmmadrazavi/Desktop/photo.jpg" http://127.0.0.1:8000/autos/upload?parts=1
```
### you can download all files by know their part id and their name from the link patter below (consider part_id:1 and the file name is water_tank.png):
```
http://127.0.0.1:8000/autos/download/1/water_tank.png
```
