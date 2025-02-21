from pydoc import pager
from tabnanny import check

from django.http import HttpResponse
from django.shortcuts import render, redirect
import random
from userTasks.models import User,  Calcul, Tasks
from .models import Quiz
import random
from django.core.paginator import Paginator
from django.shortcuts import render

def indexQuiz(request):
    return render(request, 'userQuiz/index.html')
def showQuestion(request, page ):
    objectQuestions = Quiz.objects.all()
    paginator = Paginator(objectQuestions, 1)
    page_obj = paginator.get_page(page)
    request.session['page'] = page
    return render(request, 'userQuiz/showQuestion.html', context={'page_obj':page_obj})
def userAddQustion(request, answer, id):
    objectQuestions = Quiz.objects.get(id=id)
    if objectQuestions.answerCorrect == answer:
        objectQuestions.status = 1
        objectQuestions.message = 'Верно'
        objectQuestions.save()
        page = request.session.get('page') + 1
        return redirect('showQuestion', page)
    else:
        objectQuestions.status = 0
        objectQuestions.message = 'Ошибка'
        objectQuestions.save()
        page = request.session.get('page') + 1
        return redirect('showQuestion', page)

    # return redirect('showQuestion', )



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
    checkBoxAnswer1 =request.POST.get('answer1chekbox')
    checkBoxAnswer2 = request.POST.get('answer2chekbox')
    checkBoxAnswer3 = request.POST.get('answer3chekbox')
    checkBoxAnswer4 = request.POST.get('answer4chekbox')

    inputAnswer1 = request.POST.get('answer1')
    inputAnswer2 = request.POST.get('answer2')
    inputAnswer3 = request.POST.get('answer3')
    inputAnswer4 = request.POST.get('answer4')
    objectQuiz = Quiz.objects.create(question=inputQuest,
                                     answer1=inputAnswer1,
                                     answer2=inputAnswer2,
                                     answer3=inputAnswer3,
                                     answer4=inputAnswer4,
                                     )
    if checkBoxAnswer1 == 'on':
        objectQuiz.answerCorrect = inputAnswer1

    elif  checkBoxAnswer2 == 'on':
        objectQuiz.answerCorrect = inputAnswer2

    elif checkBoxAnswer3 == 'on':
        objectQuiz.answerCorrect = inputAnswer3

    elif  checkBoxAnswer4 == 'on':
        objectQuiz.answerCorrect = inputAnswer4

    objectQuiz.save()
    return redirect('adminShowQuestions')