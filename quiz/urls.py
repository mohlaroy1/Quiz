from email._header_value_parser import GroupList

from django.urls import path
from .views import *

urlpatterns = [
    path('groups/', GroupListCreateAPIView.as_view()),
    path('groups/<int:pk>/', GroupRetrieveUpdateDestroyAPIView.as_view()),
]