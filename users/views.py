from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *


# Create your views here.

def index(request):
    user = {"name": "Ainazik","age": 23}
    data = {"users": user}
    return render(request,'index.html' , context=data)

def index2(request):
    data={"n": 5}
    return render(request,'index2.html' , context=data)

def index3(request):
    langs =["Python" , "JavaScript" , "Java", "C#", "C++"]
    data = {'langs': langs}
    return render(request,'index3.html' , context=data)

def practice(request):
    lst = [1,2,3,4,5,6,7,8,9,10]
    lst1 = []
    for i in lst:
        if i % 2 == 0:
            lst1.append(i)
    data = {"lst": lst1}
    return render(request, 'practice.html', context=data)

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Women.objects.all()
    return render(request, 'index5.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'about.html', {'menu': menu, 'title': 'О сайте'})

