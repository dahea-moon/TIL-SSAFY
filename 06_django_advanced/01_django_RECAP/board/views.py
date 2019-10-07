from django.shortcuts import render, redirect
from .models import Article


def index(request):
    return render(request, 'board/index.html')


def list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'board/list.html', context)


def detail(request, id):
    article = Article.objects.get(id=id)
    context = {'article': article}
    return render(request, 'board/detail.html', context)


def new(request):
    return render(request, 'board/new.html')


def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('board:detail', article.id)
