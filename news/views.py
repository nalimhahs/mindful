from django.shortcuts import render, get_object_or_404
from .models import News


def allnews(request):
    news = News.objects
    return render(request, 'news/allnews.html', {'news': news})


def detail(request, news_id):
    newsdetail = get_object_or_404(News, pk=news_id)
    return render(request, 'news/detail.html', {'new': newsdetail})
