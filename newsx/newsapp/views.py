from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def newsitems(request):
    articles = Article.objects.all().order_by('date_published')
    return render(request, 'newsapp/newsitems.html', {'articles': articles})

def details(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request,'newsapp/detail.html', {'article' : article})

@login_required(login_url="/account/login/")
def user_profile(request):
    return render(request, 'newsapp/profile.html')