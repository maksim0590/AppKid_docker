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
    error_message = request.session.get('error_message')
    if error_message:
        del request.session['error_message']
    return render(request, 'userQuiz/admin/adminShowQuestions.html', context={'objectQuiz':objectQuiz,  'error_message':error_message})

def deleteQuestion(request, idQuest):
    objectQuiz = Quiz.objects.get(id=idQuest)
    objectQuiz.delete()
    return redirect('adminShowQuestions')

def addQuestion(request):
    inputQuest = request.POST.get('question')
    answerCorrect  = request.POST.getlist('chekbox[]')
    inputAnswer1 = request.POST.get('answer1')
    inputAnswer2 = request.POST.get('answer2')
    inputAnswer3 = request.POST.get('answer3')
    inputAnswer4 = request.POST.get('answer4')
    if not answerCorrect:
        request.session['error_message'] = 'Нужно отметить правильный ответ'
        return redirect('adminShowQuestions')
    else:
        objectQuiz = Quiz.objects.create(question=inputQuest,
                                     answer1=inputAnswer1,
                                     answer2=inputAnswer2,
                                     answer3=inputAnswer3,
                                     answer4=inputAnswer4,
                                     )
        correct = ''.join(answerCorrect)
        if correct == 'answer1':
            objectQuiz.answerCorrect = inputAnswer1
        elif correct  == 'answer2':
            objectQuiz.answerCorrect = inputAnswer2
        elif correct == 'answer3':
            objectQuiz.answerCorrect = inputAnswer3
        elif correct  == 'answer4':
            objectQuiz.answerCorrect = inputAnswer4

        objectQuiz.save()
        return redirect('adminShowQuestions') 
        
    
    
        
    
    