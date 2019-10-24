from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods,require_POST
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model # 프로젝트에서 사용할 user 모델을 리턴
from .models import User
# 회원가입용 form, 인증(로그인)용 form
from .forms import CustomAuthenticationForm, CustomUserCreationForm

User = get_user_model()

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('/')
        else:
            form = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {
                'form': form
            })


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = CustomAuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('/')
        else:
            form = CustomAuthenticationForm()
            return render(request, 'accounts/login.html', {
                'form': form
            })


def logout(request):
    auth_logout(request)
    return redirect('/')
