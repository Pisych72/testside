from django.shortcuts import render,get_list_or_404,redirect
from django.shortcuts import HttpResponse
from .models import *
from .forms import NewsForm
from django.views.generic import ListView
# Create your views here.
class HomeView(ListView):
    model = news
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'


def index(request):

    new=news.objects.all()

    context={'new':new,
             'title':'Список новостей',
             }
    return render(request,'news/index.html',context)

class NewsByCategory(ListView):
    model = news
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    def get_queryset(self):
        return news.objects.filter(category_id=self.kwargs['category_id'],is_published=True)
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']=Category.objects.get(pk=self.kwargs['category_id'])
        return context


def get_category(request,category_id):
    new=news.objects.filter(category_id=category_id)

    category=Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'new':new,'category':category})

def view_news(request,news_id):
   # news_item=news.objects.get(pk=news_id)
    news_item=get_list_or_404(news,pk=news_id)
    return render(request,'news/view_news.html',{'news_item':news_item})

def add_news(request):
    if request.method=='POST':
        form=NewsForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
           # news1= news.objects.create(**form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form=NewsForm()
    return render(request,'news/add_news.html',{'form': form} )