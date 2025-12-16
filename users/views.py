from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


from  users.models import CustomUser
from users.forms import CustomUserForm, LoginCaptchaInput

from django.views import generic


#Личный кабинет пользователей
def user_list_view(request):
    if request.method == 'GET':
        users_list = CustomUser.objects.all().order_by('-id')
        return render(
            request,
            'users/user_list.html',
            {
                'users_list': users_list
            }
        )


#Выход из личного кабинета по нажатию кнопки выйти из аккаунта
def auth_logout_view(request):
    logout()
    return redirect('login')



#Авторизация
class AuthLoginView(generic.View):

    def get(self, request):
        form = LoginCaptchaInput()
        context_object_name = {
            'form': form
        }
        return render(
            request,
            template_name="users/login.html",
            context = context_object_name
        )


    def post(self, request):
        form = LoginCaptchaInput(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("users_list")
        context_object_name = {
            'form': form
        }
        return render(
            request,
            template_name='users/login.html',
            context=context_object_name
        )









# def auth_login_view(request):
#     if request.method == 'POST':
#         form = LoginCaptchaInput(data=request.POST)
#         #form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             #return HttpResponse('Вы успешно авторизовались 200')
#             return redirect('users_list')
#     else:
#         form = LoginCaptchaInput()
#         #form = AuthenticationForm()
#     return render(
#         request,
#         'users/login.html',
#         {
#             'form':form
#         }
#     )




#Регистрация


class RegisterView(generic.View):
    #Регистрация если статус код 200 успешен и на сервере нет ошибок
    def post(self, request):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context_object_name = {
            'form':form
        }
        return render(
                      request, 
                      template_name='users/create_user.html',
                      context=context_object_name)
        
    #Если при регистрации какая то серверная ошибка
    def get(self, request):
        form = CustomUserForm()
        context_object_name = {
            'form':form
        }
        return render(
                      request, 
                      template_name='users/create_user.html',
                      context=context_object_name)
        



# def register_view(request):
#     if request.method == 'POST':
#         form = CustomUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             #return HttpResponse('Регистрация прошла успешно 200')
#             return redirect('login')
#     else:
#         form = CustomUserForm()
#     return render(
#         request,
#         'users/create_user.html',
#         {
#             "form": form
#         }
#     )

