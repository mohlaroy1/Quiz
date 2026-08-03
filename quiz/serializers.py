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


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSafeSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ( 'id', 'text', 'image', 'quiz', 'answers')


class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text', 'image', 'is_correct')
        read_only_fields = ('id')


class QuestionCreateSerializer(serializers.ModelSerializer):
    answers = AnswerCreateSerializer(many=True)
    class Meta:
        model = Question
        fields = ('id', 'text', 'image', 'quiz', 'answers')

        def create(self, validated_data):
            answers = validated_data.pop('answers')
            question = Question.objects.create(**validated_data)

            for answer in answers:
                Answer.objects.create(question=question, **answer)

            return question

