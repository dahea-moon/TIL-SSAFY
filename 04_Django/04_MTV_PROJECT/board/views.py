from django.shortcuts import render, redirect
from .models import Article


# Create
def new(request): # 새로운 게시글을 작성할 화면
    return render(request, 'board/new.html')


def create(request): # 입력 데이터를 DB에 저장
    # request.GET == {'input_title': ['제목'], 'input_content': ['내용']}
    article = Article()
    article.title = request.GET.get('input_title')
    article.content = request.GET.get('input_content')
    article.save()
    return redirect(f'/board/articles/{article.id}')


# Read
def index(request): # 모든 게시글(article) 목록을 보여주는 view 함수
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles': articles
    })


# Read
def show(request, article_id): # 특정 게시글을 보여주는 view
    article = Article.objects.get(id=article_id)
    return render(request, 'board/show.html', {
        'article': article,
    })


# Update
def edit(request, article_id): # 특정 게시글을 수정할 화면
    article = Article.objects.get(id=article_id)
    return render(request, 'board/edit.html', {
        'article': article
    })

def update(request, article_id):
    article = Article.objects.get(id=article_id)
    article.title = request.GET.get('modified_title')
    article.content = request.GET.get('modified_content')
    article.save()
    return redirect(f'/board/articles/{article.id}')


# TODO: Delete view
def delete(request, article_id): # 특정 게시글을 삭제하는 view
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/board/articles/')
