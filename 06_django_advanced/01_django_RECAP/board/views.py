from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from .models import Article


@require_GET
def index(request):
    return render(request, 'board/index.html')


@require_GET
def list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'board/list.html', context)


@require_GET
def detail(request, id):
    article = get_object_or_404(Article, id=id)
    context = {'article': article}
    return render(request, 'board/detail.html', context)


def new(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect(article)
    else:
        return render(request, 'board/new.html')


# @require_POST
# def create(request):
#     article = Article()
#     article.title = request.POST.get('title')
#     article.content = request.POST.get('content')
#     article.save()
#     return redirect('board:detail', article.id)


def edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect(article)
    else:
        context = {'article': article}
        return render(request, 'board/edit.html', context)


# @require_POST
# def update(request, id):
#     article = get_object_or_404(Article, id=id)
#     article.title = request.POST.get('title')
#     article.content = request.POST.get('content')
#     article.save()
#     return redirect('board:detail', article.id)


@require_POST
def delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect('board:list')
