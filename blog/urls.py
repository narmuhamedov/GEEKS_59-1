from django.urls import path
from . import views

urlpatterns = [
    #as_view() - метод который вызывает классы
    path('', views.NewsPostView.as_view(), name='news_post_list'),
    path('news_list/<int:id>/', views.NewsPostDetailView.as_view(), name='news_detail'),
    path('hello_word/', views.helloWordView, name='hello'),
    path('radomir/', views.about_me, name='about_me'),
]