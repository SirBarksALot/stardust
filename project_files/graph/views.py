from django.shortcuts import render
from datetime import datetime

posts = [
    {
        'author': 'filip',
        'title': 'post 1',
        'content': '1 post content',
        'date_posted': datetime. now(),
    },
    {
        'author': 'filip',
        'title': 'post 2',
        'content': '2 post content',
        'date_posted': datetime. now(),
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'graph/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'graph/about.html', context)
