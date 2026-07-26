from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from users.permissions import IsAdminUser, IsTeacherUser, IsStudentUser

from .serializers import *
from .models import *

class GroupListCreateAPIView(ListCreateAPIView):

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Group.objects.all()
        elif user.role == 'teacher':
            return user.teacher_groups.all()
        elif user.role =='student':
            return user.student_groups.all()
        return None


    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return GroupSafeSerializer
        return GroupSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        return [IsAdminUser()]


class GroupRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Group.objects.all()
        elif user.role == 'teacher':
            return user.teacher_groups.all()
        elif user.role =='student':
            return user.student_groups.all()
        return None


    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return GroupSafeSerializer
        return GroupSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        return [IsAdminUser()]



