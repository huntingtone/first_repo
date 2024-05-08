from django.urls import path, include
from .views import (
    AutomobileListApiView,
    PartsListApiView,
)

urlpatterns = [
    path('api', AutomobileListApiView.as_view()),
    path('parts', PartsListApiView.as_view()),
]