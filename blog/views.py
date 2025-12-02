from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import NewsPost, Slider

#Detail

def newsPostDetailView(request, id):
    if request.method == "GET":
        news_id = get_object_or_404(NewsPost, id=id)
        return render(
            request,
            'blog/news_detail.html',
            {
                'news_id': news_id,
            }
        )






#List
def newsPostView(request):
    if request.method == 'GET':
        #query запрос
        news = NewsPost.objects.all().order_by('-id')
        slider = Slider.objects.all().order_by('-id')
        return render(
            request,
            'blog/news_list.html',
            {
                'news_blog': news,
                'slider': slider
            }
        )












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

