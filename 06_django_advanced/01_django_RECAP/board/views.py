from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Article, Comment
from IPython import embed
from .forms import ArticleModelForm, CommentModelForm


def new_article_with_form(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article.objects.created(title=title, content=content)
            return redirect(article)
    else:
        form = ArticleForm()
    return render(request, 'board/new.html', {
        'form': form
    })

#CRUD
@require_http_methods(['GET', 'POST'])
def new_article(request):
    # 요청이 GET/POST 인지 확인한다.
    # 만약 POST 라면,
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
        # ArticleModelForm의 인스턴스를 생성하고 Data를 채운다.(binding).
        # binding 된 form이 유효한지 체크한다.
        if form.is_valid():
            # 유효하다면 저장한다.
            article = form.save()
            # 저장한 article 로 redirect 한다.
            # redirect('board:article_detail', article.id) => get_absolute_url 때문에 줄이기 가능
            return redirect(article)
        # form이 유효하지않다면,
        else:
            # 유효하지 않은 입력데이터를 담은 HTML과 에러메세지를 사용자한테 보여준다.
            return render(request, 'board/new.html', {
                'form': form,
            })
    # GET 이라면
    else:
        # 비어있는 form을 만든다.
        form = ArticleModelForm()
        # form 과 html을 사용자에게 보여준다.
        return render(request, 'board/new.html', {
            'form': form,
        })

def list_article(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'board/list.html', context)

def detail_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comment_set.all().order_by('-id')
    comment_form = CommentModelForm()
    context = {'article': article, 'comments': comments, 'comment_form': comment_form, }
    return render(request, 'board/detail.html', context)

@require_http_methods(['GET', 'POST'])
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        # update
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save() # aritcle = 은 안 써도 된다
            return redirect(article)
    else:
        # edit
        # 그 article 내용을 가져올 수 있는 코드
        form = ArticleModelForm(instance=article)
    return render(request, 'board/edit.html', {'form': form})


@require_POST
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('board:list')


@require_POST
def new_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    form = CommentModelForm(request.POST)
    if form.is_valid():
        # comment = Comment()
        # comment.content = request.POST.get('content')
        comment = form.save(commit=False)
        comment.article_id = article.id
        comment.save()
    return redirect(article)


def delete_comment(request, article_id, comment_id):
    article = get_object_or_404(Article, id=article_id)
    # SELECT * FROM articles WHERE id=article_id
    comment = get_object_or_404(Comment, id=comment_id, article_id=article_id)
    # SELECT * FROM comments WHERE id=comment_id
    # if comment in article.comment_set.all():
    comment.delete()
    return redirect(comment.article)
