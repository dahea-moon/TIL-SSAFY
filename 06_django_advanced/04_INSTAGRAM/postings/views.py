from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from .forms import PostingForm
from .models import Posting

@require_GET
def posting_detail(request,  posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    return render(request, 'postings/posting_detail.html', {
        'posting': posting,
    })


@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'postings/posting_list.html', {
        'postings': postings,
    } )

@login_required
@require_http_methods(['GET', 'POST'])
def create_posting(request):
    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():
            posting = form.save(commit=False)
            posting.author = request.user
            posting.save()
            return redirect(posting)
        
    else:
        form = PostingForm()
    return render(request, 'posting/form.html', {
        'form': form,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def update_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.method == 'POST':
        form = PostingForm(request.POST, instance=posting)
        if form.is_valid():
            posting = form.save()
            return redirect(posting)
        
    else:
        form = PostingForm(instance=posting)
    return render(request, 'posting/form.html', {
        'form': form,
    })

@login_required
@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('postings:posting_list')
