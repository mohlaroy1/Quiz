from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from users import permissions
from users.permissions import IsAdminUser, IsTeacherUser, IsStudentUser

from .serializers import *
from .models import *

class GroupListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Group.objects.all()
        elif user.role == 'teacher':
            return user.group_set.all()
        elif user.role =='student':
            return Group.objects.filter(students=user)
        return None


    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return GroupSafeSerializer
        return GroupSerializer

