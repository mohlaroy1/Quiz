from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'role', 'avatar', 'date_joined', 'last_login')
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class TeacherSerializer(UserSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.role = 'teacher'
        user.save()
        return user


class StudentSerializer(UserSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.role = 'student'
        user.save()
        return user
