from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

#папка для создания html страниц для разных путей сайта
def index(request):
    posts = Messager.objects.all()#получить ссылки на все содержимое базы данных
    cats = Categories.objects.all()
    cat_selected = 0
    menu =  'главная', 'админка', 'войти/зарегистрироваться'
    return render(request, 'messager/index.html', {'menu':menu, 'title':'Главная страница', 'posts':posts, 'cats':cats, 'cat_selected':cat_selected})#шаблон главной страницы, переменные дял шаблона третьим аргументом
def profile(request):
    #вывод инофрмации после знака ? (/profile/?name=pivo)
    if request.GET:
        print(request.GET)
    return HttpResponse('Ваш профиль')

def archive_year(request, year):
    if year>2023 and year<3000:
        return redirect('/', permanent=True)#перенаправление на другую страницуб тру для кода 301, ничего или фолс для когда 302
    elif year>3000 and year<4000:
        return redirect(index)#обращение напрямую к функции
    elif year>4000:
        return redirect('home')#переход через имя пути
    return HttpResponse(f'год:{year}')
def archive(request):
    return HttpResponse('Введите год')
def categories_int(request, cat_id):
    posts = Messager.objects.filter(cat_id=cat_id)  # получить ссылки на все содержимое базы данных
    if len(posts) == 0:
        raise Http404()
    cats = Categories.objects.all()
    cat_selected = cat_id

    menu = 'главная', 'админка', 'войти/зарегистрироваться'
    return render(request, 'messager/index.html',{'menu': menu, 'title': 'категории', 'posts': posts, 'cats': cats,'cat_selected': cat_selected})
def categories_slug(request, cat_slug):
    return HttpResponse(f'Категория название:{cat_slug}')
def anketa(request):
    return render(request, 'messager/index7.html')
def page_not_found(request, exception):
    return HttpResponseNotFound(f'<h1>Страницы по такому пути не существует</h1>')
def registration(request):
    return render(request, 'messager/registration.html')