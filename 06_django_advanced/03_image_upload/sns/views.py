from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .models import Posting


@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    context = {'postings': postings}
    return render(request, 'sns/posting_list.html', context)


@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    context = {'posting': posting}
    return render(request, 'sns/posting_detail.html', context)


@require_POST
def create_posting(request):
    posting = Posting()
    posting.content = request.POST.get('content')
    posting.icon = ''
    posting.image = request.FILES.get('image')
    posting.save()
    return redirect(posting)