from drf_yasg import openapi
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import SAFE_METHODS

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
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('student_groups',)

    def get_queryset(self):
        return User.objects.filter(role='student')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        return StudentCreateSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'student_groups',
                in_=openapi.IN_QUERY,
                description="Guruh bo'yicha filterlash",
                type=openapi.TYPE_INTEGER,
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


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