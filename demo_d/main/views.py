from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'main/landing.html')

def learn(request):
    return render(request, 'main/learn.html')

def categories(request):
    return render(request, 'main/categories.html')