from rest_framework import serializers

from apps.question.models import Subject, Question

class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        
class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'