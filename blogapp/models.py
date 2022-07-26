from django.db import models
from django.utils.text import slugify

from userapp.models import UserProfile

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(UserProfile)
    image = models.ImageField(upload_to='category/%Y/%m/%d/')
    content = models.TextField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to="blog/%Y/%m/%d/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text