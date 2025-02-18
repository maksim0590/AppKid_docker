from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_two'),
    path('bonusShow', views.bonusShow, name='bonusShow'),
    path('bonusInputData', views.bonusInputData, name='bonusInputData'),
    path('exitplay', views.exitplay, name='exitplay'),
    path('level', views.level, name='level'),
    path('levelchoice/<int:level>/', views.levelchoice, name='levelchoice'),
]