from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required

from .models import Posting, Image
from .forms import PostingForm, ImageForm


@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    return render(request, 'postings/posting_detail.html', {
        'posting': posting,
    })


@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'postings/posting_list.html', {
        'postings': postings,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def create_posting(request):
    # image 일단 받기
    images = request.FILES.getlist('file')

    if request.method == 'POST':
        # image 보다 posting 먼저 확인
        posting_form = PostingForm(request.POST)
        # if posting_form.is_valid():
        if posting_form.is_valid() and len(images) <= 5:  # image 5개 까지만 받기
            posting = posting_form.save(commit=False)
            posting.author = request.user
            posting.save()  # 이미 save 되었는데 image 검증 어떻게 하지?
            # posting 이 있어야 id 등등 있음
            for image in images:
                request.FILES['file'] = image
                image_form = ImageForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.posting = posting  # posting 을 save 안하면 id 가 안나와서 이부분 못함
                    image.save()
            return redirect(posting)

        
        # for image in request.FILES.getlist('file'):
        #     # 하나씩 돌면서 FILES 에 image 저장
        #     request.FILES['file'] = image
        #     image_form = ImageForm(files=request.FILES)  # form 류는 request 로 시작하는 객체여야만 사용(저장) 가능
        #     if image_form.is_valid():
        #         image = image_form.save()
        
    else:
        posting_form = PostingForm()
        image_form = ImageForm()
    return render(request, 'postings/posting_form.html', {
        'posting_form': posting_form,
        'image_form': image_form,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def update_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.method == 'POST':
        form = PostingForm(request.POST, instance=posting)
        if form.is_valid():
            # posting = form.save(commit=False)
            # posting.author = request.user
            # posting.save()
            # 작성자 채워져 있으니까, 또 쓸 필요없음
            posting = form.save()
            return redirect(posting)
    else:
        form = PostingForm(instance=posting)
    return render(request, 'postings/posting_form.html', {
        'form': form,
    })


@login_required
@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('postings:posting_list')
