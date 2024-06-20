from django.db import models

# Create your models here.
class Subject(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название предмета'
    )   
    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        
class Question(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name="Предмет"
    )
    question = models.CharField(
        max_length=255,
        verbose_name='Вопрос'
    )
    answer = models.TextField(
        verbose_name='ответ'
    )
    
    def __str__(self):
        return f'{self.question} - {self.answer}'
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
