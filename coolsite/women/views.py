from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from coolsite import settings

menu = [
        {'title' : "о сайте", 'url_name': 'about'},
        {'title' : "Добавить статью", 'url_name': 'add_page' },
        {'title' : "Обратная связь", 'url_name': 'contact'},
        {'title' : "Войти", 'url_name': 'login'}
]

from .models import *

def index(requets):
    posts = Women.objects.all()

    context = {
               'posts': posts,
               'menu': menu,
               'title': 'Главная страница',
               'cat_selected': 0,
    }
    return render(requets, 'women/index.html' , context=context )

def about(request):
    return render(request, 'women/about.html',{'menu': menu, 'title': 'О сайте' })

def add_page(request):
    return HttpResponse('Добавить статью')

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def show_post(request, post_id ):
    return HttpResponse(f'Отабражение статьи с id = {post_id}')

def pageNotFound(request,exception):
    return HttpResponseNotFound("<h1>Страница не найден<h1>")

def show_category(request, cat_id ):
    posts = Women.objects.filter( cat_id = cat_id )


    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отабражение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html' , context=context)



