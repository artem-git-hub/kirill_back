from rest_framework import serializers
from .models import Subject, Test, Question, UserAnswer

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'code']

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['name', 'code']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'answer']

class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['question', 'user_answer']
