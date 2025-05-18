from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from core import models
from django.contrib import messages


def news(request):
    template_name = "news/news.html"
    news_ = models.BlogPost.objects.filter(published = True)
    page = request.GET.get('page', 1)
    paginator = Paginator(news_, 8)
    news = paginator.page(page)
    return render(request,template_name,{'news':news})

def news_details(request, slug):
    template_name = "news/news_details.html"
    obj = get_object_or_404(models.BlogPost, slug=slug)
    news_ = models.BlogPost.objects.filter(published = True).exclude(id=obj.id)[:5] 
    return render(request,template_name,{'obj':obj,'news':news_})