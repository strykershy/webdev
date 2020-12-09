from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse('home')
    return render(request, 'index.html')

def about(request):
    #return HttpResponse('about')
    return render(request, 'about.html')