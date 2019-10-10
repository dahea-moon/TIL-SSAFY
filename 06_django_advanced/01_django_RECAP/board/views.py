from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Article
from IPython import embed
from .forms import ArticleModelForm

#CRUD
@require_http_methods(['GET', 'POST'])
def new(request):
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
            # redirect('board:detail', article.id) => get_absolute_url 때문에 줄이기 가능
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

def list(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'board/list.html', context)

def detail(request, id):
    article = get_object_or_404(Article, id=id)
    context = {'article': article}
    return render(request, 'board/detail.html', context)

@require_http_methods(['GET', 'POST'])
def edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        # update
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        # edit
        # 그 article 내용을 가져올 수 있는 코드
        form = ArticleModelForm(instance=article)
    return render(request, 'board/edit.html', {'form': form})


@require_POST
def delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect('board:list')
