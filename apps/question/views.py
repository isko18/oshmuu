from rest_framework import mixins, viewsets
from rest_framework.generics import GenericAPIView

from apps.question.models import Subject, Question
from apps.question.serializers import QuestionSerializers, SubjectSerializers
# Create your views here.

class SubjectAPIViews(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializers

class QuestionAPIViews(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers