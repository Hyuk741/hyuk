"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.http import HttpResponse, Http404
from django.shortcuts import render



movie_list = [
    {'title': '파묘', 'director': '장재현'},
    {'title': '윙카', 'director': '폴 킴'},
    {'title': '둠 : 파트 2', 'director': '도니 벨뇌브'}


]

def index(request):
    return HttpResponse('<h1>hello</h1>')

def book_list(request):
    # book_text = ''
    #
    # for i in range(0,10):
    #     book_text += f'book {i}<br>'
    #
    # return HttpResponse(book_text)
    return  render(request, 'book_list.html', {'range': range(0,10)})

def book(request, num):
    return render(request, 'book_detail.html', {'num': num})

def language(request, lang):
    return  HttpResponse(f'<h1>{lang}언어 페이지입니다.')

def movies(request):


    return render(request,'movies.html', {'movie_list': movie_list})
def movie_detail(request, index):
    if index > len(movie_list) - 1 :
        raise Http404

    movie = movie_list[index]
    context = {'movie': movie}

    return render(request, 'movie.html', {'movie':movie})

def gugu(request, num):
    context = {
        'num' : num,
        'results' : [(i, num * i)for i in range(1,10)]
    }
    return render(request, 'gugu.html', context)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('book_list', book_list),
    path('book_list/<int:num>/', book),
    path('language/<str:lang>/', language),
    path('movie/', movies),
    path('movie/<int:index>/', movie_detail),
    path('gugu/<int:num>/', gugu),

]
