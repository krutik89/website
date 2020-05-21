from django.shortcuts import render,HttpResponse
from .models import Blog
# Create your views here.
def blog(request):
    allPosts = Blog.objects.all()
    context = {'allPosts':allPosts}
    return render(request,'blog/blog.html',context)
def blogpost(request,slug):
    return render(request,'blog/blogpost.html')