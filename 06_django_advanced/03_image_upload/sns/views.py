from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required

from .models import Posting, Comment
from .forms import PostingModelForm, CommentModelForm


@require_GET
def posting_list(request):
    # nickname = request.COOKIES.get('nickname')
    postings = Posting.objects.all()
    context = {'postings': postings}
    return render(request, 'sns/posting_list.html', context)


@login_required # login이 안되면 => 무조건 /accounts/login/ 으로 보냄
@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comments.all() # comment_set이 아닌 이유는 related_name이 comments이기 때문이다
    if posting.like_users.filter(id=request.user.id).exists():
        is_like = True
    else:
        is_like = False
    context = {'posting': posting, 'comments': comments, 'is_like': is_like}
    return render(request, 'sns/posting_detail.html', context)


@login_required # login이 안되면 => 무조건 /accounts/login/ 으로 보냄
@require_POST
def create_posting(request):
    form = PostingModelForm(request.POST, request.FILES)   # 검증 & 저장 준비
    if form.is_valid(): # 검증
        posting = form.save(commit=False) # 저장 후 posting 개체를 return
        # posting.user = request.user
        posting.user_id = request.user.id
        posting.save()
        return redirect(posting)
    else:
        return redirect('sns:posting_list')


@login_required # login이 안되면 => 무조건 /accounts/login/ 으로 보냄
@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.user == posting.user:
        posting.delete()
    return redirect('sns:posting_list')


@login_required # login이 안되면 => 무조건 /accounts/login/ 으로 보냄
@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentModelForm(request.POST) # content 만을 확인 (forms.py에 있는 fields만 읽는다)
    if form.is_valid():
        comment = form.save(commit=False)
        # comment.posting_id = posting_id
        comment.posting = posting
        comment.user = request.user
        comment.save()
    return redirect(posting)


@login_required # login이 안되면 => 무조건 /accounts/login/ 으로 보냄
@require_GET
def delete_comment(request, posting_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect(comment.posting)


@login_required
@require_POST
def toggle_like(request, posting_id):
    user = request.user
    posting = get_object_or_404(Posting, id=posting_id)
    if user in posting.like_users.filter(id=user.id).exists():
        posting.like_users.remove(user)
    else:
        posting.like_users.add(user)
    return redirect(posting)

# @require_POST
# def create_posting(request):
    # posting = Posting()
    # posting.content = request.POST.get('content')
    # posting.icon = ''
    # posting.image = request.FILES.get('image')
    # posting.save()
    # return redirect(posting)