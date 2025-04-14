from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import BlogModel
from .forms import BlogForm
from .util.recomend import tag_recommend
from .util.dummy_blog import create_dummy_users_and_blogs
class Home(LoginRequiredMixin,TemplateView):
    template_name = 'html/blog/home.html'
    
    # sending recomended blogs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Default to 10 blogs, or get the count from ?limit=
        limit = int(self.request.GET.get('limit', 10))
        context['limit'] = limit
        context['next_limit'] = limit + 30
        context['recomended_blog'] = tag_recommend(self.request.user, top_k=limit)
        return context
    
    
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
    
    
def DummyData(request):
    if create_dummy_users_and_blogs():
        return HttpResponse('Created Dummy Blog')
    else:
        return HttpResponse("Error in creating Dummy Blog")