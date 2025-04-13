# apps/blog/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('',Home.as_view(), name='blog_home'),
]
