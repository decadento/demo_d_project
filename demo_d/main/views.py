from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def landing(request):
    return render(request, 'main/landing.html')

def learn(request):
    return render(request, 'main/learn.html')

def categories(request):
    return render(request, 'main/categories.html')

def landing_eng(request):
    return render(request, 'main/landing_eng.html')