# apps/blog/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('',Home.as_view(), name='blog_home'),
    path("create/",CreateBlog.as_view(),name="create_blog"),
    path('delete/<uuid:pk>/',DeleteBlog.as_view(),name="delete_blog"),
    path('dummy/',DummyData,name="dummydata"),
    
    
]
