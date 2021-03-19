from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class NewsList(ListView):
    model = Post
    template_name = 'news/newslist.html'
    context_object_name = 'newslist'
    queryset = Post.objects.order_by('-time_in') # выводим первыми самые свежие новости

class NewsDetail(DetailView):
    model = Post
    template_name = 'news/newsdetail.html'
    context_object_name = 'newsdetail'  
