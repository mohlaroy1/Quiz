from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, \
    get_object_or_404, CreateAPIView
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from users.permissions import IsAdminUser, IsTeacherUser, IsStudentUser, IsTeacherOrAdmin

from .serializers import *
from .models import *

class GroupListCreateAPIView(ListCreateAPIView):

    def get_queryset(self):
        # Prevent Swagger from executing this method
        if getattr(self, 'swagger_fake_view', False):
            return Group.objects.none()

        user = self.request.user

        if not user.is_authenticated:
            return Group.objects.none()

        if user.role == 'admin':
            return Group.objects.all()

        elif user.role == 'teacher':
            return user.teaching_groups.all()

        elif user.role == 'student':
            return user.student_groups.all()

        return Group.objects.none()


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
        # Prevent Swagger from executing this method
        if getattr(self, 'swagger_fake_view', False):
            return Group.objects.none()

        user = self.request.user

        if not user.is_authenticated:
            return Group.objects.none()

        if user.role == 'admin':
            return Group.objects.all()

        elif user.role == 'teacher':
            return user.teaching_groups.all()

        elif user.role == 'student':
            return user.student_groups.all()

        return Group.objects.none()


    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return GroupSafeSerializer
        return GroupSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        return [IsAdminUser()]


class QuizListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        return [IsTeacherUser()]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'student':
            groups = user.student_groups.all()
            return Quiz.objects.filter(allowed_groups__in=groups).distinct()
        elif user.role == 'teacher':
            return Quiz.objects.filter(teacher=user)
        elif user.role == 'admin':
            return self.queryset
        return Quiz.objects.none()

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class QuizRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [IsAuthenticated()]
        elif self.request.method in ['PUT', 'PATCH']:
            return [IsTeacherUser()]
        elif self.request.method in ['DELETE']:
            return [IsTeacherOrAdmin()]
        return [IsAdminUser()]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'student':
            groups = user.student_groups.all()
            return Quiz.objects.filter(allowed_groups__in=groups).distinct()
        elif user.role == 'teacher':
            return Quiz.objects.filter(teacher=user)
        elif user.role == 'admin':
            return self.queryset
        return Quiz.objects.none()


class QuizAddQuestionAPIView(CreateAPIView):
    permission_classes = [IsTeacherUser,]
    serializer_class = QuestionCreateSerializer

    def get_queryset(self):
        return Question.objects.filter(quiz__teacher=self.request.user)



class QuestionListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'student':
            groups = user.student_groups.all()
            quizzes = Quiz.objects.filter(allowed_groups__in=groups).distinct()
            return Question.objects.filter(quiz__in=quizzes).distinct()
        elif user.role == 'teacher':
            return Question.objects.filter(quiz__teacher=user)
        elif user.role == 'admin':
            return self.queryset
        return Question.objects.none()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return QuestionSafeSerializer
        return QuestionSerializer

