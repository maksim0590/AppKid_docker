from django.db import models


class User(models.Model):
    name = models.CharField('Имя', max_length=50)
    prize = models.CharField('Приз', max_length=250, null=True, blank=True)
    count_zvezd = models.IntegerField('Количество звезд', null=True, blank=True)
    role = models.CharField('Роль', max_length=50, default='user')
    def __str__(self):
        return self.name

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField('Задание', max_length=250, default=0)
    mon = models.IntegerField('Понедельник', default=0)
    tue = models.IntegerField('Вторник', default=0)
    wed = models.IntegerField('Среда', default=0)
    thu = models.IntegerField('Четверг', default=0)
    fri = models.IntegerField('Пятница', default=0)
    sat = models.IntegerField('Суббота', default=0)
    sun = models.IntegerField('Воскресенье', default=0)
    price = models.IntegerField('Oценка', null=True, blank=True)
    def __str__(self):
        return self.task



class Test(models.Model):
    name = models.CharField('Имя', max_length=50)
    age = models.CharField('Возраст', max_length=250)
    text = models.CharField('Текст', max_length=250)

    def __str__(self):
        return self.name

class Calcul(models.Model):
    number1 = models.IntegerField('Первое значение', null=True, blank=True)
    number2 = models.IntegerField('Второе значение', null=True, blank=True)
    number3 = models.IntegerField('Третье значение', null=True, blank=True)
    rezult = models.IntegerField('Результат', null=True, blank=True)
    rezultUser = models.IntegerField('Результат пользователя', null=True, blank=True)
    level = models.IntegerField('Уровень сложности', default=0)
    count_zvezd  = models.IntegerField('Количество заработанных звезд', null=True, blank=True)
    message = models.BooleanField('Сообщение', default=False)
    message_warning = models.BooleanField('Сообщение-предупреждение', default=False)
    message_error = models.BooleanField('Сообщение-ошибка', default=False)
    message_endPlay = models.CharField('Сообщение', max_length=50)

