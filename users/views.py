from rest_framework.generics import ListCreateAPIView

from .serializers import *
from .models import *
from permissons import *

class TeacherListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return User.objects.filter(role='teacher')

