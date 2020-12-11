from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def newsitems(request):
    articles = Article.objects.all().order_by('date_published')
    return render(request, 'newsapp/newsitems.html', {'articles': articles})

def details(request, slug):
    return HttpResponse(slug)