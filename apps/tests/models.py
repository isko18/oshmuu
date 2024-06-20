from django.db import models

from apps.question.models import Subject, Question
# Create your models here.
class Test(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название теста'
    )
    subject = models.ForeignKey(
        Subject, 
        on_delete=models.CASCADE
    )
    questions = models.ManyToManyField(
        Question,
        verbose_name='Вопросы'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'