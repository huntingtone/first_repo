from django.urls import path, include
from django.urls import re_path as url
from django.conf import settings

from .views import (
    AutomobileListApiView,
    PartsListApiView,
    FileUploadView,
    PartFilesListApiView,
    download,
)



urlpatterns = [
    path('api', AutomobileListApiView.as_view()),
    path('parts', PartsListApiView.as_view()),
    path('upload', FileUploadView.as_view()),
    path('list_of_part_files', PartFilesListApiView.as_view()),
    url(r'^download/(?P<path>.*)$', download),
]