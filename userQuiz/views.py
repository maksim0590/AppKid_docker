from django.http import HttpResponse
from django.shortcuts import render, redirect
import random
from userTasks.models import User,  Calcul, Tasks
from .models import Quiz
import random

def indexQuiz(request):
    return render(request, 'userQuiz/index.html')
def showQuestion(request):
    global list
    valueMax = Quiz.objects.latest('id').id
    valueMin = Quiz.objects.earliest('id').id
    t = Quiz.objects.all().order_by("id")
    return render(request, 'userQuiz/showQuestion.html')




#admin
def adminShowQuestions(request):
    objectQuiz = Quiz.objects.all()
    return render(request, 'userQuiz/admin/adminShowQuestions.html', context={'objectQuiz':objectQuiz})

def deleteQuestion(request, idQuest):
    objectQuiz = Quiz.objects.get(id=idQuest)
    objectQuiz.delete()
    return redirect('adminShowQuestions')

def addQuestion(request):
    inputQuest = request.POST.get('question')
    inputAnswer1 = request.POST.get('answer1')
    inputAnswer2 = request.POST.get('answer2')
    inputAnswer3 = request.POST.get('answer3')
    inputAnswer4 = request.POST.get('answer4')
    objectQuiz = Quiz.objects.create(question=inputQuest, answer1=inputAnswer1,answer2=inputAnswer2, answer3=inputAnswer3,answer4=inputAnswer4)
    objectQuiz.save()
    return redirect('adminShowQuestions')