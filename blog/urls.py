from django.urls import path
from . import views

urlpatterns = [
    path('hello_word/', views.helloWordView, name='hello'),
    path('radomir/', views.about_me, name='about_me'),
]