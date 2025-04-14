from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import BlogModel
from .forms import BlogForm
class Home(LoginRequiredMixin,TemplateView):
    template_name = 'html/blog/home.html'
    
    
    
class CreateBlog(LoginRequiredMixin,CreateView):
    model = BlogModel
    template_name = 'html/blog/createblog.html'
    success_url = reverse_lazy('blog_home')
    form_class = BlogForm
    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)

class DeleteBlog(DeleteView):
    model = BlogModel
    template_name = 'html/blog/deleteblog.html'
    success_url = reverse_lazy('blog_home')
    