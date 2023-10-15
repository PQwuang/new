from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# from ckeditor.fields import RichTextField

class Category(models.Model):
    name=models.CharField(max_length=225)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')
    
    class profiles(models.Model):
        users = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
        bio = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image= models.ImageField(null=True, blank=True)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models)
    # body = RichTextField(blank=True, null=True)
    Postdate = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255, default='coding')
    like = models.ManyToManyField(User, related_name="blog_post")

    def total_likes(self):
        return self.like.count()

    def __str__(self):
        return self.title +' | '+ str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')