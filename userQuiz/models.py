from django.db import models


class Quiz(models.Model):
    question = models.CharField('Вопрос', max_length=250)
    answerCorrect = models.CharField('Правильный', max_length=250, null=True, blank=True)
    answer1= models.CharField('Ответ1', max_length=250, null=True, blank=True)
    answer2 = models.CharField('Ответ2', max_length=250, null=True, blank=True)
    answer3= models.CharField('Ответ3', max_length=250, null=True, blank=True)
    answer4 = models.CharField('Ответ4', max_length=250, null=True, blank=True)
    status = models.IntegerField('Статус ответа', null=True, blank=True)
    message = models.CharField('Сообщение', max_length=250, null=True, blank=True)
    def __str__(self):
        return self.question