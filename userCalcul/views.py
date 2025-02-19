from django.http import HttpResponse
from django.shortcuts import render, redirect
import random
from userTasks.models import User,  Calcul, Tasks
from .servieces import calcul, calculTwoLevel, calculThreeLevel



def index(request):
    object = User.objects.all()
    return render(request, 'two/index.html', context={'object':object})

def level(request):
    return render(request, 'two/level.html')
def levelchoice(request, level):
    id = request.session.get('id_calcul')
    objectCalcul = Calcul.objects.get(id=id)
    if level == 1:
        objectCalcul.level = 1
        objectCalcul.save()
    elif level == 2:
        objectCalcul.level = 2
        objectCalcul.save()
    elif level == 3:
        objectCalcul.level = 3
        objectCalcul.save()
    return redirect('bonusShow')

def bonusShow(request):
    title = 'Реши пример'

    a = random.randint(2, 10)
    b = random.randint(2, 10)
    f = None
    id = request.session.get('id_calcul')
    objectCalcul = Calcul.objects.get(id=id)
    level = objectCalcul.level
    d = []
    def oper(a):
        if a == 1:
            d.append('+')
            return d
        elif a == 2:
            d.append('+')
            d.append('-')
            return d
        elif a == 3:
            d.append('+')
            d.append('-')
            # d.append('*')
            return d
    oper(level)
    operation = random.choice(d)
    operatorTwo = random.choice(d)
    if level == 2:
        c = calculTwoLevel(a=a, b=b, operator=operation)
        id = request.session.get('id_calcul')
        objectCalcul = Calcul.objects.get(id=id)
        objectCalcul.number1 = a
        objectCalcul.number2 = b
        objectCalcul.rezult = c
        objectCalcul.save()
    elif level == 3:
        f = random.randint(2, 10)
        c = calculThreeLevel(a=a, b=b, f=f, operation=operation, operatorTwo=operatorTwo)
        id = request.session.get('id_calcul')
        objectCalcul = Calcul.objects.get(id=id)
        objectCalcul.number1 = a
        objectCalcul.number2 = b
        objectCalcul.number3 = f
        objectCalcul.rezult = c
        objectCalcul.save()
    else:
       c = calcul(a=a, b=b, operation=operation)
    id = request.session.get('id_calcul')
    objectCalcul = Calcul.objects.get(id=id)
    objectCalcul.number1 = a
    objectCalcul.number2 = b
    objectCalcul.number3 = f
    objectCalcul.rezult = c
    objectCalcul.save()
    return render(request, 'two/bonus_task.html', context={'title':title,
                                                             'level':level,
                                                             'a':objectCalcul.number1,
                                                             'b':objectCalcul.number2,
                                                             'f':objectCalcul.number3,
                                                             'operatorTwo':operatorTwo,
                                                             'count':objectCalcul.count_zvezd,
                                                              'operation':operation,
                                                             'message':objectCalcul.message,
                                                             'message_error':objectCalcul.message_error,
                                                             'message_warning': objectCalcul.message_warning,
                                                             'message_endPlay':objectCalcul.message_endPlay
                                                             })
def bonusInputData(request):
    rezultInput = request.POST.get('rezult')

    id = request.session.get('id_calcul')
    objectCalcul = Calcul.objects.get(id=id)
    objectCalcul.rezultUser = int(rezultInput)
    objectCalcul.save()
    if objectCalcul.rezultUser == objectCalcul.rezult:
        objectCalcul.message = True
        objectCalcul.message_warning = False
        objectCalcul.message_error = False
        objectCalcul.count_zvezd +=1
        objectCalcul.save()
        if objectCalcul.count_zvezd == 15:
            id = request.session.get('id_user')
            objectUser = User.objects.get(id=id)
            if objectCalcul.level == 1:
                objectUser.count_zvezd += 1
                objectUser.save()
            elif objectCalcul.level == 2:
                objectUser.count_zvezd += 2
                objectUser.save()
            elif objectCalcul.level == 3:
                objectUser.count_zvezd += 3
                objectUser.save()
        return redirect('bonusShow')
    else:
        objectCalcul.message = False
        objectCalcul.message_warning = False
        objectCalcul.message_error = True
        objectCalcul.count_zvezd -= 1
        objectCalcul.save()
        if objectCalcul.count_zvezd < -1:
            objectCalcul.count_zvezd += 1
            objectCalcul.save()
        return redirect('bonusShow')

def exitplay(request):
    id = request.session.get('id_calcul')
    objectCalcul = Calcul.objects.get(id=id)
    objectCalcul.count_zvezd = 0
    objectCalcul.message = False
    objectCalcul.message_warning = False
    objectCalcul.message_error = False
    objectCalcul.save()
    return redirect('task')

def stillPlay(request):
    id = request.session.get('id_calcul')
    objectCalcul = Calcul.objects.get(id=id)
    objectCalcul.count_zvezd = 0
    objectCalcul.message = False
    objectCalcul.message_warning = False
    objectCalcul.message_error = False
    objectCalcul.save()
    return redirect('level')