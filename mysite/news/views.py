from django.shortcuts import render,get_list_or_404
from django.shortcuts import HttpResponse
from .models import *
# Create your views here.
def index(request):

    new=news.objects.all()

    context={'new':new,
             'title':'Список новостей',

             }
    return render(request,'news/index.html',context)

def get_category(request,category_id):
    new=news.objects.filter(category_id=category_id)

    category=Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'new':new,'category':category})

def view_news(request,news_id):
   # news_item=news.objects.get(pk=news_id)
    news_item=get_list_or_404(news,pk=news_id)
    return render(request,'news/view_news.html',{'news_item':news_item})