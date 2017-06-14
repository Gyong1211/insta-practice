from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html',context=context)


def post_detail(request, post_pk):
    return HttpResponse('Post Detail')
