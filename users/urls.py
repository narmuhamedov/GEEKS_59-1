from django.urls import path
from users.views import RegisterView, AuthLoginView, user_list_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', AuthLoginView.as_view(), name='login'),
    path('users_list/', user_list_view, name='users_list'),
]