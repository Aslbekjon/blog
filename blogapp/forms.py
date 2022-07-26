from django import forms
from .models import Blog

class AddBlogForm(forms.ModelForm):
    tags = forms.CharField(max_length=500)
    class Meta:
        model = Blog
        fields = ['title','content', 'image','category']

class BlogUpdateForm(forms.ModelForm):
    tags = forms.CharField(max_length=500)
    class Meta:
        model = Blog
        fields = ['title','content','image','category']