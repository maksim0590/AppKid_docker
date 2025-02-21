from django.urls import path
from . import views
from django.http import HttpResponse
from django.shortcuts import render

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome', views.welcome, name='welcome'),
    path('gogames', views.gogames, name='gogames'),
    path('gogamesshow', views.gogamesShow, name='gogamesshow'),
    path('main', views.main, name='main'),
    path('mainusershow', views.mainusershow, name='mainusershow'),
    path('tasks', views.tasks, name='task'),
    path('status/<str:day>/<int:idtask>/', views.status, name='status'),
    path('delete', views.delete, name='delete'),
    path('choicePlay', views.choicePlay, name='choicePlay'),


    # admin
    path('welcomeAdmin', views.welcomeAdmin, name='welcomeAdmin'),
    path('adminMain', views.adminMain, name='adminMain'),
    path('adminModule', views.adminModule, name='adminModule'),
    path('adminTasks', views.adminTasks, name='adminTasks'),
    path('adminViewUser/<int:idUser>/', views.adminViewUser, name='adminViewUser'),
    path('adminDeleteTask/<int:idTask>/', views.adminDeleteTask, name='adminDeleteTask'),
    path('adminAddTask', views.adminAddTask, name='adminAddTask'),
    path('adminStatus/<str:day>/<int:idTask>/', views.adminStatus, name='adminStatus'),
    

    
]

a = 0
try: 
    if a == 5:
        urlpatterns = [
            path('test', views.test, name='test'),
        ]
except:
    print('no')
    