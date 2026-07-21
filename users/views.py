from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import *
from .models import *
from .permissions import *

class TeacherListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return User.objects.filter(role='teacher')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        return TeacherCreateSerializer



class TeacherRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(role='teacher')


class StudentListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return User.objects.filter(role='student')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        return StudentCreateSerializer


class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(role='student')


class AdminListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return User.objects.filter(role='admin')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        return AdminCreateSerializer


class AdminRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(role='admin')