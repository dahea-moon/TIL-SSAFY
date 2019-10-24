from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Article
from .forms import ArticleModelForm


def like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    # if article.like_users.filter(id=user.id).exists():
    if user in article.like_users.all():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)
    return redirect('articles:article_list')


@require_GET
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {
        'articles': articles,
    })


@require_GET
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail.html', {
        'article': article,
    })


@login_required
@require_http_methods(['POST', 'GET'])
def create_article(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            # article.user_id = request.user.id
            article.save()
        return redirect('articles:article_detail', article.id)
    else:
        form = ArticleModelForm()
    return render(request, 'articles/form.html', {
        'form': form
    })


@login_required
@require_http_methods(['POST', 'GET'])
def update_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if article.user != request.user:
        return redirect('articles:article_list')
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            article.save()
        return redirect('articles:article_detail', article.id)
    else:
        form = ArticleModelForm(instance=article)
    return render(request, 'articles/form.html', {
        'form': form
    })


def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.user == article.user:
        article.delete()
    return redirect('articles:article_list')
    