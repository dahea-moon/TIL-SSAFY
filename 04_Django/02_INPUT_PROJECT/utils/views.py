from django.shortcuts import render, redirect, HttpResponse
from art import *
from decouple import config
import requests


def index(request):
    return render(request, 'utils/index.html')


def art(request):
    fonts = ['cola', 'coinstak', 'cards', 'lildevil', 'bigchief']
    return render(request, 'utils/art.html', {
        'fonts': fonts
    })


def output(request):
    user_input = request.GET.get('user-input')
    font = request.GET.get('user-font')
    if not font:
        font = 'random'

    if user_input:
        result = text2art(user_input, font=font)
        return render(request, 'utils/output.html', {
            'result': result,
        })
    else:
        return redirect('/utils/art/')


def throw(request):
    return render(request, 'utils/throw.html')


def catch(request):
    earth_date = request.GET.get('earth_date')
    NASA_API_KEY = config('NASA_API_KEY')

    BASE_URL = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

    URL = BASE_URL + '?earth_date=' + earth_date + '&api_key=' + NASA_API_KEY

    res = requests.get(URL).json()
    images = res.get('photos')

    return render(request, 'utils/catch.html', {
        'images': images,
    })
