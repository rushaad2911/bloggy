from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4
from ..user.models import Interest
    

class Tags(models.Model):
    name = models.CharField(max_length=50)
    
    
class BlogPage(models.Model):
    id = models.URLField(primary_key=True,unique=True,default=uuid4)
    title = models.CharField(blank=False, null=False,max_length=100)
    content = models.TimeField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='blog_content')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tags,related_name='blog_tags')
    
    
    def __str__(self):
        return self.title
    
    def peek(self):
        return self.content[:101]+'....'
    
    
    
