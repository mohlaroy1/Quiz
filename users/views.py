from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import *
from .models import *
from .permissions import *

class TeacherListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return User.objects.filter(role='teacher')



class TeacherRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return User.objects.filter(role='teacher')
