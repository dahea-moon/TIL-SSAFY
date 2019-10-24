from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:article_list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:article_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/form.html', context={
        'form': form,
    })


def login(request):
    if request.user.is_authenticated:
        return redirect('articles:article_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'articles:article_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/form.html', context={
        'form': form,
    })

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')