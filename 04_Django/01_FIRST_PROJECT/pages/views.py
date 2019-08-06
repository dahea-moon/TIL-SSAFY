from django.shortcuts import render, HttpResponse
import json

# Create your views here.


def index(request):
    return HttpResponse('Hi django! :)')


def about(request):
    me = {
        'name': '문다혜',
        'role': 'Student',
        'email': 'dahea0512@gmail.com'
    }

    return HttpResponse(json.dumps(me))


def portfolio(request):
    return render(request, 'portfolio.html')


def help(request):
    return render(request, 'help.html')
