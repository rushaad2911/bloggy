from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

class Interest(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class BlogUser(AbstractUser):
    id = models.UUIDField(default = uuid4,primary_key=True,unique=True)
    interest = models.ManyToManyField(Interest,related_name='user_interest',blank=False)
    
    def __str__(self):
        return self.username
    