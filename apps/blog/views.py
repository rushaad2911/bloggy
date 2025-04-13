from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginRequiredMixin,TemplateView):
    template_name = 'html/blog/home.html'
    