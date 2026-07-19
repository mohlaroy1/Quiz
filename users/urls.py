from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

urlpatterns = [
    path('token/', token_obtain_pair),
    path('token/refresh/', token_refresh),
]