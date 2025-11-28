from django.urls import path
from . import views

urlpatterns = [
    path('news_list/', views.newsPostView, name='news_post_list'),
    path('news_list/<int:id>/', views.newsPostDetailView, name='news_detail'),
    path('hello_word/', views.helloWordView, name='hello'),
    path('radomir/', views.about_me, name='about_me'),
]