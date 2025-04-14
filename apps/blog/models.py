from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4
from ..user.models import Interest
from sentence_transformers import SentenceTransformer
from .util.vectorize import create_embedding  # Import your vector creation function
from django.core.exceptions import ValidationError    


class BlogModel(models.Model):
    id = models.UUIDField(primary_key=True,unique=True,default=uuid4)
    title = models.CharField(blank=False, null=False,max_length=100)
    content = models.TextField(blank=False,null=False)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='blog_content')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Interest, related_name='blog_tags', blank=True)  # Reference to Interest
    vectorized = models.JSONField(blank=True,null=True)
    
    
    def __str__(self):
        return self.title
    
    def peek(self):
        return self.content[:101]+'....'
    
    
    def save(self, *args, **kwargs):
        print("saving the model")
        # Generate the embedding only if it does not already exist or the blog is being created
        if not self.vectorized:
            # Check if the vector is generated successfully
            vector = create_embedding(self.title, self.tags.all())
            
            if not vector:
                raise ValidationError("Vector generation failed, blog will not be saved.")
            
            self.vectorized = vector  # Set the generated vector
            print(self.vectorized)
        super().save(*args, **kwargs)  

