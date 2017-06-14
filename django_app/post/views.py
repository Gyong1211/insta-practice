from django.http import HttpResponse
from django.shortcuts import render, redirect

from member.models import User
from .forms import CreatePost
from .models import Post, Comment


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context=context)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {
        'post': post,
    }
    return render(request, 'post/post_detail.html', context=context)


def post_create(request):
    if request.method == 'POST':
        forms = CreatePost(request.POST, request.FILES)
        if forms.is_valid():
            user = User.objects.get(id=2)
            post = Post.objects.create(author=user, photo=request.FILES['photo'])
            comment_string = forms.cleaned_data['comment']
            if comment_string:
                post.comment_set.create(author=user, content=comment_string)
            return redirect('post:post_detail', post_pk=post.id)
        else:
            forms = CreatePost()
            context = {
                'forms': forms,
            }
            return render(request, 'post/post_create.html', context=context)
    else:
        forms = CreatePost()
        context = {
            'forms': forms,
        }
        return render(request, 'post/post_create.html', context=context)
