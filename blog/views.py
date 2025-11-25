from django.shortcuts import render
from django.http import HttpResponse

#HttpResponse - модуль который отвечает за вывод одиночного сообщения

def helloWordView(request):
    if request.method == 'GET':
        return HttpResponse('Привет это мой первый проект на DJango!')


def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Всем привет я Радомир!')


#Пошагово урок 1 
#1.Создание startapp
#2.Прописание функции (def helloWordView)
#3.К каждой функции создается  url 
#4.Подключение urls.py (blog) -> main_app (urls.py) подключаем в главные urls.py

