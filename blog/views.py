from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost


def index(request):
    blog_data = Blogpost.objects.all()
    # print(blog_data)
    # print(type(blog_data))
    # for item in blog_data:
    #     print(item,item.title,item.head0)

    return render(request,'blog/index.html',{'blogs':blog_data,'range':range(3)})


def blogpost(request,postid):
    blog_data = Blogpost.objects.filter(post_id=postid)
    # print(blog_data.title)
    return render(request,'blog/blogpost.html',{"post":blog_data[0]})