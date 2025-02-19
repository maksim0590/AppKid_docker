from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexQuiz, name='index_quiz'),
    path('showQuestion', views.showQuestion, name='showQuestion'),


    path('adminShowQuestions', views.adminShowQuestions, name='adminShowQuestions'),
    path('deleteQuestion/<int:idQuest>/', views.deleteQuestion, name='deleteQuestion'),
    path('addQuestion', views.addQuestion, name='addQuestion'),

]