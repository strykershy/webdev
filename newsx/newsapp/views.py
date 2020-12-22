from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def newsitems(request):
    articles = Article.objects.all().order_by('date_published')
    return render(request, 'newsapp/newsitems.html', {'articles': articles})

def details(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request,'newsapp/detail.html', {'article' : article})

@login_required(login_url="/account/login/")
def user_profile(request):
    if request.method == 'POST':
        form = forms.AddArticle(request.POST,request.FILES)
        if form.is_valid():
            savetouser = form.save(commit=False)
            savetouser.author = request.user
            savetouser.save()
            return redirect('articles:items')
    else:
        form = forms.AddArticle()
    return render(request, 'newsapp/profile.html', {'form': form})