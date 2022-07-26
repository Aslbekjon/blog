from django.urls import path
from .views import *

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('category/<slug:slug>',CategoryBlog.as_view(),name='category_blog'),
    path('tag/<slug:slug>',TagBlog.as_view(),name='tag_blog'),
    path('blog/<slug:slug>',BlogDetail.as_view(),name='blog_detail'),
    path('categories',CategoryList.as_view(),name='category_list'),
    path('add_blog',AddBlogView.as_view(),name='add_blog'),
    path('update_blog/<slug:slug>',UpdateBlogView.as_view(),name='update_blog'),
]