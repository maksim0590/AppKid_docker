
import time
from django.shortcuts import render, redirect
import datetime
from .models import Calcul, User, Tasks
from .services import sendMessage


def index(request):
    return render(request, 'first/index.html')

def welcome(request):
    return render(request, 'first/welcome_pg.html')

def main(request):
    nameFromInput = request.POST.get('name')
    nameDbObject = User.objects.filter(name=nameFromInput).exists()
    if nameDbObject == True:
        objectUser = User.objects.get(name=nameFromInput)
        request.session['id_user'] = objectUser.id
        return redirect('task')
    else:
        objectUser = User.objects.create(name=nameFromInput, count_zvezd=1)
        request.session['id_user'] = objectUser.id
        objectCalcul = Calcul.objects.create(number1=0, number2=0, number3=None, rezult=0, rezultUser=0, count_zvezd=0)
        request.session['id_calcul'] = objectCalcul.id
        return redirect('mainusershow')
def mainusershow(request):
    id = request.session.get('id_user')
    objectUser = User.objects.get(id=id)
    return render(request, 'first/main.html', context={'name':objectUser.name, 'count':objectUser.count_zvezd})

def gogames(request):
    prize = request.POST.get('prize')
    id = request.session.get('id_user')
    save_prize = User.objects.get(id=id)
    save_prize.prize = prize
    save_prize.count_zvezd +=1
    save_prize.save()
    return redirect('gogamesshow')
def gogamesShow(request):
    id = request.session.get('id_user')
    user = User.objects.get(id=id)
    count = user.count_zvezd
    prize = user.prize
    sendMessage(f'{user.name} приступила к выполнению заданий  \n В качестве вознаграждения хочет получить: {user.prize} ')
    return render(request, "first/gogames.html", context={ 'prize':prize, 'count':count})


def tasks(request):
    id = request.session.get('id_user')
    user = User.objects.get(id=id)
    data = user.tasks_set.all()
    dateNow = datetime.datetime.now()
    weekDay = dateNow.weekday()
    return render(request, "first/tasks.html", context={'data':data, 'user':user, 'weekDay':weekDay})
def status(request, day, idtask):
    id = request.session.get('id_user')
    user = User.objects.get(id=id)
    task = Tasks.objects.get(id=idtask)
    user.count_zvezd += task.price
    user.save()
    setattr(task, day, 1)
    task.save()
    return redirect('task')
def delete(request):
    id = request.session.get('id_user')
    user = User.objects.get(id=id)
    user.delete()
    return redirect('index')


# AdminViews
def adminTasks(request):
    objectUser = User.objects.all()
    return render(request, 'first/admin/adminTask.html', context={'objectUser':objectUser})

def adminViewUser(request, idUser):
    user = User.objects.get(id=idUser)
    dataTask = user.tasks_set.all()
    request.session['id_user'] = user.id
    return render(request, 'first/admin/adminViewUser.html', context={'dataTask':dataTask, 'dataUser':user})

def adminDeleteTask(request, idTask):
    id = request.session.get('id_user')
    objectTask = Tasks.objects.get(id=idTask)
    objectTask.delete()
    return redirect('adminViewUser', idUser=id)

def adminAddTask(request):
    id = request.session.get('id_user')
    inputUserTask = request.POST.get('task')
    inputUserPrice = request.POST.get('price')
    user = User.objects.get(id=id)
    task = Tasks(task=inputUserTask, price=inputUserPrice)
    user.tasks_set.add(task, bulk=False)
    return redirect('adminViewUser', idUser=id)

def adminStatus(request, day, idTask):
    idUser = request.session.get('id_user')
    user = User.objects.get(id=idUser)
    task = Tasks.objects.get(id=idTask)
    user.count_zvezd += task.price
    user.save()
    setattr(task, day, 1)
    task.save()
    return redirect('adminViewUser', idUser=idUser)







