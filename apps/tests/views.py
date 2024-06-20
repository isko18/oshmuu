from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.tests.models import Test
from apps.tests.serializers import SerializersTest
from apps.question.models import Question, Subject
import random

class TestViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Test.objects.all()
    serializer_class = SerializersTest

    def create(self, request, *args, **kwargs):
        subject_id = request.data.get('subject')
        subject = get_object_or_404(Subject, id=subject_id)
        questions = list(Question.objects.filter(subject=subject))
        
        if len(questions) < 3:
            return Response(
                {"detail": "Недостаточно вопросов для создания теста."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        selected_questions = random.sample(questions, 3)
        
        # Создаем тест без вопросов
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        test = serializer.save()
        
        # Добавляем выбранные вопросы
        test.questions.set(selected_questions)
        test.save()

        serializer = self.get_serializer(test)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
