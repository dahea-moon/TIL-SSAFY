from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('sns:posting_list')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('sns:posting_list')
        else:
            form = UserCreationForm()
        return render(request, 'accounts/signup.html', {
            'form': form
        })


@require_http_methods(['GET', 'POST'])
def login(request):
    # if # 사용자가 login 한 상태라면, 무시
    if request.user.is_authenticated:
        return redirect('sns:posting_list')
    # anonymoususer라면 login 페이지로
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                # response = redirect('sns:posting_list')
                # response.set_cookie(key='nickname', value='idiot', max_age=5)
                return redirect('sns:posting_list')
        else:
            form = AuthenticationForm()
        return render(request, 'accounts/login.html', {
            'form': form
        })


def logout(request):
    auth_logout(request)
    return redirect('sns:posting_list')