from rest_framework import serializers

from users.serializers import UserSerializer
from .models import *

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class GroupSafeSerializer(serializers.ModelSerializer):
    students = UserSerializer(many=True, read_only=True)
    teacher = UserSerializer(read_only=True)

    class Meta:
        model = Group
        fields = '__all__'