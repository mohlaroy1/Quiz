from rest_framework import serializers

from users.serializers import StudentCreateSerializer
from .models import *

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'students')


class GroupSafeSerializer(serializers.ModelSerializer):
    students = StudentCreateSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'students')