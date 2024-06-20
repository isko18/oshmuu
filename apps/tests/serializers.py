from rest_framework import serializers
from apps.tests.models import Test
from apps.question.serializers import QuestionSerializers

class SerializersTest(serializers.ModelSerializer):
    questions = QuestionSerializers(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ('title', 'subject', 'questions')