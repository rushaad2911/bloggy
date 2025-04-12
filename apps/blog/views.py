from django.shortcuts import render
# apps/blog/views.py
from django.http import HttpResponse



def home(request):
    return HttpResponse("Welcome to the Blog!")
