from django.shortcuts import render, redirect

from django.views import View

from .forms import AddBlogForm, BlogUpdateForm
from .models import *

class BasicView:
    def category(self):
        return Category.objects.all()
    def tag(self):
        return Tag.objects.all()

class Home(BasicView, View):
    def get(self,request):
        context = {}
        context['blogs'] = Blog.objects.all()
        context['categories']= self.category()
        context['tags'] = self.tag()
        return render(request,'blogapp/home.html',context)

class CategoryBlog(BasicView, View):
    def get(self, request, slug):
        context = {}
        category= Category.objects.get(slug=slug)
        context['blogs'] = Blog.objects.filter(category=category)
        context['category']=category
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return render(request, 'blogapp/home.html', context)

class TagBlog(BasicView, View):
    def get(self, request, slug):
        context = {}
        tag = Tag.objects.get(slug=slug)
        context['blogs'] = Blog.objects.filter(tags=tag)
        context['tag'] = tag
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return render(request, 'blogapp/home.html', context)


class BlogDetail(BasicView,View):
    def get(self, request, slug):
        blog=Blog.objects.get(slug=slug)
        blog.views += 1
        blog.save()
        context = {
            'blog':blog,
            'categories':self.category(),
            'tags':self.tag()
        }
        return render(request,'blogapp/blog_detail.html',context)

class CategoryList(BasicView, View):
    def get(self, request):
        context = {
            'categories':self.category(),
            'tags':self.tag(),
        }
        return render(request, "blogapp/category_list.html",context)

class AddBlogView(BasicView, View):
    def get(self, request):
        context={
            'categories':self.category(),
            'tags':self.tag(),
            'form':AddBlogForm(),
        }
        return render(request, 'blogapp/add_blog.html', context)
    def post(self, request):
        form = AddBlogForm(request.POST, request.FILES)
        if form.is_valid():
            form_create = form.save(commit=False)
            form_create.slug = slugify(form_create.title)
            form_create.user = request.user
            form_create.save()

            blog = Blog.objects.get(id = form_create.id)
            tags = form.cleaned_data['tags'].split(',')
            for tag in tags:
                tag, created= Tag.objects.get_or_create(name=tag.strip())
                blog.tags.add(tag)
            return redirect('home')

class UpdateBlogView(BasicView, View):

        def get(self, request, slug):
            blog = Blog.objects.get(slug=slug)
            satr = ''
            for tag in blog.tags.all():
                satr += str(tag) + ','
            satr = satr[0:len(satr)-1]
            context = {
                'categories':self.category(),
                'tags':self.tag(),
                'form':BlogUpdateForm(instance=blog),
                'satr':satr,
            }
            return render(request, 'blogapp/update_blog.html', context)

        def post(self, request, slug):
            blog = Blog.objects.get(slug=slug)
            form = BlogUpdateForm(request.POST, request.FILES, instance=blog)
            if form.is_valid():
                form_create = form.save(commit=False)
                form_create.slug = slugify(form_create.title)
                form_create.user = request.user
                form_create.save()
                tags = form.cleaned_data['tags'].split(',')
                for tag in tags:
                    tag, created = Tag.objects.get_or_create(name=tag.strip())
                    blog.tags.add(tag)
                return redirect('home')