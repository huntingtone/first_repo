from django.urls import path, include

from .views import (
    AutomobileListApiView,
    PartsListApiView,
    FileUploadView,
)



urlpatterns = [
    path('api', AutomobileListApiView.as_view()),
    path('parts', PartsListApiView.as_view()),
    path('upload', FileUploadView.as_view())
]