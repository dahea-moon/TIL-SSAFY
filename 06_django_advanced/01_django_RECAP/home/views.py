from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'home/index.html')


def guess(request):
    return render(request, 'home/guess.html')

def answer(request):
    count = 0
    wrong = 0
    if request.POST.get('q1') == '0512':
        count += 1
    else:
        wrong += 1

    if request.POST.get('q2') == 'blue':
        count += 1
    else:
        wrong += 1

    if request.POST.get('q3') == 'food':
        count += 1
    else:
        wrong += 1

    return render(request, 'home/answer.html',  {'count': count, 'wrong': wrong})
