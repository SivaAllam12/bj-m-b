from django.shortcuts import render,get_object_or_404
from .models import Blog


def blog(request):
    blogs=Blog.objects
    return render(request,"blogpage.html",{'blogs':blogs})

def details(request,blog_id):
    detail_blog=get_object_or_404(Blog, pk=blog_id)
    return render(request,"detailpage.html",{'detail_blog':detail_blog})