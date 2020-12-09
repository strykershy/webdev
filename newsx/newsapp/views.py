from django.shortcuts import render
from .models import Article

def newsitems(request):
    articles = Article.objects.all().order_by('date_published')
    return render(request, 'newsapp/newsitems.html', {'articles': articles})