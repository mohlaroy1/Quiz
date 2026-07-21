from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from users.views import TeacherListCreateAPIView, TeacherRetrieveUpdateDestroyAPIView, StudentListCreateAPIView, \
    StudentRetrieveUpdateDestroyAPIView, AdminListCreateAPIView, AdminRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('token/', token_obtain_pair),
    path('token/refresh/', token_refresh),
    path('teachers/', TeacherListCreateAPIView.as_view()),
    path('teachers/<int:pk>/', TeacherRetrieveUpdateDestroyAPIView.as_view()),
    path('students/', StudentListCreateAPIView.as_view()),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view()),
    path('admins/', AdminListCreateAPIView.as_view()),
    path('admins/<int:pk>/', AdminRetrieveUpdateDestroyAPIView.as_view()),
]