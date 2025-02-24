from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexQuiz, name='index_quiz'),
    path('showQuestion/<int:page>/', views.showQuestion, name='showQuestion'),
    path('userAddQustion/<str:answer>/<int:id>/', views.userAddQustion, name='userAddQustion'),


    path('adminShowQuestions', views.adminShowQuestions, name='adminShowQuestions'),
    path('deleteQuestion/<int:idQuest>/', views.deleteQuestion, name='deleteQuestion'),
    path('addQuestion', views.addQuestion, name='addQuestion'),
    path('deleteRezultQuest', views.deleteRezultQuest, name='deleteRezultQuest'),

]