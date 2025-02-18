from .views import LoadAPIView
from django.urls import path

urlpatterns = [
    path('load/', LoadAPIView.as_view(), name='load')
]